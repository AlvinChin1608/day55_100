from flask import Flask
import random

app = Flask(__name__)

Rand_Number = random.randint(0, 9)  # Generate the random number when the server starts
print(Rand_Number)

# Decorator to wrap text in <h1> tags
def home_page(screen_text):
    def wrapper():
        return f"<h1>{screen_text()}</h1>"
    return wrapper

@app.route('/')
@home_page
def greet_page():
    return "Guess a number between 0 and 9"

@app.route('/<int:Guess_Number>')
def Guess(Guess_Number):
    if Guess_Number == Rand_Number:
        return ('<h1>You Got it!</h1>'
                '<img src= "https://i.giphy.com/media/v1'
                '.Y2lkPTc5MGI3NjExZmZieGhkaW96cG5rdGRhMjFveHZjZGt0eHpuMWJ6a3J3emJ1eWdldSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26uTqJWUxDMgWc5pu/giphy.gif">')
    else:
        return ('<h1>Wrong Number, try again!</h1>'
                '<img src="https://i.giphy.com/media/v1'
                '.Y2lkPTc5MGI3NjExcndzOXpyejBpNnBuMzUyZ2Z6YzhkOHlqYWd3Z3ppZDUxdzM1YzA3YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jyEM1C2euOklQ18qrq/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)