from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        :itype, List[List[int]]
        :rtype, List[List[int]]
        :return, merged list.

        Examples
        --------
        input:
        >>> intervals = [[1,3],[2,6],[8,10],[15,18]]
        >>> obj = Solution()
        >>> obj.merge(intervals)
        output:
        >>> [[1,6],[8,10],[15,18]]
        """
        result_intervals = []
        intervals.sort()
        for idx in range(len(intervals)):
            if result_intervals == []:
                result_intervals.append(intervals[idx])
            else:
                res_end = result_intervals[-1][1]
                cur_start = intervals[idx][0]
                cur_end = intervals[idx][1]
                if res_end >=  cur_start:
                    result_intervals[-1][1] = max(res_end,intervals[idx][1])
                else:
                    result_intervals.append(intervals[idx])
        return result_intervals

if __name__ == '__main__':
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    obj = Solution()
    print(obj.merge(intervals))