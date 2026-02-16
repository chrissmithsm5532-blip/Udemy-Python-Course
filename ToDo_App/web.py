import streamlit as st
import functions

def add_todo():
    n_todo = st.session_state["new_todo"]
    todos.append(n_todo+'\n')
    functions.write_todos(todos)



st.title('My ToDo App')
st.subheader("This is my ToDo app")
st.write("This app is to increase your productivity")

todos =functions.get_todos()



for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input("",placeholder="Enter a todo",on_change=add_todo,key="new_todo")

st.session_state

