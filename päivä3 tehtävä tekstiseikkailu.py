
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
eka = (input("Do you want left or right? \n")).lower()
if eka =="left":
  toka = input("Nice pick, you avoided the wolfs! You come to a lake, boat is coming in 5min, wait or swim? \n").lower()
  if toka =="wait":
    kolmas = input("Nice one, the boat takes you safely across the lake. You come to three doors, which do you want to open, red, blue or yellow? \n").lower()
    if kolmas =="yellow":
        print("You win, awesome, look at all this moneeeeyyy")
    elif kolmas =="red":
        print("Oh no, this is the red light district, no treasure this time")
    elif kolmas =="blue":
        print("Oh no, the Blues Brothers are here! So much for the treasure I guess...")
    else:
        print("Come on mate, you had one job")
  else:
    print("Forgot you can't swim, aye?")
elif eka =="right":
  print("Oh no, the wolfs are coming, aaaargh... say goodbye to my turtle Leonardo")
else:
  print("try again!")