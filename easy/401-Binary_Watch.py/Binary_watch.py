from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = [] # Here we store all the combinations

        # For every hour we iterate
        for hour in range(12):
            # For every minute we iterate
            for minute in range(60):

                # Transform hours and minutes to binary. Count the number of 1s and compare it to turnedOn
                if (bin(hour).count('1') + bin(minute).count('1')) == turnedOn:
                    # If there are the same amount of numbers, add it to the result array
                    result.append(f"{hour}:{minute:02d}")
        
        return result