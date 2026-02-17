from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current_number = None # Stores the current number we are comparing to
        counter = 0 # Counter of non repeated values
        duplicate_counter = 0 # Counter of duplicate values

        for idx in range(len(nums)):

            # If the current number is duplicated, add one to the counter
            if current_number == nums[idx]:
                duplicate_counter += 1
            else:
                # If we find a new number, the new number is going to be copied to the last position.
                nums[idx - duplicate_counter] = nums[idx]
                current_number = nums[idx]
                counter += 1
            
        return counter