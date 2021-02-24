from flask import Flask
from random import randint
app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def Funny_Story(adjective, noun):
    return f"""Once Upon a Midnight {adjective} \n 
    The {noun} fell upon themself"""

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    num1 = number1
    num2 = number2
    if num1.isdigit() and num2.isdigit() == False:
        return 'Invalid inputs. Please try again by entering 2 numbers!'
    if num1.isdigit() and num2.isdigit() == True:
        num1 = int(number1)
        num2 = int(number2)
        num3 = num1*num2
        return f'{num3}'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    poof = n
    if poof.isdigit() == False:
        return f'Invalid input. Please try again by entering a word and a number!'
    Times = int(n)
    lister = '' 
    temp = word
    for each in range(Times):
        lister = lister + ' ' + temp
    return lister


@app.route('/dicegame/')
def rollingdice():
    rolled = randint(1,6)
    return f'{rolled}'


        









if (__name__) == '__main__':
    app.run(debug=True)
