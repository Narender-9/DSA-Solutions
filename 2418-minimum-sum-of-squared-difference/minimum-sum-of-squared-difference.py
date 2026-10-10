class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(diff) <= k:
            return 0
        count = [0] * 100001
        for d in diff:
            count[d] += 1
        for d in range(100000, 0, -1):
            if k == 0:
                break
            take = min(k, count[d])
            count[d] -= take
            count[d - 1] += take
            k -= take
        return sum(d * d * count[d] for d in range(100001))