#!/usr/bin/env python3
print("Name: Brayden Parman")

password_database = {"Username" : "dnedry", "Password" : "please"}
command_database = {"reboot" : "OK. I will reboot all park systems", \
"shutdown" : "OK. I will shut down all park systems.", \
 "done" : "I hate all this hacker stuff."}


white_rabbit_object = 0
counter = 0

while white_rabbit_object == 0 and counter < 3:
#If white_rabit is not greater than 0 and the counter is less than 3 the loop continues otherwise it kicks out.
    input_user = input("Enter Username: ")
    input_password = input("Enter Password: ")
    if (input_user == password_database["Username"]) and (input_password == password_database["Password"]):
    #if the user iputed username and password are both coorect then:
        white_rabbit_object += 1
        #add 1 to the white_rabbit_object 
        print("Hi, Brayden. You're still the best hacker in Jurassic Park.")
        #print following statement
        command_input = input("Enter command reboot, shutdown, or done: ")
        #print following statement and accept user input
        if (command_input == "reboot"):
        #if user inputs reboot then:
            print(command_database["reboot"])
            #print the value that corresponds to reboot key in command_database
        elif (command_input == "shutdown"):
        #if user inputs shutdown then:
            print(command_database["shutdown"])
            #print the value that corresponds to the shutdown key in command_database
        elif (command_input == "done"):
        #if user inputs done then:
            print(command_database["done"])
            #print the value that corresponds to the done key in command_database
        else:
        #if anything else is entered then:
            print("The Lysine Contingency has been put into effect.")
            #print the following statement
        #white_rabbit_object += 1
    #elif (input_user != password_database["Username"]) or (input_password != password_database["Password"]):
    else:
    #if anyting but the correct password and username are entered then:
        counter += 1
        #add 1 to counter
        if (counter >= 3):
        #if the counter is greater than or equal to 3 then:
            print(f"You didn't say the magic word.\n"*25)
            #print the following statement 25 times on a new line each time
        else:
        #if counter is anything less than 3
            print(f"You didn't say the magic word. {counter}")
            #print the following statement with the current counter value at the end
        #counter += 1
