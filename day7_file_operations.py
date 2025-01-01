with open("data.txt", "r") as file:
    content = file.read()
print(content)

wordcount = len(content.split())
print("Total number of words", wordcount)

linecount = len(content.split("\n"))
print("Total number of lines", linecount)

char_count = len(content.replace("\n",""))
print("Total Number of Char's: ",char_count)
j=0

for i in content:
    if i != '\n':
        j=j+1
    
print("Total number of characters", j)
