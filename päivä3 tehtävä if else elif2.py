height = (int(input("How tall are you?")))
bill = 0
if height >=120:
  print("Welcome to the rollercoaster!")

  age = (int(input("How old are you? ")))
  if age < 12:
    bill = 5
    print("Child tickets are 5€")
  elif age <= 18:
    bill = 7
    print("Youth tickets are 7€")
  elif age >45 and age <55:
    print("Free for midlife crisis!")
    bill = 0
  else:
    print("Adult tickets are 12€")
    bill = 12
  pic = (input("Do you want a pic for additional 3€, y or n?"))
  if pic == "y":
    bill += 3

  print(f"Your final bill is {bill}€")
else:
  print("Sorry, maybe next year!")