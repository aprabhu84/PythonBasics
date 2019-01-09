# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(sentance):

    words = sentance.split()
    reverse = ""

    while len(words) != 0:
        reverse = reverse + words.pop() + " "

    return reverse
        
