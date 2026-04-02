class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        for i in intervals:
            if not result:
                result.append(i)
            else:
                last = result[-1]
                if i[0] <= last[1]:
                    last[1] = max(last[1], i[1])
                else:
                    result.append(i)
        return result
