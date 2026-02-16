class Solution:
    def integerReplacement(self, n: int) -> int:
        
        stack_of_odds = []
        current_number = n
        steps = 0
        possibilities_left = True
        minimum = float('inf')

        while possibilities_left:

            # Check if we are at the target (1) already.
            # If we are, get another one more from the start
            # Change the minimum
            if current_number == 1:
                minimum = min(minimum, steps)
                if not stack_of_odds:
                    return minimum
                else:
                   # If there are still odds, we have to change all the variables
                   current_number, steps = stack_of_odds.pop()
                   continue

            if minimum <= steps:
                if stack_of_odds:
                    current_number, steps = stack_of_odds.pop()
                    continue
                return minimum
            # Check if its odd or even
            # Even
            if current_number % 2 == 0:
                current_number /= 2 # Divide by two
                steps += 1
            else:
                stack_of_odds.append((current_number + 1, steps + 1))
                current_number, steps = current_number - 1, steps + 1 
        return minimum
    
print(Solution().integerReplacement(15))