class Parent(object):

    def store(self):
        print("Parent store")
        self.method()

    def method(self):
        print("Parent method")
    
class Child(Parent):
    def method(self):
        print("Child method")

    def store(self):
        print("Child store")
        super(Child, self).store()


Child().store()

