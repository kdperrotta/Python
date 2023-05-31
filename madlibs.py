"""
This is a madlib generator, which generates a random number and chooses a basic story template based on that number.
It will then get the user's input to complete the words needed for the story, concatenate the words into the story string, and print it for the user.
"""
import random

# Choose a random number
story_number = ''
def choose_random_number():
    global story_number
    story_number += str(random.randint(1, 3))

# Define the mad lib stories and get user input
def madlib1():
    animals= input('Enter an animal name : ')
    profession = input('Enter the name of a profession: ')
    clothes = input('Enter a type of clothing: ')
    things = input('Enter an object: ')
    name = input('Enter a person\'s name: ')
    place = input('Enter a place: ')
    verb = input('Enter a verb in the \'ing\' form: ')
    food = input('Enter a food: ')

    print('Say \"' + food + '!\", the photographer said as the camera flashed. ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like a ' + things + ' wearing ' + clothes + ' and ' + verb + ' -- exactly what I had in mind!')

def madlib2():
    adjective = input('Enter an adjective: ')
    color = input('Enter a color name: ')
    thing = input('Enter a thing name: ')
    place = input('Enter a place: ')
    person= input('Enter a person\'s name: ')
    adjective1 = input('Enter an adjective: ')
    insect= input('Enter a insect: ')
    food = input('Enter a food: ')
    verb = input('Enter a verb: ')

    print('Last night I dreamed I was a ' + adjective + ' bird with ' + color + ' splotches that looked like '+ thing + '. I flew to ' + place + ' with my best friend and '+ person + ' who was a '+ adjective1 + ' ' + insect +'. We ate some ' + food + ' when we got there and then decided to '+ verb + ' and the dream ended when I said-- \"lets ' + verb + '.\"')

def madlib3():
    person = input('Enter a person\'s name: ')
    color = input('Enter a color: ')
    foods = input('Enter a food: ')
    adjective = input('Enter an adjective: ')
    thing = input('Enter a thing: ')
    place = input('Enter a place: ')
    verb = input('Enter a verb: ')
    adverb = input('Enter an adverb: ')
    food = input('Enter a food: ')
    things = input('Enter a thing: ')

    print('Today we picked apples from '+ person + "'s orchard. I had no idea there were so many different varieties of apples. I ate " + color + ' apples straight off the tree that tasted like '+ foods + '. Then there was a '+ adjective + ' apple that looked like a ' + thing +'. When our bags were full, we went on a hay ride to '+ place + ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples. We are going to make appple '+ food + ' and '+ things +' pies!.')

# Choose story based on the random number
def choose_story(story_number):
    if story_number == '1':
        madlib1()
    elif story_number == '2':
        madlib2()
    elif story_number == '3':
        madlib3()

# Run programs to choose random number and generate story
choose_random_number()
choose_story(story_number)
