from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # First we are going to sort the list by the first index, (start time)
        intervals = sorted(intervals, key=lambda x: x[0])

        result = [intervals[0]]

        for start, end in intervals:

            # If the start of the next interval is overlapping
            if start <= result[-1][1]:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])

        return result