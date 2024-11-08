# a fun exercise
s=""
a=['t', 'a', 'c', '1', 'q', 'd', 'e']
for i in range(4):
	# this part checks modulus operand on i with 2 and 3 together
	if(i%2==0 and i%3==0):
		s += a[i]
	# here only odd values of i will be considered
	if(i%2 ==1):
		s += a[(-abs(i-2)) **1]
	# in this part, block is executed when i is 2
	if(i==2):
		s += a[int((len(a)-1)/2)]

# finally when for loop ends, this revers indexing appends the value to s
s += a[-3]
print(s)
