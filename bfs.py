'''
m, n = map(int, input().split())

gridlist = list(map(int, input().split()))

tx, ty = map(int, input().split())


grid = [[0] * n for _ in range(m)]
vis = [[0] * n for _ in range(m)]

for i in range(m):
	grid[i] = gridlist[i*n: (i+1)*n]

sx = 0
sy = 0
v = 0
for i,x in enumerate(gridlist):
	if x > 0:
		v = x
		sx = i // n
		sy = i % n 
		break

q = [[sx, sy, v]]
vis[sx][sy] = 1
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
tag = 0
while q:
	if tag:
		break
	tmp = q
	q = []
	for x, y, v in tmp:
		if x == tx and y == ty:
			print(v)
			tag = 1
			break
		for dx, dy in dir:
			if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and vis[x +dx][y + dy] == 0  and grid[x +dx][y + dy] == 0:
				vis[x +dx][y + dy]= 1
				q.append([x+dx, y+dy, 0 if v - 1 < 0 else v - 1])
'''
# better

# 搜索的四个方向
D = [(0,1), (1,0), (-1,0), (0,-1)]

m, n = map(int, input().split())
lst = list(map(int, input().split()))
target_x, target_y = map(int, input().split())

# 需要把lst转化为常用的grid二维数组
grid = []
for i in range(0, m*n, n):
    # lst中的每n个元素作为一行，存入grid中
    grid.append(lst[i:i+n])

q = []

# 双重循环遍历grid，寻找信号源
for i in range(m):
    for j in range(n):
        # 0表示空地，-1表示阻碍，故grid[i][j]大于0时，点(i,j)是信号源
        if grid[i][j] > 0:
            # 将信号源存入队列q中，作为BFS的起始位置
            q.append((i, j))
            # 获得信号源的强度intensity
            intensity = grid[i][j]
            # 由于有且只有一个信号源，所以找到信号源后直接退出循环
            break

# 注意，本题可以直接在grid数组上进行修改，故无需设置checkList检查数组
# 另外，搜索层数可以根据intensity递减
while q :
    # 本次搜索，强度-1
    intensity -= 1
    # 如果强度降为0，无需进行搜索，直接退出循环
    if intensity == 0:
        break
    tmp = q
    q = []
    for x, y in tmp:
        
        # 遍历点(x, y)的近邻点
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            # (nx, ny)需要满足：
            # 1. 不越界
            # 2. 在grid中为0
            if (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0):
                # 直接将grid[nx][ny]修改为强度intensity
                # 这一步替代了checkList
                grid[nx][ny] = intensity
                # 并且将点(nx, ny)加入队列中继续进行搜索
                q.append((nx, ny))


# 最后输出grid中点(target_x, target_y)的值即可
print(grid[target_x][target_y])