import turtle
import pandas as pd

# 마우스 클릭한 곳의 x좌표, y좌표 구하기
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./50_states.csv")
all_states = data.state.tolist()
guessed_states = []

letter = turtle.Turtle()
letter.hideturtle()
letter.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        letter.goto(int(state_data.x), int(state_data.y))
        letter.write(answer_state)
        #혹은 letter.write(state_data.state.item())