#Euler Question 1

print "Euler Question 1"

total = 0
for num in range(1000):
  if num % 3 ==0 or num % 5 ==0:
    total+=num
print total


#Euler Question 2
print "Euler Question 2"
x=1
y=2
z=0

while x<=40:
  z=x+y
  print z
  x=y
  y=z
