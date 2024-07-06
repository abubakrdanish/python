import streamlit as st

import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a todo app")
st.write("This app is to increase your productivity.")

# Display existing todos
for todo in todos:
    st.checkbox(todo)

# Input for adding a new todo
st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
