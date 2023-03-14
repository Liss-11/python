kata = (0, 4, 132.42222, 10000, 12345.67)

if len(kata) != 5:
    print("THe number of parameters must be five")
if (isinstance(kata[0], int) and kata[0] >= 0 and len(str(kata[0])) < 3) and (isinstance(kata[1], int) and kata[1] >= 0 and len(str(kata[0])) < 3) and isinstance(kata[2], float) and isinstance(kata[3], int) and isinstance(kata[4], float):
    print(f"module_{kata[0]:02d}, ex_{kata[1]:02d} : {'{:.2f}'.format(kata[2])}, {'{:.2e}'.format(kata[3])}, {'{:.2e}'.format(kata[4])}")
else:
    print("incorrect input")