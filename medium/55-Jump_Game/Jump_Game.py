from typing import List

class Solution:

    # Example: nums = [2,3,1,1,4]
    def canJump(self, nums: List[int]) -> bool:

        bool_array = [True] * (len(nums) + 1)
        LAST_INDEX = len(nums) - 1


        pos = 0
        penalty = 0
        current_value = nums[0]
        stack = [[pos, penalty]]

        while stack:

            # If we can reach the end it's over
            if (pos + current_value) >= LAST_INDEX: return True

            # Check if this is a final position (we can not reach longer)
            if (current_value - penalty) <= 0:
                bool_array[pos] = False
                stack.pop()
                if not stack: return False
                stack[-1][-1] += 1
                pos, penalty = stack[-1]
                current_value = nums[pos]
                continue
            

            n_pos = pos + current_value - penalty
            if bool_array[n_pos]: # Check if we can keep going
                
                pos = n_pos
                current_value = nums[pos]
                penalty = 0
                stack.append([pos, penalty]) # penalty is 0
            
            else: # If we can not stay with the same  current value and position and increase penalty
                penalty += 1
                stack[-1][-1] += 1
            
        
        return bool_array[0]

print(Solution().canJump([1,0,4,1,4,3,0,4]))