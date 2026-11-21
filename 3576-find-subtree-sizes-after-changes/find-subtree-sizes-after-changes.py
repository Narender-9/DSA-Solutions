class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        children=[[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        newParent=parent[:]
        last={}
        def dfs(node):
            old=last.get(s[node], -1)
            if old!=-1:
                newParent[node]=old
            last[s[node]]=node
            for child in children[node]:
                dfs(child)
            if old==-1:
                last.pop(s[node],None)
            else:
                last[s[node]]=old
        dfs(0)
        tree=[[] for _ in range(n)]
        for i in range(1, n):
            tree[newParent[i]].append(i)
        ans=[1]*n
        def count(node):
            for child in tree[node]:
                ans[node]+=count(child)
            return ans[node]
        count(0)
        return ans