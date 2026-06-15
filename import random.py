import random
import mysql.connector as my

# Connect to the database
db = my.connect(
    host="localhost",
    user="root",
    password="1234",
    database="game"
)
cursor = db.cursor()
print("welcome to hand cricket game")
print("\n========== HAND CRICKET RULES ==========")
print("1. Choose Odd or Even for the toss.")
print("2. Enter numbers only between 0 and 10.")
print("3. If the batting player's number matches the bowling player's number, the batter is OUT.")
print("4. If the numbers do not match, runs are scored.")
print("5. If you enter a number outside 0-10 while batting, 5 runs will be deducted from your score.")
print("6. If you enter a number outside 0-10 while bowling, 5 bonus runs will be awarded to the bot.")
print("7. Scores cannot go below 0 after a penalty.")
print("8. The team with the higher score wins.")
print("========================================\n")
c=input("do you want to play the game (yes or no): ").lower()
if c=="yes":
    v=input("enter your name: ")
    print("welcome ",v)
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
            player_score=0
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
                        print("total score is ",player_score)

                        break
                    else:
                        player_score +=x
                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score= max(0, player_score-5)
            print("now bot is battting and u are bowling")
            bot_score=0
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
                        print("Total score is", bot_score)

                        if bot_score > player_score:
                            print("Bot won by", bot_score - player_score)
                        elif bot_score < player_score:
                            print("You won by", player_score - bot_score)
                        else:
                            print("Match tied")

                        break
                    else:
                        bot_score += y

                    if bot_score > player_score:
                        print("Bot won by", bot_score - player_score)
                        break

                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score+=5

        elif a== "bowling":
            print("now bot is batting and u are bowling")
            bot_score=0
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
                        print("total score is ",bot_score)

                        break
                    else:
                        bot_score += y
                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score+=5
            print("now bot is bowling and u are batting")
            player_score=0
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
                        print("Total score is", player_score)

                        if player_score > bot_score:
                            print("You won by", player_score - bot_score)
                        elif player_score < bot_score:
                            print("Bot won by", bot_score - player_score)
                        else:
                            print("Match tied")

                        break
                    else:
                        player_score += x

                    if player_score > bot_score:
                        print("You won by", player_score - bot_score)
                        break
                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score = max(0, player_score-5)

    else :
        print("the number is ",z,"u lost the toss")
        a=random.choice(["batting","bowling"])
        print("bot choose ",a)
        if a=="batting":
            print("now bot is batting and u are bowling")
            bot_score=0
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
                        print("total score is ",bot_score)

                        break
                    else:
                        bot_score += y
                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score += 5
            print("now bot is bowling and u are batting")
            player_score=0
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
                        print("Total score is", player_score)

                        if player_score > bot_score:
                            print("You won by", player_score - bot_score)
                        elif player_score < bot_score:
                            print("Bot won by", bot_score - player_score)
                        else:
                            print("Match tied")

                        break
                    else:
                        player_score += x

                    if player_score > bot_score:
                        print("You won by", player_score - bot_score)
                        break
                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score = max(0, player_score-5)
        elif a== "bowling":
            print("bot chose bowling and you are batting")
            player_score=0
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
                        print("total score is ",player_score)

                        break
                    else:
                        player_score += x
                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score = max(0, player_score-5)
            print("now bot is batting and you are bowling")
            bot_score=0
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
                        print("Total score is", bot_score)

                        if bot_score > player_score:
                            print("Bot won by", bot_score - player_score)
                        elif bot_score < player_score:
                            print("You won by", player_score - bot_score)
                        else:
                            print("Match tied")

                        break
                    else:
                        bot_score += y

                    if bot_score > player_score:
                        print("Bot won by", bot_score - player_score)
                        break
                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score += 5

elif c=="no":
    v=input("do you want to see the players list (yes or no): ").lower()
    if v=="yes":
        cursor.execute("SELECT * FROM score")
        players = cursor.fetchall()
        for player in players:
            print(player)
