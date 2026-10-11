class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        time=[]
        for i in range(len(dist)):
            min=(dist[i]+speed[i]-1)//speed[i]
            time.append(min)
        time.sort()
        for i in range(len(time)):
            if time[i]<=i:
                return i
        return len(time)