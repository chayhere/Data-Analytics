import turtle
from states_data import StateData
from screen_manager import ScreenManager

screen_manager = ScreenManager()
screen = screen_manager.get_screen()
state_data = StateData()

# 👇🏼Only run this once to make data, then comment it
# state_data.make_data()

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()

state_data.load_states_data()
game_is_on = True

guessed_states = []

while game_is_on:
    if screen_manager.score == 28:
        game_is_on = False

    if screen_manager.score == 0:
        answer_state = screen_manager.get_user_input()
    else:
        answer_state = screen_manager.change_title()

    if not answer_state or answer_state.strip() == "":
        continue

    answer_state = answer_state.strip().title()

    if answer_state == "Quit":
        for state in state_data.all_states:
            if state not in guessed_states:
                x, y = state_data.get_coordinates(state)
                timmy.goto(x, y)
                timmy.write(state, align="left", font=("Arial", 12, "normal"))
        game_is_on = False

    if answer_state in state_data.all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        screen_manager.score += 1
        print(answer_state)
        coords = state_data.get_coordinates(answer_state)
        timmy.goto(coords)
        timmy.write(arg=answer_state, align="left", font=("Arial", 12, "normal"))

turtle.mainloop()
