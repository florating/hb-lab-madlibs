"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "<b>Hi!</b> This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment using user input from /hello."""

    player = request.args.get("person") # from /hello (from hello.html, specifically)

    compliment = choice(AWESOMENESS)
    
    # could rename to greet_and_compliment.html so connection between /greet webpage and the HTML template is clear
    # person and compliment are variables that appear in compliment.html
    # we are assigning values player and compliment from above, respectively, to those two variables
    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Get the user's response to the Yes/No question from /greet"""
    answer = request.args.get("game")

    if answer == "yes":
        temp = "game.html"
    else:
        temp = "goodbye.html"
    
    return render_template(temp)


@app.route('/madlib')
def show_madlib():
    """Show madlibs story using user input from /game"""
    madlib_options = ['person', 'color', 'noun', 'adjective']
    madlib_dict = {}
    for item in madlib_options:
        madlib_dict[item] = request.args.get(item)
    return render_template('madlib.html', person=madlib_dict['person'], color=madlib_dict['color'], noun=madlib_dict['noun'], adjective=madlib_dict['adjective'])


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
