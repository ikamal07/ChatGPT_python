text = "hello world hello python"
list1=[]
dict2 = {}
for i in text.split(" "):
    list1.append(i)
    
for j in list1:
    count=list1.count(j)
    dict2[j] = count


print(dict2)