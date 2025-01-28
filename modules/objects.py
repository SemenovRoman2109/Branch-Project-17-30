class Application():
    def __init__(self, name):
        self.name = name
        self.width = 800
        self.height = 600
    
    def show_name(self):
        print(self.name)

app = Application("app1")