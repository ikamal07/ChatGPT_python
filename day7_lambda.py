square = lambda x:x**2
print(square(3))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = list(filter(lambda x: x%2!=0 , numbers))
print(odd)

names = ["Alice", "Bob", "Charlie", "David"]

list2 = list(sorted(names, key = lambda x:len(x)))
print(list2)

add= lambda x,y:x+y
print(add(5,3))

words = ["hello", "world", "python", "lambda"]
reversed_words = list(map(lambda x:x[::-1], words))
print(reversed_words)