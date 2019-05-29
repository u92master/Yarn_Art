#This program is written in Python by GriffinC7
import random
import time
print("Yarn Art Generator")
print("The data will return in the following format:")
print("X Coordinate , Y Coordinate | Color")
print("===================================")
for i in range (0, 80): #The last number (80) in the parenthesis can be altered depending on how much work you want to do
  print("===========================")
  time.sleep(0.5)
  color = random.randint(1,3) #Generates the color
  x = random.randint(1,24) #Generates the X Coordinate
  y = random.randint(1,48) #Generates the Y Coordinate
  if color == 1:
    print(x, " , ", y, " | RED")
  elif color == 2:
    print(x, " , ", y, " | BLUE")
  elif color == 3:
    print(x, " , ", y, " | GREEN")
print("==============================")
print("End Program")
