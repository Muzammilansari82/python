b = input('Enter language html or php:')

if b == "html":
    a = 0
    i = []
    length = int(input("Input your length:"))

    while a < length:
        a = a + 1
        j = input("Enter your question:")
        i.append(j)
    
    print("HTML questions:")
    print(i)

elif b == "php":
    a = 0
    ii = []
    length = int(input("Input your length:"))

    while a < length:
        a = a + 1
        j = input("Enter your question:")
        ii.append(j)
    
    print("PHP questions:")
    print(ii)

else:
    print("Invalid input. Please enter 'html' or 'php'.")
