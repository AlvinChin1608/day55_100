class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

"""
*args, **kwargs: These are used to pass any number of positional and keyword arguments to the wrapped function.
args[0].is_logged_in: This checks if the first argument (which is expected to be a User object) is logged in.
"""


# Define a decorator to check if a user is authenticated
def is_authenticated_decorator(function):
    # Define the wrapper function
    def wrapper(*args, **kwargs):
        # Check if the first argument (expected to be a User object) is logged in
        if args[0].is_logged_in == True:
            # If logged in, call the original function with the user object
            function(args[0])
    # Return the wrapper function
    return wrapper


# Define a function to create a blog post, decorated with the authentication check
@is_authenticated_decorator
def create_blog_post(user):
    # Print a message indicating a new blog post by the user
    print(f"This is {user.name}'s new blog post. ")


# Create a new User object with the name "Alvin"
new_user = User("Alvin")
# Set the user's logged-in status to True
new_user.is_logged_in = True
# Call the create_blog_post function with the new_user object
# The decorator will check if the user is logged in before allowing the function to execute
create_blog_post(new_user)
