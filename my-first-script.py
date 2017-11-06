def welcome_message(name):
    #Prints out a personalised welcome message
    return "Welcome to this Python script, {}!".format(name)

def enjoy_yourself(name):
    #prints how I'm happy to learn python
    return "Long time you wanted to learn python, congratulations {}".format(name)

#Call the welcome message function with the input "Udacity Student" 
#and print the output
print(welcome_message("Udacity Student"))
print(enjoy_yourself('eduardo'))