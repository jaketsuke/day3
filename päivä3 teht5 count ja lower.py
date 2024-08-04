# 🚨 Don't change the code below 👇
print("Lasketaan autosi todelliset kulut!")
arvo = input("Paljonko on autosi myyntiarvo? \n")
vm = input("Minkä vuosimallin autoa ajat? \n")
vero = input("Paljonko on autosi autovero vuodessa? \n")
vakuutus = input("Paljonko on autosi vakuutusmaksu vuodessa? \n")
huolto = input("Paljonko maksaa huollot vuodessa? \n")
pesut = input("Paljonko maksaa pesut vuodessa? \n")
tuulilasinpesu = input("Paljonko maksaa lasinpesuaineet vuodessa? \n")
rahoitus = input("Paljonko maksat lainan korkoja vuodessa? \n")
katsastus = input("Paljonko menee katsastuksiin vuodessa? \n")
renkaat = input("Paljonko menee renkaisiin ja niiden vaihtoon ja säilytykseen vuodessa? \n")

if 2022 - vm > 5:
    arvonalenema = arvo * 0.1
else:
    arvonalenema = arvo * 0.07

Kiinteä = vero+vakuutus+huolto+pesut+tuulilasinpesu+rahoitus+katsastus+renkaat+arvonalenema
kk = Kiinteä / 12
print(f"Kiinteät kulut autollesi ovat {Kiinteä} euroa vuodessa, eli {kk} euroa kuukaudessa.")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lc_nimi1 = name1.lower()
lc_nimi2 = name2.lower()
nimet = lc_nimi1 + lc_nimi2

teet = nimet.count("t")
ärrät = nimet.count("r")
uut = nimet.count("u")
eet = nimet.count("e")
ekaluku = (teet+ärrät+uut+eet)

ällät = nimet.count("l")
oot = nimet.count("o")
veet = nimet.count("v")
tokaluku = (ällät+oot+veet+eet)
ekalukuteksti = str(ekaluku)
tokalukuteksti = str(tokaluku)
score = ekalukuteksti + tokalukuteksti
int_score = int(score)

if int_score <= 10 or int_score >= 90:
    print(f"Your score is {int_score}, you go together like coke and mentos.")
elif int_score <= 50 and int_score >= 40:
    print(f"Your score is {int_score}, you are alright together.")
else:
    print(f"Your score is {int_score}.")