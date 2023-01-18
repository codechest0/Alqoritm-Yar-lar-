# BFS Algorithms :D

def AddimSayiTap(coordA, coordB):
    x1, y1 = coordA
    x2, y2 = coordB
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    queue = []
    queue.append((x1-1, y1-1, 0))
    visited = [[False for i in range(8)] for j in range(8)]
    visited[x1-1][y1-1] = True
    while queue:
        x, y, count = queue.pop(0)
        if x == x2-1 and y == y2-1:
            return count
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, count + 1))
    return -1

print(AddimSayiTap([3,5], [8, 2]))
