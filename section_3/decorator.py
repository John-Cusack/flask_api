import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_fun():
        print('im the decorator')
        func()
        print('after the dec')
    return function_that_runs_fun

@my_decorator
def my_function():
    print('im the function')

my_function()


##
def decorator_with_argumnets(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_fun():
            print('im the dev')
            if number == 56:
                print('not running func')
            else:
                func()
            print('after')
        return function_that_runs_fun
    return my_decorator

@decorator_with_argumnets(56)
def my_function_too():
    print('hello')

my_function_too()
