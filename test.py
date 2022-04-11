# discovering python
import time

i = 0
b = 2
a = 0

#how to do a while in python ok that's easy

# while b > a:
    # if b > a:
    #     i += 1
    # else:
    #     for i in range(b):
    #         print("I still don't know what I'm doing")
    # a = a + (b/2)
    #this is something I really hate but I'm doing this because it's a test file

while a < b:
    a += 1
    print("i'm adding one to the a variable")
    #to use this function I have to import the time module, let's do it
    time.sleep(1)
    #eventually I've discovered that what sleep takes as argument is the number of seconds
    #and not the number of milliseconds
    print ("now the value of a is", a)
    #well I'm trying to figure out why it print like this
    #this is a bit strange for me LoL
print("congrats, a is grater than b")

