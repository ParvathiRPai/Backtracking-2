# Time and space complexity is O(2^N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []
        
        def dfs(i):
            if i>=len(s):
                result.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
                    
        dfs(0)
        return result
    
    
    def isPalin(self, s, l , r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
            
                    
                