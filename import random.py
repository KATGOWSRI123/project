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

print("\n====================== HAND CRICKET GAME ===========================")
print("____________")
print("|1. Login  |")
print("|2. Signup |")
print("____________")
while True:
    choice = input("Enter your choice: ").lower()
    if choice == "signup" or choice == "2":
        user = input("Choose a username: ")
        password = input("Choose a password: ")

        cursor.execute("SELECT * FROM users WHERE username=%s", (user,))
        result = cursor.fetchone()

        if result:
            print("Username already exists.")
            exit()

        cursor.execute(
            "INSERT INTO users(username,password) VALUES(%s,%s)",
            (user, password)
        )
        db.commit()

        print("Account created successfully!")
        break

    elif choice == "login" or choice == "1":
        user = input("Username: ")
        password = input("Password: ")

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (user, password)
        )

        result = cursor.fetchone()

        if result:
            print("Login Successful!")
            break
        else:
            print("Invalid Username or Password")
            exit()
    else:
        print("Invalid choice.")
        cursor.close()
        db.close()
        exit()

print(f"Welcome {user} to the Hand Cricket Game!")

a2=input("Do you want to see your stats? (yes/no): ").lower()
while a2 not in ["yes", "no"]:
    print("Please enter 'yes' or 'no'.")
    a2=input("Do you want to see your stats? (yes/no): ").lower()
while True:
    if a2=="yes":
        cursor.execute("""
        SELECT matches, wins, losses, highest_score, total_runs
        FROM users
        WHERE username=%s
        """, (user,))

        stats = cursor.fetchone()

        print("\n========== PLAYER STATS ==========")
        print("Matches Played :", stats[0])
        print("Wins           :", stats[1])
        print("Losses         :", stats[2])
        print("Highest Score  :", stats[3])
        print("Total Runs     :", stats[4])
        print("==================================")
        time.sleep(7)
        break

    elif a2=="no":
        print("Let's start the game!")
        break
    else:
        print("Please enter 'yes' or 'no'.")


def get_random_number():
    url = "https://www.random.org/integers/?num=1&min=0&max=10&col=1&base=10&format=plain&rnd=new"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return int(response.text.strip())
    except (requests.RequestException, ValueError):
        print("API failed. Using local random number.")
        return random.randint(0, 10)


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
time.sleep(5)

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
        else:
            print("Enter a number between 0 and 10")
    except ValueError:
        print("Enter a valid number")

y=get_random_number()
print("Bot entered number is " ,y)
time.sleep(3)
z=x1+y
if (z %2 ==0 and x=="even") or (z%2 ==1 and x=="odd"):
    time.sleep(3)
    print ("the number is ",z ,"u won the toss")
    while True:
        a = input("batting or bowling: ").lower()
        if a in ["batting", "bowling"]:
            break
        else:
         print("Enter batting or bowling only")
    if a=="batting":
        time.sleep(3)
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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x==y:
                    time.sleep(3)
                    print ("out")
                    time.sleep(3)
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-1      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")
                    break
                else:
                    player_score +=x
                    number_of_balls += 1
                    player_score_total +=x
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")
            else:
                print("out of range")
                print(f"penalty of -5 points for out of range input")
                player_score_total= max(0, player_score-5)
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                print("|                                                                            |")
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")

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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x == y:
                    time.sleep(3)
                    print("OUT")
                    print("=============================================================================")
                    print("|                                                                            |")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-1      |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                    if bot_score_total > player_score_total:
                        print("Bot won by", bot_score_total - player_score_total)
                        result = "Bot won"
                    elif bot_score_total < player_score_total:
                        print("You won by", player_score_total - bot_score_total)
                        result = "You won"
                    else:
                        print("Match tied")
                        result = "Match tied"

                    break
                else:
                    bot_score += y
                    number_of_balls_bot += 1
                    bot_score_total += y
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                if bot_score_total > player_score_total:
                    print("Bot won by", bot_score_total - player_score_total)
                    break

            else:
                print("out of range")
                time.sleep(3)
                print(f"penalty of +5 runs to bot score for out of range input")
                bot_score_total = bot_score + 5
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                print("|                                                                            |")
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")  

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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x==y:
                    print ("out")
                    time.sleep(3)
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-1         |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                    break
                else:
                    bot_score += y
                    number_of_balls_bot += 1
                    bot_score_total += y
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")
            else:
                print("out of range")
                time.sleep(3)
                print(f"penalty of +5 runs to bot score for out of range input")
                bot_score_total = bot_score + 5
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                print("|                                                                            |") 
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")

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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x == y:
                    print("OUT")
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-1      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                    if player_score_total > bot_score_total:
                        print("You won by", player_score_total - bot_score_total)
                        result = "You won"
                    elif player_score_total < bot_score_total:
                        print("Bot won by", bot_score_total - player_score_total)
                        result = "Bot won"
                    else:
                        print("Match tied")
                        result = "Match tied"

                    break
                else:
                    player_score += x
                    number_of_balls += 1
                    player_score_total += x
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                if player_score_total > bot_score_total:
                    print("You won by", player_score_total - bot_score_total)
                    break
            else:
                print("out of range")
                time.sleep(3)
                print(f"penalty of -5 points for out of range input")
                player_score_total = max(0, player_score-5)
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                print("|                                                                            |")
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")

else :
    print("=" * 60)
    print("the number is ",z,"u lost the toss")
    print
    a=random.choice(["batting","bowling"])
    print("bot choose ",a)
    if a=="batting":
        print("now bot is batting and u are bowling")
        print("-" * 60)
        time.sleep(3)
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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x==y:
                    print ("out")
                    time.sleep(3)
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-1         |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                    break
                else:
                    bot_score += y
                    bot_score_total += y
                    number_of_balls_bot += 1

                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")
            else:
                print("out of range")
                time.sleep(3)
                print(f"penalty of +5 runs to bot score for out of range input")
                bot_score_total = bot_score + 5
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                print("|                                                                            |")
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")

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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x == y:
                    print("OUT")
                    time.sleep(3)
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-1      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                    if player_score_total > bot_score_total:
                        print("You won by", player_score_total - bot_score_total)
                        result = "You won"
                    elif player_score_total < bot_score_total:
                        print("Bot won by", bot_score_total - player_score_total)
                        result = "Bot won"
                    else:
                        print("Match tied")
                        result = "Match tied"

                    break
                else:
                    player_score += x
                    number_of_balls += 1
                    player_score_total += x
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                if player_score_total > bot_score_total:
                    print("You won by", player_score_total - bot_score_total)
                    result = "You won"
                    break
            else:
                print("out of range")
                print(f"penalty of -5 points for out of range input")
                player_score_total = max(0, player_score-5)
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                print("|                                                                            |")
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")

    elif a== "bowling":
        print("bot chose bowling and you are batting")
        print("-" * 60)
        time.sleep(3)
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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x==y:
                    print ("out")
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-1      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                    break
                else:
                    player_score += x
                    number_of_balls += 1
                    player_score_total += x
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

            else:
                print("out of range")
                print(f"penalty of -5 points for out of range input")
                player_score_total = max(0, player_score-5)
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {player_score_total}-0      |")
                print("|                                                                            |") 
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")

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
            print(f"Bot entered number is {y}")
            if 0<=x<=10:
                if x == y:
                    print("OUT")
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-1         |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                    if bot_score_total > player_score_total:
                        print("Bot won by", bot_score_total - player_score_total)
                        result = "Bot won"
                    elif bot_score_total < player_score_total:
                        print("You won by", player_score_total - bot_score_total )
                        result = "You won"
                    else:
                        print("Match tied")
                        result = "Match tied"

                    break
                else:
                    bot_score += y
                    bot_score_total += y
                    number_of_balls_bot += 1
                    print("=============================================================================")
                    print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                    print("|                                                                            |")
                    print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                    print("|                                                                            |")
                    print("=============================================================================")

                if bot_score_total > player_score_total:
                    print("Bot won by", bot_score_total - player_score_total)
                    result = "Bot won"
                    break
            else:
                print("out of range")
                print(f"penalty of +5 runs to bot score for out of range input")
                bot_score_total = bot_score + 5
                print("=============================================================================")
                print(f"|{user}   {player_score} ({number_of_balls})    {bot_score_total}-0         |")
                print("|                                                                            |")
                print(f"|bot   {bot_score} ({number_of_balls_bot})                                  |")
                print("|                                                                            |")
                print("=============================================================================")

cursor.execute("""
UPDATE users
SET matches = matches + 1,
    total_runs = total_runs + %s
WHERE username = %s
""", (player_score_total, user))
db.commit()

if result == "You won":
    cursor.execute("""
    UPDATE users
    SET wins = wins + 1
    WHERE username = %s
    """, (user,))
    db.commit()

elif result == "Bot won":
    cursor.execute("""
    UPDATE users
    SET losses = losses + 1
    WHERE username = %s
    """, (user,))
    db.commit()

cursor.execute("""
UPDATE users
SET highest_score = GREATEST(highest_score, %s)
WHERE username = %s
""", (player_score_total, user))
db.commit()

cursor.execute("""
SELECT matches, wins, losses, highest_score, total_runs
FROM users
WHERE username=%s
""", (user,))

stats = cursor.fetchone()

print("\n========== PLAYER STATS ==========")
print("Matches Played :", stats[0])
print("Wins           :", stats[1])
print("Losses         :", stats[2])
print("Highest Score  :", stats[3])
print("Total Runs     :", stats[4])
print("==================================")

leaderboard_choice = input("\nDo you want to see the leaderboard? (yes/no): ").lower()
if leaderboard_choice == "yes":
    cursor.execute("""
    SELECT username, wins, highest_score
    FROM users
    ORDER BY wins DESC, highest_score DESC
    LIMIT 5
    """)

    print("\n===== TOP 5 PLAYERS =====")
    for row in cursor.fetchall():
        print(f"{row[0]:10} Wins: {row[1]:2}  Highest: {row[2]}")
