# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nimet = (name1).lower()+(name2).lower()
eka_nro = (nimet.count("t")+nimet.count("r")+nimet.count("u")+nimet.count("e"))
toka_nro = (nimet.count("l")+nimet.count("o")+nimet.count("v")+nimet.count("e"))
score = str(eka_nro)+str(toka_nro)

pisteet = ("Your score is "+score)
if int(score) < 10 or int(score) > 90:
    print(pisteet + ", you go together like coke and mentos.")
elif int(score) >40 and int(score) <50:
    print(pisteet +", you are alright together.")
else:
    print(pisteet + ".")