class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        counter = 0
        finished_word = False

        for c in s:
            if c != ' ':
                
                if finished_word: 
                    counter = 0
                    finished_word = False

                counter += 1

            else:
                finished_word = True

        return counter