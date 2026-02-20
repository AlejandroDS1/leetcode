from typing import List
from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        previous_two_numbers = deque()
        
        def add_to_queue(n1):
            if len(previous_two_numbers) == 2:
                previous_two_numbers.popleft()
            previous_two_numbers.append(n1)


        TOTAL_LENGTH = len(nums1) + len(nums2)

        # Now that we have the total length we can already know in which position is going to be the median

        # If its an even number, there are going to be 2 numbers
        # If its an odd number, only one number
        IS_EVEN = TOTAL_LENGTH % 2 == 0

        # We are going to have a pointer for each list
        l1_idx = 0
        l2_idx = 0

        #TARGET_INDEX = (TOTAL_LENGTH // 2) - 1 if IS_EVEN else TOTAL_LENGTH // 2
        TARGET_INDEX = TOTAL_LENGTH // 2

        while (l1_idx + l2_idx) < TARGET_INDEX + 1:

            if l1_idx >= len(nums1):
                add_to_queue(nums2[l2_idx])
                l2_idx += 1
                continue
            elif l2_idx >= len(nums2):
                add_to_queue(nums1[l1_idx])
                l1_idx += 1
                continue

            if nums1[l1_idx] > nums2[l2_idx]:
                add_to_queue(nums2[l2_idx])
                l2_idx += 1
            elif nums1[l1_idx] < nums2[l2_idx]:
                add_to_queue(nums1[l1_idx])
                l1_idx += 1
            else: # They are equal
                add_to_queue(nums1[l1_idx])
                l1_idx += 1

                # Quick check if we reached the mid point before adding both
                if (l1_idx + l2_idx) > TARGET_INDEX:
                    break
                add_to_queue(nums2[l2_idx])
                l2_idx += 1

        return (previous_two_numbers[0] + previous_two_numbers[1]) / 2 if IS_EVEN else previous_two_numbers.pop()