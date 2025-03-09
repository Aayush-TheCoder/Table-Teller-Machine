print("\nWELCOME in the 'table teller' machine!\n\t\t\t\t-by Aayush Kumar")

while True:
    num = int(input("\nYahan pe wo number dalo jiska aapko table chahiye : "))
    res = 1
    for i in range(1,11):
        res = num * i
        print("\n\t\t", num, "X", i, "=", res)

    print("\n")
    
    continuity = input("Want to continue? (yes: y, no: n)): ")
    
    match continuity:
        case "y": continue
        case "n": print("Thanks for using this calculator. Have a good day!\n"); input(); break
