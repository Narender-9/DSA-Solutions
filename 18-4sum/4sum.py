class Solution:
    def fourSum(self, num: list[int], tar: int) -> list[list[int]]:
        num.sort()
        n=len(num)
        res=[]
        for i in range(n):
            if i>0 and num[i]==num[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and num[j]==num[j-1]:
                    continue
                l,r=j+1,n-1
                while l<r:
                    tot=num[i]+num[j]+num[l]+num[r]
                    if tot==tar:
                        res.append([num[i],num[j],num[l],num[r]])
                        while l<r and num[l]==num[l+1]:
                            l+=1
                        while l<r and num[r]==num[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif tot<tar:
                        l+=1
                    else:
                        r-=1
        return res