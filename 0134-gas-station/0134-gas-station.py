class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        if total_gas < 0:
            return -1

        return start