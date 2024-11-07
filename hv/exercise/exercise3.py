s=""
a=['t', 'a', 'c', '1', 'q', 'd', 'e']
for i in range(4):
	if(i%2==0 and i%3==0):
		s += a[i]
	if(i%2 ==1):
		s += a[(-abs(i-2)) **1]
		print((-abs(i-2)) **1)
	if(i==2):
		s += a[int((len(a)-1)/2)]
s += a[-3]
print(s)
