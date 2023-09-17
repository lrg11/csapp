# IO
#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。


import sys
if __name__ == "__main__":
    # 读取第一行的n
    linx = input()
    n = int((linx.strip().split())[0])
    k = int((linx.strip().split())[1])
    ans = 0
    
    # 读取每一行
    line = input()
    # 或者 line = sys.stdin.readline()
 
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.strip().split()))
        
    #values.sort()
    def check(i: int) -> bool:
    	cnt = 1
    	pre = 0
    	j = 1
    	while j < len(values):
    		if values[j] - values[pre] >= i:
    			pre = j
    			j += 1
    			cnt += 1
    			if cnt >= k:
    				return True
    		else:
    			j += 1

    	return False

    if k == 2:
    	print(values[-1] - values[0])

    else:
    

	    right = values[-1] - values[0] + 1

	    left = 0

	    while left + 1 < right:
	    	mid = (left +right) // 2
	    	print("right: ", right)
	    	print("left:", left)
	    	if check(mid):
	    		left = mid
	    	else:
	    		right = mid
	    print(left)

