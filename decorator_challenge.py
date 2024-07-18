"""Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given and finally the returned output:

You called a_function(1,2,3)
It returned: 6
The value 6 is the return value of the function. Don't change the body of a_function.

IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.

"""

# Positional Arguments - *args
# Key Word Arguments - **kwargs

inputs = eval(input())
# TODO: Create the logging_decorator() function 👇

def logging_decorator(fn):
  def wrapper(*args):
      print(f"You called {fn.__name__}{args}")
      result = fn(args[0], args[1], args[2])
      print(f"It returned: {result}")
  return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])