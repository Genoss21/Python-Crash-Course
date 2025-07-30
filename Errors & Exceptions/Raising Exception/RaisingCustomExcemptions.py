class MyCustomError(Exception):
    pass

def risky_function():
    raise MyCustomError("Something went wrong in risky_function")

try:
    risky_function()
except MyCustomError as e:
    print(e)