from typing import List

class Solution:

    def computeMinimum(self, idx):

        value = self.nums[idx]

        # If the value is 0 we can not jump from here
        if not value: return float('inf')

        # If we can reach the end
        # REVIEW THIS !!!!!
        if (idx + value) >= (self.n - 1):
            return 1

        # If we are in the last position is either 1 or 0
        if (idx == (self.n - 1)):
            return 1 if value > 0 else float('inf')

        # What is the reachable position with less steps
        return min(self.min_arr[idx+1:idx+1+value]) + 1
        

    def jump(self, nums: List[int]) -> int:
        
        self.nums = nums
        self.n = len(nums)

        # If there is only one item in the list
        if self.n < 2: return 0

        self.min_arr = [0] * (self.n)

        # Iterate for each position of the array backwards
        for idx in range(self.n-1, -1, -1):

            # Compute minimum and assing it to the min_array
            self.min_arr[idx] = self.computeMinimum(idx)
        
        return self.min_arr[0]

print(Solution().jump([2,3,1,1,4]))
