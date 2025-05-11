def greetMorning(func):
    def wrapper():
        print("It's a sunny day!")
        func()
    return wrapper

@greetMorning
def sayHello():
    print("Hello ")


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles~")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge~")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
def test():
    print("test")

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream!")
    
get_ice_cream("Vanilla")
get_ice_cream("Chocolate")
# test()