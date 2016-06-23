
#This is a simple python program that opens the webbrowser with the specified URL after certain amount of Time breaks
#It needs the webbrowser and time library
import webbrowser
import time

i=0
break_counter = 0
print("Current time is "+time.ctime())

while i < 2:
    time.sleep(5) #wait 5 seconds till the next browser opening
    print("Looping",i)
    webbrowser.open("www.google.com")
    break_counter+=1
    i+=1
    
print ("outside loop now")
