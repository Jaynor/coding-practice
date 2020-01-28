from typing import List


def dfs_helper(x, y, grid):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
        return
    if grid[x][y] == 0:
        return

    grid[x][y] = 0
    dfs_helper(x - 1, y, grid)
    dfs_helper(x + 1, y, grid)
    dfs_helper(x, y - 1, grid)
    dfs_helper(x, y + 1, grid)

class Solution:
    def dfs(self, grid: List[List[int]]) -> int:
        total = 0
        for y in range(len(grid)):
            # print(grid[x])
            for x in range(len(grid[y])):
                if grid[x][y] == 1:
                    total += 1
                    dfs_helper(x, y, grid)
        return total




def main ():
    test_1 = Solution()
    print("Final result:", test_1.dfs([[1,1,1],[1,0,0],[0,1,0]]))


main()