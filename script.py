print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 1

# Write an if statement below:

if planet == 1:
  print("Your weight on Venus is " + str(round(weight * 0.91, 1)) + " pounds.")
elif planet == 2:
  print("Your weight on Mars is " + str(round(weight * 0.38, 1)) + " pounds.")
elif planet == 3:
  print("Your weight on Jupiter is " + str(round(weight * 2.34, 1)) + " pounds.")
elif planet == 4:
  print("Your weight on Saturn is " + str(round(weight * 1.06, 1)) + " pounds.")
elif planet == 5:
  print("Your weight on Uranus is " + str(round(weight * 0.92, 1)) + " pounds.")
elif planet == 6:
  print("Your weight on Neptune is " + str(round(weight * 1.19, 1)) + " pounds.")
else:
  print("Your weight on earth is " + str(weight) + " pounds.\nPlease input planet numbers 1 - 6 for additional weights.")
