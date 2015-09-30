
week =1
month=1
year=1900
d=1
day=1

result=1

'''
week in range (1,4)
month in range (1, 12)
year in range (1900, 2001)
d in range(1,7)
result =1
'''
'''
jan 1
feb 2
mar 3
april 4
may 5
june 6
jul 7
aug 8
sept 9
octo 10
nov 11
dec 12
'''



for x in range(0, 100):
  if(month == 9 or 4 or 6 or 11):
    day in range(1,30)
  elif(month ==2):
    day in range(1,28)
  else:
    day in range(1,31)

  d+=1
  if(d==7 and day ==1 and week ==1 ):
    result+=1
  if(d>7):
    d=1
    week +=1
    if(week>4):
      week=1
      month +=1
      if(month>12):
        month=1
        year +=1


print result



