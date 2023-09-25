n = int(input())

nums = list(map(int, input().split()))

sn = int(input())

if nums.count(sn) == 1:
	print(nums.index(sn), nums.index(sn))
else:
	start = nums.index(sn)
	end = nums.count(sn) + start - 1
	if start == 0 and nums[-1] == sn:
		for i, x in enumerate(nums):
			if x != sn:
				end = i - 1
				break
		for i in range(n - 2, -1, -1):
			if nums[i] != sn:
				start = i + 1
				break


	print(start, end)