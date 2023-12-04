import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    count = 0
    text = request.form['text']
    for char in text:
        if char in 'aeiou':
            count +=1
    return f'There are {count} vowels in "{text}"'

@app.route('/sort_names',methods=['POST'])
def sort_names():
    
    
    return ','.join(sorted(request.form['names'].split(',')))

@app.route('/names', methods =['GET'])
def get_names():
    nameslist = ['Karim','Alice','Julia']
    names = request.args['add']
    names = names.split(',')
    for name in names:
        if name.isalpha():
            nameslist.append(name)
        else:
            return 'Invalid name structure. Please seperate names by commas(,) I.e "name1,name2,name3"'
        
    return ', '.join(sorted(nameslist))
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

