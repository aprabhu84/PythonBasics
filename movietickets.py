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
    movie_names = list(drct_movies.keys())
    keylen = len(movie_names)

    while (keylen > 0):
        if (age >= drct_movies[movie_names[keylen-1]]["age_rstrct"]):
            print ("\t\t" + str(keylen) + ". " + movie_names[keylen-1])
        keylen = keylen - 1

# Ask for the number of tickets


# Depending on availability assign the tickets or display the appropriate message


# Print the ticket status to the users


# Ask users if they want to stop the Movie Assist
    var_stop = input ("\n\t >> Do you want to stop the Movie Assist? (Y/N) : ").strip().capitalize()
    if (var_stop == "Y"):
        repeat = False

print ("*"*154 + "\n" + "*"*50 + "!!! Good Bye... It was nice doing business with you !!!" + "*"*50 + "\n" + "*"*154)


