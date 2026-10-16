class FenwickTree:
    def __init__(self, size):
        self.tree1 = [0] * (size + 2)
        self.tree2 = [0] * (size + 2)

    def _add(self, tree, idx, delta):
        idx += 1  # 1-based indexing for Fenwick Tree
        while idx < len(tree):
            tree[idx] += delta
            idx += idx & (-idx)

    def _query(self, tree, idx):
        idx += 1
        total = 0
        while idx > 0:
            total += tree[idx]
            idx -= idx & (-idx)
        return total

    # Range add operation: adds 'delta' to all elements from L to R
    def range_add(self, L, R, delta):
        self._add(self.tree1, L, delta)
        self._add(self.tree1, R + 1, -delta)
        self._add(self.tree2, L, delta * (L - 1))
        self._add(self.tree2, R + 1, -delta * R)

    # Prefix sum query: returns sum of elements from 0 to idx
    def prefix_sum(self, idx):
        return self._query(self.tree1, idx) * idx - self._query(self.tree2, idx)

    # Range sum query: returns sum of elements from L to R
    def range_query(self, L, R):
        if L > R: return 0
        return self.prefix_sum(R) - self.prefix_sum(L - 1)


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        bit = FenwickTree(n)
        last_seen = {}
        
        total_ans = 0
        current_sum_sq = 0
        
        for j in range(n):
            k = last_seen.get(nums[j], -1)
            L, R = k + 1, j
            
            # 1. Get the sum of elements in the range [L, R] before updating
            range_sum = bit.range_query(L, R)
            range_len = R - L + 1
            
            # 2. Update our running sum of squares using the math expansion formula
            current_sum_sq = (current_sum_sq + 2 * range_sum + range_len) % MOD
            
            # 3. Add the current sum of squares to our final answer
            total_ans = (total_ans + current_sum_sq) % MOD
            
            # 4. Update the Fenwick tree range with +1
            bit.range_add(L, R, 1)
            
            # Record the last seen index
            last_seen[nums[j]] = j
            
        return total_ans
