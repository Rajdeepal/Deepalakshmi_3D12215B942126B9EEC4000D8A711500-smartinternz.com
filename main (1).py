year=int(input("ente the year")) 
if(year% 4==0and year%1000!=0):
   print ("the year is Leap year")
elif(year % 400==0):
    print("the year is Leap year")
else:
    print("the year is not Leap year")