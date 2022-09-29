# Set up your imports and your flask app.
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('07-solution-index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.
    lower_letter = False
    upper_letter = False
    num_end = False

    username = request.args.get('username')
    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input
    report = lower_letter and upper_letter and num_end
    # Return the information to the report page html.


if __name__ == '__main__':
    # Fill this in!
    pass
