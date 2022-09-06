def emoji_converter(message):
    words = message.split(' ')
    output = ""
    emoji_lib = {":-)":"😊",":-(":"😢"} 

    for word in words:
        output += emoji_lib.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))