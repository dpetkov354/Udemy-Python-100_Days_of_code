from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, Dimitar!<h1>' \
#            '<p>This is a paragraph</p>' \
#            '<img src="https://media.giphy.com/media/2zotXB1xGbTB28cKAD/giphy.gif" width =200>'  # Can take HTML tags and CSS Style and images,GIFs via link
#
#
# def bold(function):  # bold text decorator
#     def bold_wrap():
#         return f"<b>{function()}</b>"
#
#     return bold_wrap
#
#
# @app.route('/bye')  # can make multiple decorators (this one makes the text bold)
# @bold
# def bye_world():
#     return "Bye, Dimitar!"
#
#
# @app.route("/username/<name>/<int:age>")  # Variable url / 2 variables / and predefine its type to int
# def greet(name, age):
#     return f"Have a nice day {name}, {age} years old!"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)  # Enables debug mode


# Day 55 Start

# Advanced Python Decorator Functions

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
# new_user = User("angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)

# Exercise

def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        # result = fn(args[0], args[1], args[2])
        result = fn(*args)
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
# def a_function(a, b, c):
def a_function(*args):
    product = 1
    for arg in args:
        product *= arg
    return product


@logging_decorator
def b_function(*args):
    return sum(args)


a_function(1, 2, 3)
a_function(1, 2, 3, 4)
b_function(4, 5)
b_function(3, 5, 7, 2)
