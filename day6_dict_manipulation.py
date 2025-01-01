dict1 = { "Name" : "Arjun", "Age" : 16, "Class" : "10th", "Subjects" : ["Math", "Science", "History"]}
dict1["Hobby"] = "Chess"
dict1['Class'] = "11th"
for i in dict1.keys():
    print(f" {i} is" ,dict1[i])
