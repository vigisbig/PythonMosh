first_number = input ("Enter first number - ")
second_number = input ("Enter second number - ")
answer = float(first_number) + float(second_number) # since input can take only string, we convert to integers first 
answer_string = str (answer) # answer converted to string
print("The answer is " + answer_string)
