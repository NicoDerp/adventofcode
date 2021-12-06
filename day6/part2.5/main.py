from collections import deque

with open('input','r') as f:
	fishList=list(map(lambda i:int(i),f.read().split(',')))

#fishList=[3,4,3,1,2]


fish = []
for i in range(9):
	fish.append(fishList.count(i))

fish = deque(fish)
print(fish)

#print('Initial state: ',fish)
for day in range(256):
	fish.rotate(-1)
	fish[6]+=fish[8]
	#print(fish)
	#print("After {} day: {}".format(day,fish))

print(fish)
print(sum(fish))
