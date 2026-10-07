class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        lr=0
        rr=0
        for ch in s:
            if ch == '(':
                lr+=1
            elif ch==')':
                if lr>0:
                    lr-=1
                else:
                    rr+=1
        ans=set()
        def backtrack(index,current,balance,l,r):
            if balance<0:
                return
            if index==len(s):
                if balance==0 and l==0 and r==0:
                    ans.add("".join(current))
                return
            ch=s[index]
            if ch == '(' and l > 0:
                backtrack(index + 1, current,balance, l- 1, r)
            if ch == ')' and r > 0:
                backtrack(index+1,current,balance, l, r - 1)
            current.append(ch)
            if ch == '(':
                backtrack(index+1,current,balance + 1, l, r)
            elif ch == ')':
                backtrack(index+1,current,balance - 1, l, r)
            else:
                backtrack(index+1,current,balance, l, r)
            current.pop()
        backtrack(0, [], 0, lr, rr)
        return list(ans)