from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # We are going to create a hash map at the same time we are looking for the answer
        # x is going to be the current index. Therefore: target - x = The other number
        # Create a hashmap where to store each number and its index, if the found number is in pair we got it.

        number_idx = dict()

        for i, x in enumerate(nums):
            value = target - x
            
            if value in number_idx: # If we already found the number return the solution
                return [i, number_idx[value]]
            
            # If not we add the number to the index
            number_idx[x] = i