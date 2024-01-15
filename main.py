import turtle
import pandas
screen=turtle.Screen()
screen.title("US states guess game")

image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_data=data.state.to_list()
guessed_state=[]


while len(guessed_state)<50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 correct state",prompt="whats the another state name?").title()
    if answer_state=="Exit":
        missing_states=[state for state in all_data if state not in guessed_state ]

        break

    if answer_state in all_data:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


data_=pandas.DataFrame(missing_states)
data_.to_csv("new states")


