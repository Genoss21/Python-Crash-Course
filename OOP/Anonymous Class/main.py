# Create an anonymous class dynamically
AnonymousClass = type(
    'AnonymousClass',
    (),
    {'greet': lambda self: print("Hi from an anonymous class!")}
)

# Create an instance and use it
obj = AnonymousClass()
obj.greet()
