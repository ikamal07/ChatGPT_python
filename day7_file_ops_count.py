with open("data.txt", "r") as file:
    content = file.read()


wordcount = content.split()


my_dict = {i:wordcount.count(i) for i in wordcount}
print(my_dict)