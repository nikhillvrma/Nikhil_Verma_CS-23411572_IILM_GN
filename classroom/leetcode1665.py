class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = 0
        curr = 0
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)
        for i in range(len(tasks)):
            if tasks[i][1]>curr:
                ans += (tasks[i][1] - curr)
                curr = tasks[i][1]
            curr = curr - tasks[i][0]
        return ans