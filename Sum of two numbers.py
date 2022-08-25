first_number = input("Enter first number - ")#variable first_number format for saving value of the string.
second_number = input("Enter second number - ") #input used for prompt, saves value as string
answer = float(first_number) + float(second_number) # since input can take only string, we convert to integers or float first 
answer_string = str (answer) # answer converted to string since concatenate below works with similar data only. Alternatively, you can use in print too directly.


print("Your answer is" + str (answer))
print(answer_string+second_number)
print("Your number is "+ answer_string)
print("Your number is "+ answer) # does not work since it's trying to concatenate string with float type

# basically we have the following data types 

#1. int
#2. float
#3. bool
#4. str

# Python is case-sensitive, True is not the same as true. So tread carefully. Below is another way to solve this

first_number = float(input("Enter first number- "))
second_number = float(input("Enter second number- "))
sum = (first_number+second_number)

print("Your number is " + str(sum))
