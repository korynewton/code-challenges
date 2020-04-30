class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if sum(machines) % n != 0:
            return -1

        d_per_machine = sum(machines)//n

        # normalize to show how much should be removed per machine
        # (negative means dresses must be added)
        for i in range(len(machines)):
            machines[i] -= d_per_machine

        current_sum = max_sum = result = 0
        for m in machines:
            current_sum += m
            max_sum = max(max_sum, abs(current_sum))
            result = max(result, max_sum, m)

        return result
