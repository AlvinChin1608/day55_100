# day55_100
# What I Learned Today: Flask Decorators: Enhancing Routes and User Authentication

## Key Takeaways:
- Use decorators to modify Flask route behaviour in a reusable way.
- Implement text formatting, function logging, and user authentication with decorators.

## Explanation:

### Text Formatting:
I have created custom decorators (make_bold, make_italic, and make_underline) to format text returned by routes.

```python
@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'bye'
```

- __Routes:__ Defined routes like / (root), /bye (formatted text), and dynamic route /&lt;name&gt;/&lt;int:number&gt;for greetings.
- __Function Logging:__ Created a logging_decorator to log function calls, arguments, and return values.

```python
def logging_decorator(fn):
    def wrapper(*args):
        # Log function name and arguments
        result = fn(*args)
        # Log return value
        return result
    return wrapper
```
- __User Authentication:__ Implemented an is_authenticated_decorator to restrict access based on user login status.

```python
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):  
        if args[0].is_logged_in:
            function(args[0])
        else:
            # Handle authentication failure (e.g., redirect to login)
    return wrapper
```
## Conclusion:

Exploring Flask decorators enhanced my understanding of building robust and maintainable web applications. These decorators can be used for various functionalities beyond the examples covered here.
