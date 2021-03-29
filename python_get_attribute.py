class X:

    def test(self):
        self.suffix = "a"

    def __getattribute__(self, attr):
        try:
            suffix = super().__getattribute__("suffix")
            return getattr(self, f"{attr}__{suffix}")
        except AttributeError:
            return getattr(self, "__dict__")[attr]

    def something_first(self):
        self.context = "a"

    def something__a(self):
        print("something__a")

x = X()
x.something_first()
x.something()
