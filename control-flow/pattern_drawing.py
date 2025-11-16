size = int(input("Enter the size of the pattern: "))

pattern = 0
while pattern != size:
    for i in range(size):
        print("*", end="")
    print("\n")
    pattern += 1
    
