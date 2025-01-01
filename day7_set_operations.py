s1 = set()
s2 = set()
for i in range(0,20,2):
    s1.add(i)


for j in range(3,20,3):
    s2.add(j)




union_set = s1.union(s2)
intersection_set = s1.intersection(s2)
difference_set = s1.difference(s2)

print("Union of 2 sets ", union_set)
print("Intesection of 2 sets ", intersection_set )
print("Differece in 2 sets ", difference_set)