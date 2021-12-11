from scipy import ndimage
import numpy as np

with open('input','r') as f:
	lines=f.read().split('\n')
	lines.pop()

dl = len(lines[0])

tmp=[]
for l in lines:
	a=[]
	for i in l:
		a.append(int(i))
	tmp.append(a)
lines=tmp
print(lines)

dt = np.array(lines)
dt.reshape(-1, dl)

label, num_label = ndimage.label(dt < 9)
size = np.bincount(label.ravel())

top3 = sorted(size[1:], reverse=True)[:3]
print(top3)
print(np.prod(top3))

