f=open('input', 'r')
l=int(f.readline().strip())
c=0
for line in f:
	if (i := int(line))>l:c+=1
	l=i
f.close()
print(c)
