class Solution:

    def fn_score_words(self, letter_dict, begin_pointer: int = 0, sum: int = 0)-> int:        

        ld = letter_dict.copy()

        current_word = self.words[begin_pointer]
        
        for letter in current_word: # For each letter of the word
            # If the letter is not available return. 
            print(f"current letter: {letter}")
            if ld[letter] == 0:
                sum = -1
                break

            ld[letter] -= 1

        output = sum
        if sum != -1:
            sum += self.score_words[current_word]
            output = sum   
            for i in range(begin_pointer + 1, len(self.words)):
                output = max(output, self.fn_score_words(ld, i, sum))


        if (begin_pointer + 1) < len(self.words):
            output = max(output, self.fn_score_words(self.letter_dict, begin_pointer + 1, 0))  

        return output

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        self.words = words
        self.solution = 0

        self.letter_dict = DefaultDict(int) 
        for l in letters: 
            self.letter_dict[l] += 1

        self.score_letters = {string.ascii_lowercase[i] : score[i] for i in range(len(score)) if score[i] != 0}

        # We iterate over the words and get their score
        self.score_words = {}

        remove_words = []

        for w in words:
            self.score_words[w] = 0
            for _ in w:
                if _ not in self.score_letters:
                    remove_words.append(w)
                    break
                self.score_words[w] += self.score_letters[_]
       
        for w in remove_words:
            self.score_words.pop(w)
            self.words.remove(w)


        return max(0,self.fn_score_words(self.letter_dict))