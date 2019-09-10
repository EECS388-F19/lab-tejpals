import random

print("Tejpal Singh")
sum = 0
for x in range(2):
  num = random.randint(0,100)
  sum += num
  print(num)
print("Sum = " + str(sum))
print("Average = " + str(sum / 2))
