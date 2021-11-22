import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# reading the csv file
data = pandas.read_csv('50_states.csv')
states_list = data.state.tolist()
guessed_states = []

# asking the user for input
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state's name")
    answer_state = answer_state.capitalize()

    # plotting the state
    if answer_state in states_list:
        guessed_states.append(answer_state)
        index_value = int(data[data['state'] == answer_state].index.values)
        answer_details = data.iloc[index_value].tolist()
        name_of_state = answer_details[0]
        x_cor = answer_details[1]
        y_cor = answer_details[2]
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(x_cor, y_cor)
        tim.write(name_of_state)
        states_list.remove(answer_state)
    else:
        remaining_states = pandas.DataFrame(states_list)
        remaining_states.to_csv('remaining_states.csv')
        break

turtle.mainloop()
