# working with the if statement
# use the input () function to get information from the user
userReply = input("Do you need to ship a package? (Enter yes or no)")

#working wiht the else statement
#use the if statement to print a response (== symbols is a comparative operator. means equal to)
if userReply == "yes":
    print("we can help you ship the package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
# working with the elif statement
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")