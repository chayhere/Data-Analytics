import turtle

class ScreenManager:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Name the States")
        self.screen.setup(width=725, height=846)
        self.screen.bgpic("india_map.gif")
        self.title = "Guess the State"
        self.prompt = "  Name the States you know: "
        self.score = 0

    def get_screen(self):
        return self.screen

    def get_user_input(self):
        return self.screen.textinput(title=self.title, prompt=self.prompt)

    def change_title(self):
        self.prompt = "    Keep going — next state: "
        return self.screen.textinput(title=f"{self.score}/28 States Correct",prompt=self.prompt)
