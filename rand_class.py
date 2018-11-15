"""print("generating random numbers")

import random as ran
for i in range(5):
    print(ran.randint(0,10))"""

"""import random as ran

print("GUESSING GAME\n")
print("from numbers 1 to 10, guess the number i have picked")

while True:
    score = (0)
    while True:
        response = ran.randint(0,5)
        player_guess= int(input("what number have i picked?: "))
        if player_guess ==(response):
        
            print ("CORRECT!You guessed right!")
            score = score + 1
            print ("score:", score)
        
        elif player_guess !=(response):
            print("wrong guess. try again!")
            print ("score:", score)
            break"""
    

print("zodiac signs indicator")
zodiac_signs= ["aqua"," pisces","aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagi","capri"]
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
while True:
    user_input= input("what month were you born? :")
    for index in range (12):
        if months[index]== user_input:
            print("your zodiac sign is: ", zodiac_signs[index])
    
        break

⚀ ⚁ ⚂ ⚃ ⚄ ⚅