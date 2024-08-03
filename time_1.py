import time

t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))

print(t)
print(hour)

if(0<hour and hour<12):
  print("GM")
elif(12<=hour<18):
  print("GA")
elif(18<=hour<21):
  print("GA")  
else:
  print("GN")
