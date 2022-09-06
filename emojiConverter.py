message = input("> ")
words = message.split(' ')
output = ""
emoji_lib = {":-)":"😊",":-(":"😢"} 

for word in words:
    output += emoji_lib.get(word, word) + " "

print(output)