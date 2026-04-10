import datetime

currentTime = datetime.datetime.now()
name = input("Enter Your Name: ")
if(currentTime.hour<12):
    print("Good Morning",name)
elif(12<=currentTime.hour<18):
    print("Good Afternoon",name)
else:
    print("Good Evening",name)




