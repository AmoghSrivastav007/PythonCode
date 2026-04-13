row = int(input("Enter the row size for the pattern:"))

for i in range(1, row+1):       #Outer loop for rows
    for j in range(row-i):      #Inner loop for spaces
        print(" ", end =" ")
    for k in range(1,2*i):      #Inner loop for stars
        print("*", end=" ")
    print()