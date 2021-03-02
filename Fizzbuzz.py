for x in range(1, 100):
    if x % 2 == 0:
        print("fizz")
    if x % 3 == 0:
        print("buzz")
    if x % 2 == 0 and x % 3 == 0:
        print("fizzbuzz")
    else:
        print(x)
