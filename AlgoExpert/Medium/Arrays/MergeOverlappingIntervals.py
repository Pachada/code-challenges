"""
Merge Overlapping Intervals | AlgoExpert
Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, 
and returns the new intervals in no particular order.

Each interval interval is an array of two integers, with interval[0] as the start of the interval 
and interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. 
For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of that interval.

Sample Input
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
Sample Output
[[1, 2], [3, 8], [9, 10]]
// Merge the intervals [3, 5], [4, 7], and [6, 8].
// The intervals could be ordered differently.
"""

# Solution: To know if an interval overlaps with another we first need to make sure the intervals are sorted by their star value,
# then to know if an intervar overlas we need to see if the end value of the first intervals is greater or equal to the star value of
# the second interval. If this is true the it overlaps, and to create the new interval we grabe the start value of the first interval 
# and the max(firts interval end value, second interval end value). We add the result to a new list and continue with the next interval.

from typing import List

# O(nlogn) time | O(n) space
def mergeOverlappingIntervals(intervals: List[List[int]]):
    intervals.sort(key=lambda x: x[0]) # time: n log n
    result = [intervals[0]] # memory: n 
    for interval in intervals:
        start, end = interval
        last_interval = result[-1]
        _, last_end = last_interval
        if not result or last_end < start:
            result.append(interval)
        else:
            last_interval[1] = max(end, last_end)
        
            
    return result


if __name__ == "__main__":
    intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    result = mergeOverlappingIntervals(intervals)
    expected_output = [[1, 2], [3, 8], [9, 10]]
    assert result == expected_output
    print(result)