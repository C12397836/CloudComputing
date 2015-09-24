total = 0
for num in range(1000):
  if num % 3 ==0 or num % 5 ==0:
    total+=num
print total

x=1
y=2
z=0

while x<=400000:
  z=x+y
  print z
  x=y
  y=z
