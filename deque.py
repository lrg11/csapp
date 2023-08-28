# 2810
class Solution:
    def finalString(self, s: str) -> str:
    	direction = True
    	q = deque()
    	for c in s:
    		if c != 'i' and direction:
    			q.append(c)
    		elif c != 'i' and not direction:
    			q.appendleft(c)
    		elif c == 'i':
    			direction = not direction
    	if not direction:
    		return ''.join(reversed(q))
    	return ''.join(q)
