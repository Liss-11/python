kata = "The right format"

if len(kata) > 42:
    print("String must not contain more than 42 characters!")
    exit(1)
length = 42 - len(kata)
while(length > 0):
    print("-", end="")
    length -= 1
print(kata, end="")