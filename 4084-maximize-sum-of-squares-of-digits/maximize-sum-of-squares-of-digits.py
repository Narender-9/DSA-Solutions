class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        if sum_val>num*9:
            return ""
        count_9=sum_val//9
        r=sum_val%9
        non_zeros=count_9+(1 if r>0 else 0)
        if non_zeros>num:
            return ""
        count_0=num-non_zeros
        if r>0:
            return "9"*count_9+str(r)+"0"*count_0
        return "9"*count_9+"0"*count_0