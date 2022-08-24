first_number = input ("Enter first number - ")
second_number = input ("Enter second number - ") #input used for prompt, saves value as string
answer = float(first_number) + float(second_number) # since input can take only string, we convert to integers first 
answer_string = str (answer) # answer converted to string
print("The answer is " + answer_string)

# basically we have the following data types 

#1. int
#2. float
#3. bool
#4. str

# Python is case sensitive, True is not the same as true. So tread carefully.