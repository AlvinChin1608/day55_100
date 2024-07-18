from flask import Flask

app = Flask(__name__)

def make_bold(screen_text):
    def wrapper_function():
        return f"<b>{screen_text()}</b>"
    return wrapper_function

def make_italic(screen_text):
    def wrapper_function():
        return f"<em>{screen_text()}</em>"
    return wrapper_function

def make_underline(screen_text):
    def wrapper_function():
        return f"<u>{screen_text()}</u>"
    return wrapper_function

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello World</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://tinyurl.com/3udbauxt" width= 200 height =200>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2lic2Z5eTZ0MXYyb2o5Y2FpNTd2Z3pxcW90eDczcWJpYmZtcno2OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif" width=200>')

#Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'bye'

#Creating variable paths and converting the path to a specified data type
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"

if __name__ == "__main__":
    #run the app in debug mode to auto-reload
    app.run(debug=True)