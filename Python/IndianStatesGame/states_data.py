import turtle
import pandas

class StateData:
    def __init__(self):
        self.clicked_states = []
        self.data = None
        self.all_states = []

    def make_data(self):
        self.screen = turtle.Screen()
      
        # ask for file name before clicks
        filename = self.screen.textinput("Filename", "Enter filename (without .csv):")
        self.filename = f"{filename}.csv"
        if filename is None or filename.strip() == "":
            filename = "some_random_name"
        self.filename = f"{filename}.csv"

        self.screen.onscreenclick(self.get_mouse_clicked_coordinates)
        turtle.mainloop()

    def get_mouse_clicked_coordinates(self,x, y):
        state_name = self.screen.textinput("State Name","What's the state name?")

        # 🔸 Fix crash when Cancel is clicked
        if state_name is None:
            return
        state_name = state_name.title()

        if state_name == "Exit":
            df = pandas.DataFrame(self.clicked_states)
            df.to_csv(self.filename, index=False)
            turtle.bye()
        else:
            self.clicked_states.append({"state": state_name, "x": int(x), "y": int(y)})
            print(f"{state_name} added at ({int(x)}, {int(y)})")

    def load_states_data(self, filename="india_states.csv"):
        self.data = pandas.read_csv(filename)
        self.all_states = self.data.states.to_list()

    def get_coordinates(self,state_name):
        row = self.data[self.data.states == state_name]
        if row.empty:
            print(f"State not found in data: {state_name}")
            return None
        x = int(row.x)
        y = int(row.y)
        return x,y
