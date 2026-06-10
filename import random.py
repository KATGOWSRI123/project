import random 
x = input("odd  or even   :")
x1= int(input("enter a number  :"))

y=random.randint(0,10)
print("bot enter number is " ,y)
z=x1+y
if z %2 ==0 and x=="even":
    print ("the number is ",z ,"u won the toss")
    a=input("batting or bowling  :")
    if a=="batting":
        print("u chose batting and bot is bowling")
        i=0
        while True:
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
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
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",q)
                    if q>i:
                        a1=q-i
                        print ("bot won by ",a1)
                        break
                    else:
                        a1=i-q
                        print("u won by ",a1)

                        break
                if q>i:
                    a1=q-i
                    print ("bot won by ",a1)
                else:
                    q+=y
            else:
                print("out of range")
    if a== "bowling":
        print("now bot is batting")
        i=0
        while True:
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
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
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",q)
                    if q>i:
                        a1=q-i
                        print ("you won by ",a1)
                        break
                    else:
                        a1=i-q
                        print("bot won by ",a1)

                        break
                if q>i:
                    a1=q-i
                    print ("you won by ",a1)
                else:
                    q+=x
            else:
                print("out of range")


            
elif z%2 ==1 and x=="odd":
    print ("the number is ",z," u won the toss")
    a= input("batting or bowling   :")
    if a=="batting":
        print("u chose batting and bot is bowling")
        i=0
        while True:
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
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
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",q)
                    if q>i:
                        a1=q-i
                        print ("bot won by ",a1)
                        break
                    else:
                        a1=i-q
                        print("u won by ",a1)

                        break
                if q>i:
                    a1=q-i
                    print ("bot won by ",a1)
                else:
                    q+=y
            else:
                print("out of range")  
    if a== "bowling":
        print("now bot is batting")
        i=0
        while True:
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
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
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",q)
                    if q>i:
                        a1=q-i
                        print ("you won by ",a1)
                        break
                    else:
                        a1=i-q
                        print("bot won by ",a1)

                        break
                if q>i:
                    a1=q-i
                    print ("you won by ",a1)
                else:
                    q+=x
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
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
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
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",q)
                    if q>i:
                        a1=q-i
                        print ("you won by ",a1)
                        break
                    else:
                        a1=i-q
                        print("bot won by ",a1)

                        break
                if q>i:
                    a1=q-i
                    print ("you won by ",a1)
                else:
                    q+=x
            else:
                print("out of range")
    if a== "bowling":
        print("u chose bowling and bot is batting")
        i=0
        while True:
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
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
            x=int(input("enter a number (0 to 10)   :"))
            y=random.randint(0,10)
            print(y)
            if x<=10:
                if x==y:
                    print ("out")
                    print("total score is ",q)
                    if q>i:
                        a1=q-i
                        print ("you won by ",a1)
                        break
                    else:
                        a1=i-q
                        print("bot won by ",a1)

                        break
                if q>i:
                    a1=q-i
                    print ("you won by ",a1)
                else:
                    q+=x
            else:
                print("out of range")