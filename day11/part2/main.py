from itertools import product

with open('input','r') as f:
	nums=f.read().split('\n')
	nums.pop()
	nums=list(map(lambda i:list(i),nums))

nums=[list(map(lambda i:int(i),l)) for l in nums]

def neighbours(cell,size):
	for c in product(*(range(n-1, n+2) for n in cell)):
		if c != cell and all(0 <= n < size for n in c):
			yield c

def printList(l):
	for i in nums:
		for j in i:
			print(0 if j==0 else '.', end=' ')
		print(end='    ')
		for j in i:
			print(j,end=' ')
		print()

for step in range(1000):
	c=0
	for i in range(len(nums)):
		for j in range(len(nums[i])):
			nums[i][j]+=1

	while True:
		changed=0
		for i in range(len(nums)):
			for j in range(len(nums)):
				if nums[i][j]>9:
					nums[i][j]=-100
					changed+=1
					for n in neighbours((i,j),len(nums)):
						#if nums[n[0]][n[1]]<=9:
						nums[n[0]][n[1]]+=1
		#printList(nums)
		#print()
		if changed==0:
			break

	for i in range(len(nums)):
		for j in range(len(nums[i])):
			if nums[i][j]<0:
				nums[i][j]=0
				c+=1

	print("\nAfter step {}:".format(step))
	printList(nums)
	#print(c)

	if c==len(nums)**2:
		print(step+1)
		break


