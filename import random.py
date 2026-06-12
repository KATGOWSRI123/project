import random 
while True:
    x = input("odd or even: ").lower()
    if x in ["odd", "even"]:
        break
    print("Enter only odd or even")
while True:
    try:
        x1 = int(input("enter a number (0-10): "))
        if 0 <= x1 <= 10:
            break
        print("Enter a number between 0 and 10")
    except ValueError:
        print("Enter a valid number")

y=random.randint(0,10)
print("bot enter number is " ,y)
z=x1+y
if (z %2 ==0 and x=="even") or (z%2 ==1 and x=="odd"):
    print ("the number is ",z ,"u won the toss")
    while True:
        a = input("batting or bowling: ").lower()
        if a in ["batting", "bowling"]:
            break
        print("Enter batting or bowling only")
    if a=="batting":
        print("u chose batting and bot is bowling")
        i=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",i)

                    break
                else:
                    i+=x
            else:
                print("out of range")
        print("now bot is battting")
        q=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x == y:
                    print("OUT")
                    print("Total score is", q)

                    if q > i:
                        print("Bot won by", q - i)
                    elif q < i:
                        print("You won by", i - q)
                    else:
                        print("Match tied")

                    break
                else:
                    q += y

                if q > i:
                    print("Bot won by", q - i)
                    break

            else:
                print("out of range")
    elif a== "bowling":
        print("now bot is batting")
        i=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",i)

                    break
                else:
                    i+=y
            else:
                print("out of range")
        print("now bot is bowling")
        q=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x == y:
                    print("OUT")
                    print("Total score is", q)

                    if q > i:
                        print("You won by", q - i)
                    elif q < i:
                        print("Bot won by", i - q)
                    else:
                        print("Match tied")

                    break
                else:
                    q += x

                if q > i:
                    print("You won by", q - i)
                    break
            else:
                print("out of range")
            
else :
    print("the number is ",z,"u loss the toss")
    a=random.choice(["batting","bowling"])
    print("bot choose ",a)
    if a=="batting":
        print("now bot is batting")
        i=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",i)

                    break
                else:
                    i+=y
            else:
                print("out of range")
        print("now bot is bowling")
        q=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x == y:
                    print("OUT")
                    print("Total score is", q)

                    if q > i:
                        print("You won by", q - i)
                    elif q < i:
                        print("Bot won by", i - q)
                    else:
                        print("Match tied")

                    break
                else:
                    q += x

                if q > i:
                    print("You won by", q - i)
                    break
            else:
                print("out of range")
    elif a== "bowling":
        print("u chose bowling and bot is batting")
        i=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",i)

                    break
                else:
                    i+=y
            else:
                print("out of range")
        print("now bot is bowling")
        q=0
        while True:
            try:
                x = int(input("enter a number (0 to 10): "))
            except ValueError:
                print("Enter a valid number")
                continue
            y=random.randint(0,10)
            print(y)
            if 0<=x<=10:
                if x == y:
                    print("OUT")
                    print("Total score is", q)

                    if q > i:
                        print("Bot won by", q - i)
                    elif q < i:
                        print("You won by", i - q)
                    else:
                        print("Match tied")

                    break
                else:
                    q += x

                if q > i:
                    print("Bot won by", q - i)
                    break
            else:
                print("out of range")
