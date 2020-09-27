def main():
	
	num1 = 0
	num2 = 0
	
	question = True
	while question:
		calc = input("Would you like to add, sub, mul, or div?\n")
		list_of_calcs = ["add","sub","mul","div"]
		
		for i in list_of_calcs:
			if(i == calc):
				question = False
		
		if question:
			print("That is not a valid option.\n")
	

	while True:
		try:
			num1 = float(input("First number "))
			break
		except ValueError:
			print("Oops! That is not a valid number")

	while True:
		try:
			num2 = float(input("Second number "))
			break
		except ValueError:
			print("Oops! That is not a valid number")

	def cal(num1, num2, operation):
		if operation == "add":
			return num1 + num2
		if operation == "sub":
			return num1 - num2
		if operation == "mul":
			return num1 * num2
		if operation == "div":
			return num1 / num2
		
	result = cal(num1,num2,calc)
	print(result)

main()
