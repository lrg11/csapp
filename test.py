while True:
	n, k = map(int,input().split())
	if n == -1 or k == -1:
		break
	free = []
	for _ in range(n):
		line = input()
		freecol = [0] * n
		for i in range(n):
			if line[i] == '#':
				freecol[i] = 1
		free.append(freecol)

	def isValid(tack, row, col):
 		for i in range(row):
 			if tack[i][col] == 1:
 				return False

 		return True

	ans = 0

	def dfs(i, k, tack):
		if k == 0 and i <= n:
			global ans
			ans = ans + 1
			#print(i, k)
			return 
		if i >= n :
			return 
		for j in range(n):
			if free[i][j] == 0 or not isValid(tack, i, j):
				continue
			tack[i][j] = 1
			dfs(i+ 1, k -1, tack)
			tack[i][j] = 0
			#if n - i >= k:
		dfs(i + 1, k, tack)


			
	tack = [[0]*n for _ in range(n)]
	dfs(0, k, tack)

	print(ans)