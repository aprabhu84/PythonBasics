
### Function written to print the list of Movies on the basis of AgeRestrictions ###
def print_movies():
    movie_names = list(drct_movies.keys())
    keylen = len(movie_names)

    while (keylen > 0):
        if (age >= drct_movies[movie_names[keylen-1]]["age_rstrct"]):
            print ("\t\t" + str(keylen) + ". " + movie_names[keylen-1])
        keylen = keylen - 1


# Create a basic movie list with its parameters
drct_movies = {
    "Black Panther" : {"type" : "Action", "age_rstrct" : 12, "tickets" : 5},
    "Insedious" : {"type" : "Horror", "age_rstrct" : 18, "tickets" : 5},
    "50 Shares Darker" : {"type" : "Drama", "age_rstrct" : 18, "tickets" : 10},
    "Justice League" : {"type" : "Action", "age_rstrct" : 12, "tickets" : 10},
    "Ferdinand" : {"type" : "Animated", "age_rstrct" : 0, "tickets" : 15},
               }

repeat = True

while repeat:
    
    # Get the user's Name and Age in Movie
    print("\tHi! I am your Movie Assistant, Please provide me wiht the following information")
    name = input ("\t > Name : ").strip().capitalize()
    age = int(input("\t > Age : ").strip())

    # Display the movies as per age restrictions and ask to select
    print_movies()

    #Ask the user to select the Movie to go to
    whichMovie = input("\t > Which Movie do you want to go to? (Give the Movie Number from above)")
    whichMovie = int(whichMovie)
    movie_names = list(drct_movies.keys())
    
    if(whichMovie > len(movie_names)):
        print(f"\t @@@@ Please select a valid movie number!! @@@@")
        continue
    else:
        print("\t > Movie {} slected for tickets".format(movie_names[whichMovie-1]))

    # Ask for the number of tickets and Movie
    numTickets = input("\t > Number of Tickets you need? ")
    numTickets = int(numTickets)

    # Depending on availability assign the tickets or display the appropriate message    
    if drct_movies[movie_names[whichMovie-1]]["tickets"] >= numTickets:
        drct_movies[movie_names[whichMovie-1]]["tickets"] = drct_movies[movie_names[whichMovie-1]]["tickets"] - numTickets
        print (f"\t > You purchases {numTickets} tickets successfully for the Show {whichMovie}. Enjoy the Show!!")
    else:
        print (f"\t @@@@ {numTickets} tickets are not available for the show {whichMovie} for your purchased @@@@")
        
    # Provide ticket status to the users
    print ("\t > Ticket status for the other movies is as follows")
    for name in movie_names:
        
        print(f"\t\t Movie - {name}\t\tTickets Avilable - {drct_movies[name]['tickets']}")
    


    # Ask users if they want to stop the Movie Assist
    var_stop = input ("\n\t >> Do you want to book more tickets? (Y/N) : ").strip().capitalize()
    if (var_stop == "N"):
        repeat = False

print ("*"*154 + "\n" + "*"*50 + "!!! Good Bye... It was nice doing business with you !!!" + "*"*50 + "\n" + "*"*154)




