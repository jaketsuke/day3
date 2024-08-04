height = (int(input("How tall are you?")))
bill = 0
if height >=120:
  print("Welcome to the rollercoaster!")

  age = (int(input("How old are you? ")))
  if age < 12:
    bill = 5
    print("Child tickets are 5€")
  elif age > 18:
    bill = 12
    print("Adult tickets are 12€")
  else:
    print("Youth tickets are 7€")
    bill = 7
  pic = (int(input("Do you want a pic for additional 3€, y or n?")))
  if pic == "y":
    bill += 3

  print(f"Your final bill is {bill}€")
else:
  print("Sorry, maybe next year!")
pic = (int(input("Do you want a pic for additional 3€?")))