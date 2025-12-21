x = int(input("enter a number: "))

if x %20 == 0:
    print("twist")
    pass
elif x%15 ==0:
    pass
elif x%5 ==0:
    print("fizz")
    pass
elif x% 3 ==0:
    print("buzz")
    pass
else:
    print(x)