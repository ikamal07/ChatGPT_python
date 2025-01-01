num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
oper = input("Enter the operation you want to perform +,-,*,/ : ")

if oper == "+":
	res = num1+num2
elif oper == "-":
	res = num1-num2
elif oper == "*":
	res = num1*num2
elif oper == "/" and num2!=0:
	res = num1/num2
else:
	res = "Error, Invalid Operation or Division by Zero"

print("The result is :", res)

