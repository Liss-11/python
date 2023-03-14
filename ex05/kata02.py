kata = (2019, 9, 25, 3, 30)

if len(kata) != 5:
    print("Incorrect format, only 5 numbers are permitted")
    exit(1)

if kata[1] < 0 or len(str(kata[1]))>4:
    print("First param must be less than 10000")
    exit(1)
for num in kata[1:]:
    if num < 0 or len(str(num)) > 2:
        print("Nums must be less than 100")
        exit(1)

print("0" + str(kata[1]), end="/") if kata[1] < 10 else print(str(kata[1]), end="/")
print("0" + str(kata[2]), end="/") if kata[2] < 10 else print(str(kata[2]), end="/")
print(str(kata[0]), end=" ")
print("0" + str(kata[3]), end=":") if kata[3] < 10 else print(str(kata[3]), end=":")
print("0" + str(kata[4])) if kata[4] < 10 else print(str(kata[4]))