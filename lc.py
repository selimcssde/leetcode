from helper import TreeNode


class Solution(object):
    def allPossibleFBT(self, N):
        dp = [[] for _ in range(N+1)]
        dp[1] = [TreeNode(0)]

        def dfs(res):
            if dp[res]:
                return dp[res]
            ans = []
            i = 1
            while i < res:
                for left in dfs(i):
                    for right in dfs(res-1-i):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        ans.append(node)
                i += 2
            dp[res] = ans
            return ans

        return dfs(N)

N = 7
ans = Solution().allPossibleFBT(N)
arrs = [TreeNode.serialize(node) for node in ans]
for arr in arrs:
    print(arr)
