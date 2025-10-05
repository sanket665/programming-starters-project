class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        tank = 0
        start = 0
        n = len(gas)
        
        for i in range(n):
            diff = gas[i] - cost[i]
            total_tank += diff
            tank += diff
            
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start if total_tank >= 0 else -1
