class Application():
    def __init__(self, name):
        self.name = name
        self.width = 800
        self.height = 600
    
    def show_name(self):
        print(self.name)
    def show_info(self):
        print(self.width,self.height)

app = Application("app1")