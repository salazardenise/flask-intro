"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<a href='/hello'>Hola page !</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    # first part of HTML
    top_part = """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          How awesome are you?
          <select name="compliment_choice">
    """

    # last part of HTML
    last_part = """
          </select>
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

    # generate middle part of HTML
    options = []
    for compliment in AWESOMENESS:
        option_string = "<option value='terrific'>{}</option>".format(compliment)
        options.append(option_string)

    middle_part = ' '.join(options)

    return top_part + middle_part + last_part 


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
