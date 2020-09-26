def main():
	true = True
	while true:
		calc = input("Would you like to add, sub, mul, or div?\n")
		list_of_calcs = ["add","sub","mul","div"]
		
		for i in list_of_calcs:
			if(i == calc):
				true = False
		if true:
			print("That is not a valid option.\n")
			
	num1 = float(input("First number "))
	num2 = float(input("Second number "))
	
	def cal(operation,number1,number2):
		if operation == "add":
			return number1+number2
		if operation == "sub":
			return number1-number2
		if operation == "mul":
			return number1*number2
		if operation == "div":
			return number1/number2
		
	result = cal(calc,num1,num2)
	print(result)

main()
