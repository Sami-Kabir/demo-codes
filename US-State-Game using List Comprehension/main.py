import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(state_list):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        print(missing_states)
        break

    elif answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
        state_list.remove(answer_state)


