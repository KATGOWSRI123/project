import random
import mysql.connector as my
import requests
import time

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



def get_random_number():
    url = "https://www.random.org/integers/?num=1&min=0&max=10&col=1&base=10&format=plain&rnd=new"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return int(response.text.strip())
    except (requests.RequestException, ValueError):
        print("API failed. Using local random number.")
        return random.randint(0, 10)

c=input("do you want to play the game (yes or no): ").lower()
if c=="yes":
    v=input("enter your name: ")
    print("welcome ",v)
    print("=" * 60)
    print("TOSS TIME")
    print("=" * 60)
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

    y=get_random_number()
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
            print("=" * 60)
            print("\n")
            player_score=0
            number_of_balls=0
            bot_score=0
            number_of_balls_bot=0
            player_score_total=0
            bot_score_total=0
            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x==y:
                        print ("out")
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        break
                    else:
                        player_score +=x
                        number_of_balls += 1
                        player_score_total +=x
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")
                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score_total= max(0, player_score-5)
            print("=" * 60)
            print("now bot is battting and u are bowling")
            print("=" * 60)

            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x == y:
                        print("OUT")
                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        if bot_score_total > player_score_total:
                            print("Bot won by", bot_score_total - player_score_total)
                        elif bot_score_total < player_score_total:
                            print("You won by", player_score_total - bot_score_total)
                        else:
                            print("Match tied")

                        break
                    else:
                        bot_score += y
                        number_of_balls_bot += 1
                        bot_score_total += y
                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                    if bot_score_total > player_score_total:
                        print("Bot won by", bot_score_total - player_score_total)
                        break

                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score_total = bot_score + 5

        elif a== "bowling":
            print("=" * 60)
            print("now bot is batting and u are bowling")
            print("=" * 60)
            bot_score=0
            number_of_balls_bot=0
            player_score=0
            number_of_balls=0
            player_score_total=0
            bot_score_total=0
            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x==y:
                        print ("out")
                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        break
                    else:
                        bot_score += y
                        number_of_balls_bot += 1
                        bot_score_total += y
                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")
                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score_total = bot_score + 5
            print("=" * 60)
            print("now bot is bowling and u are batting")
            print("=" * 60)

            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x == y:
                        print("OUT")
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        if player_score_total > bot_score_total:
                            print("You won by", player_score_total - bot_score_total)
                        elif player_score_total < bot_score_total:
                            print("Bot won by", bot_score_total - player_score_total)
                        else:
                            print("Match tied")

                        break
                    else:
                        player_score += x
                        number_of_balls += 1
                        player_score_total += x
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                    if player_score_total > bot_score_total:
                        print("You won by", player_score_total - bot_score_total)
                        break
                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score_total = max(0, player_score-5)

    else :
        print("=" * 60)
        print("the number is ",z,"u lost the toss")
        print
        a=random.choice(["batting","bowling"])
        print("bot choose ",a)
        if a=="batting":
            print("now bot is batting and u are bowling")
            print("-" * 60)
            bot_score=0
            number_of_balls_bot=0
            player_score=0
            number_of_balls=0
            player_score_total=0
            bot_score_total=0
            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x==y:
                        print ("out")
                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        break
                    else:
                        bot_score += y
                        bot_score_total += y
                        number_of_balls_bot += 1

                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")
                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score_total = bot_score + 5

            print("=" * 60)
            print("now bot is bowling and u are batting")
            print("=" * 60)
            
            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x == y:
                        print("OUT")
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        if player_score_total > bot_score_total:
                            print("You won by", player_score_total - bot_score_total)
                        elif player_score_total < bot_score_total:
                            print("Bot won by", bot_score_total - player_score_total)
                        else:
                            print("Match tied")

                        break
                    else:
                        player_score += x
                        number_of_balls += 1
                        player_score_total += x
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                    if player_score_total > bot_score_total:
                        print("You won by", player_score_total - bot_score_total)
                        break
                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score_total = max(0, player_score-5)
        elif a== "bowling":
            print("bot chose bowling and you are batting")
            player_score=0
            number_of_balls=0
            bot_score=0
            number_of_balls_bot=0
            player_score_total=0
            bot_score_total=0
            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x==y:
                        print ("out")
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        break
                    else:
                        player_score += x
                        number_of_balls += 1
                        player_score_total += x
                        print(f"{v}   {player_score} ({number_of_balls})    {player_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                else:
                    print("out of range")
                    print(f"penalty of -5 points for out of range input")
                    player_score_total = max(0, player_score-5)

            print("=" * 60)
            print("now bot is batting and you are bowling")
            print("=" * 60)
            
            while True:
                try:
                    x = int(input("enter a number (0 to 10): "))
                except ValueError:
                    print("Enter a valid number")
                    continue
                y=get_random_number()
                print(y)
                if 0<=x<=10:
                    if x == y:
                        print("OUT")
                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-1")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                        if bot_score_total > player_score_total:
                            print("Bot won by", bot_score_total - player_score_total)
                        elif bot_score_total < player_score_total:
                            print("You won by", player_score_total - bot_score_total )
                        else:
                            print("Match tied")

                        break
                    else:
                        bot_score += y
                        bot_score_total += y
                        number_of_balls_bot += 1
                        print(f"{v}   {player_score} ({number_of_balls})    {bot_score_total}-0")
                        print(f"bot   {bot_score} ({number_of_balls_bot})")

                    if bot_score_total > player_score_total:
                        print("Bot won by", bot_score_total - player_score_total)
                        break
                else:
                    print("out of range")
                    print(f"penalty of +5 runs to bot score for out of range input")
                    bot_score_total = bot_score + 5

elif c=="no":
    v=input("do you want to see the players list (yes or no): ").lower()
    if v=="yes":
        cursor.execute("SELECT * FROM score")
        players = cursor.fetchall()
        for player in players:
            print(player)
