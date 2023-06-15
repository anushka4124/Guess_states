import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("Indian States")
image="states_map.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("states.csv")
all_states=list(data["state"])
all_capitals=data["capital"].tolist()
not_guessed=all_states
c=0
for i in range(1,30):

    orig_st=turtle.textinput(title=f"Score:{c}/29",prompt="Guess the state")
    new_st=orig_st.title()
    print(new_st)
    if new_st=="Exit":
        break
    if new_st in all_states:
        not_guessed.remove(new_st)
        c+=1
        t = turtle.Turtle()
        t.hideturtle()
        a = data[data.state==new_st]
        print(type(a.x))
        t.penup()
        t.goto(int(a.x),int(a.y))
        t.write(new_st)


missing_states=pd.DataFrame(not_guessed)
missing_states.to_csv("Missing_states.csv")
print(missing_states)
