# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_mcdonald(anytext):

    lenText = len(anytext)
    textList = []

    if lenText < 4 :
        return ("Please enter Text with more than 4 characters in length")

    return f"{anytext[0:3].capitalize()}{anytext[3:].capitalize()}"
