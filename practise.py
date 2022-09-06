def emoj_bulao(message):
    words = message.split(' ')
    output = ""
    emoji_dict = {
        ":-)":"😊",":-(":"😢"
    }
    for word in words:
        output += emoji_dict.get(word,word) + ' '
    return output


message = input("> ")
print(emoj_bulao(message))