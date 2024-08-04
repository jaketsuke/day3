# 🚨 Don't change the code below 👇
print("Lasketaan autosi todelliset kulut!")
arvo = int(input("Paljonko on autosi myyntiarvo? \n"))
vm = int(input("Minkä vuosimallin autoa ajat? \n"))
vero = int(input("Paljonko on autosi autovero vuodessa? \n"))
#Voisko saada rekkarihaulla?
vakuutus = int(input("Paljonko on autosi vakuutusmaksu vuodessa? \n"))
huolto = int(input("Paljonko maksaa huollot vuodessa? \n"))
pesut = int(input("Paljonko maksaa pesut vuodessa? \n"))
tuulilasinpesu = int(input("Paljonko maksaa lasinpesuaineet vuodessa? \n"))
rahoitus = int(input("Paljonko maksat lainan korkoja vuodessa? \n"))
katsastus = int(input("Paljonko menee katsastuksiin vuodessa? \n"))
renkaat = int(input("Paljonko menee renkaisiin ja niiden vaihtoon ja säilytykseen vuodessa? \n"))

ikä = 2022 - vm
if ikä < 5:
    arvonalenema = arvo * 0.1
else:
    arvonalenema = arvo * 0.07

Kiinteä = vero+vakuutus+huolto+pesut+tuulilasinpesu+rahoitus+katsastus+renkaat+arvonalenema
km = int(input("Paljonko vuodessa tulee kilometrejä? \n"))
kulutus = int(input("Montako litraa autosi kuluttaa/100km? \n"))
löpöhinta = float(input("Paljonko maksaa löpö? \n"))
muuttuva = (km/100)*kulutus*löpöhinta
yht = Kiinteä + muuttuva
kk = yht / 12
pyör_kk = ("{:.2f}".format(round(kk,2)))
perkm = yht / km
pyör_perkm = ("{:.2f}".format(round(perkm,2)))
print(f"Kulut autollesi ovat {yht} euroa vuodessa, eli {pyör_kk} euroa kuukaudessa.")
print(f"Hinta per kilometri sinulle on {pyör_perkm}€/km, verohallinnon mukaan keskiarvo olisi 0,43€/km")
