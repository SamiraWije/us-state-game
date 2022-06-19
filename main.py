import turtle
import pandas

# Store correctly guessed states
guessed_states = []

screen = turtle.Screen()
screen.title("U. S. States  Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read states csv
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

while len(guessed_states) < 50:
    # Get user input in title case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Exit the game
    if answer_state == "Exit":
        missing_states = []
        # Check missing guesses and store to new csv
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        dot = turtle.Turtle()
        dot.hideturtle()

        # Read state from 50_states csv
        state_data = data[data.state == answer_state]
        # Read x, y coordinates from 50_states csv
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)

        # Store correctly guessed states
        guessed_states.append(state_data.state.item())

        dot.penup()
        dot.setposition(x_cor, y_cor)
        dot.write(answer_state)

