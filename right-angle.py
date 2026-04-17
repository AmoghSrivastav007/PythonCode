row = int(input("Enter the row size for the pattern :"))

for i in range(1, row+1):       #outer loop for rows
    for j in range(1, i+1):     # Inner loop for columns
        print("*", end ="")     #print star
    print()