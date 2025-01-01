list1 = [5,4,32,45,22]
k=0
for i in list1:
	k=k+i
avg = k/5
print(avg)
for j in list1:
	if j > avg:
		print(j)
