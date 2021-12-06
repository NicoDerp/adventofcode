with open('input','r') as f:
	fish=list(map(lambda i:int(i),f.read().split(',')))

#fish=[3,4,3,1,2]

#print('Initial state: ',fish)
for day in range(256):
	for i in range(len(fish)):
		fish[i]-=1
		if fish[i]==-1:fish[i]=6;fish.append(8)
	#print("After {} day: {}".format(day,fish))

print(len(fish))
