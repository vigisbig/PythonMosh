numbers = [5,2,5,2,2]

for i in numbers:
    output = ''
    for y in range(i):
        output += '*'
    print(output)

print("########## alternative way #############")

for i in numbers:
    print(i * "*")

print("############### alternative way ###############")

L = [5,2,5,2,2]
for i in L:
    for j in range(i):
        print('*', end='')
    print()