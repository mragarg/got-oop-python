
# Name
# Avatar (profile picture)

# def do_stuff():
#       pass

class Character():
    
    # Constructor Method
    def __init__(self, new_name, new_avatar):
        # 'self' is similar to 'this' in other languages
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []

    #someone=None is similar to `null` in other langauges
    def greet(self, someone=None):
        if someone:
            return "Hello, %s, I am %s. I am awesome." % (someone.name, self.name)
        else:
            return "Hello, I am %s. I am awesome." % self.name