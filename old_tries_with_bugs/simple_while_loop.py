a = True
b = -2

while a:
    print("in while")
    if b < 0:
        print(" in if", b)
        b = b + 1
        print(" in if", b)
    else:
        print("in else")
        #a = False
        break