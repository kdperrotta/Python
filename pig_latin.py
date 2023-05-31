"""
A very basic program that converts a user's input into pig latin.

1) Ask input for original phrase
3) Convert to pig latin
4) Print output and ask user if they want to try again
"""

def pig_latin():
    while True:
        print("~Pig Latin Generator~\n")

        #Ask input for original phrase
        original_message = input("Enter the phrase to be translated: ")

        #Convert to pig latin
        translated_phrase = ""
        for word in original_message.split():
            new_word = word[1:] + word[0] + "ay"
            message = "hello"
            translated_phrase += new_word + " "


        #Print output and ask user if they want to try again
        print(translated_phrase)

        play_again = input("Would you like to translate another phrase? y/n: ")
        if play_again == "n":
            break
        else:
            continue


pig_latin()
