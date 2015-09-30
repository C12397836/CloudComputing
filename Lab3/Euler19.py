week in range (1,4)
month in range (1, 12)
year in range (1900, 2001)
d (1,7)
result =1
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

if(month =9 || 4 || 6 || 11):
  day in range(1,30)
else if(month =2):
  day in range(1,28)
else:
  day in range(1,31)

if(day==1 && month ==1 && year==1900)
  d=7

for(;;):
  d++
    if(d>7):
      d=1 && week++
        if(week>4):
          week=1 && month ++
            if(month>12):
              month=1 && year++
                if(d==7 && day ==1 && week ==1 ):
                  result++

print result



