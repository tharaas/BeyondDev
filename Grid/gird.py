#Suppose you have a grid of n x m cells, where each cell is either empty or contains a
#rock. You're given a starting position in the grid (x,y), and you want to reach a target position (tx,ty),
#but you can only move in four directions (up, down, left, right) and you can only move through empty cells.
#You're also given a limited number of moves k that you can make. Write a program to determine if it's possible to reach the target position from the starting position within k moves.


def findPath(grid, start, target, k, n, m):
    if k == 0:
        return False

    dp = []
    for i in range(n):
        layer = []
        for j in range(m):
            list = [False] * (k + 1)
            layer.append(list)
        dp.append(layer)

    row, col = start
    dp[row][col][0] = True

    for moves in range(1, k + 1):
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    continue

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and dp[nx][ny][moves - 1]:
                        dp[x][y][moves] = True

    return dp[target[0]][target[1]][k]


n = 3
m = 3
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
start = (0, 0)
target = (2, 2)
k = 6
print("k=", k, findPath(grid, start, target, k, n, m))


k = 3
print("k=", k, findPath(grid, start, target, k, n, m))
