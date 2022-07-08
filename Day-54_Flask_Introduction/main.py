# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, Dimitar!'
#
#
# if __name__ == "__main__":
#     app.run()

import time
# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrap_func():
        before_time = time.time()
        function()
        after_time = time.time()
        duration = after_time - before_time
        func_name = function.__name__
        print(f"{func_name} run speed: {duration}")
    return wrap_func


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
