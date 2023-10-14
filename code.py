
# 1
def hasCycle(head:Optional[ListNode]) -> int:
	slow = head
	fast = head
	while fast:
		if fast.next:
			fast = fast.next.next
		slow = slow.next
		if slow == fast:
			return 1
	return 0


# 2

n, k = map(int,input().split())

while n != -1 or k != -1:
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
 				return false

 		return true

 	ans = 0
	def dfs(i, k, tack):
		if k == 0:
			ans += 1
		if i > n and k > 0:
			return 
		for j in range(n):
			if not isValid(tack, i, j) and free[i][j] == 1:
				continue
			tack[i][j] = 1
			dfs(i+ 1, k -1)
			tack[i][j] = 0
			dfs(i + 1, k)

			
	tack = [[0] for _ in range(n)]

	print(dfs(0, k, tack))
