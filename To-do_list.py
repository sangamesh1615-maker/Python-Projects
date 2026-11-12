import streamlit as st
from datetime import date, time, timedelta

st.set_page_config(page_title="My To-do List", page_icon="✅")
st.title("✅ My To-do List")

# Store tasks in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

tasks = st.session_state.tasks

# Add task
with st.form("add_task"):
    text = st.text_input("New task")
    due = st.date_input("Due date", value=None)
    due_time = st.time_input(
    "Due time",
    value=time(9, 0),
    step=timedelta(minutes=1)
)

    if st.form_submit_button("Add task"):
        if text.strip():
            tasks.append({
                "text": text.strip(),
                "due": due,
                "time": due_time,
                "done": False
            })
            st.rerun()
        else:
            st.warning("Please enter a task.")

# Reminders
today = date.today()

for task in tasks:
    if not task["done"] and task["due"] == today:
        st.info(f"Due today: {task['text']}")

    elif not task["done"] and task["due"] < today:
        st.warning(f"Overdue: {task['text']}")

# Search and sort
st.subheader("Your tasks")

search = st.text_input("Search tasks")

sort = st.selectbox(
    "Sort by",
    ["Due date", "Task name", "Status"]
)

filtered = [
    task for task in tasks
    if search.lower() in task["text"].lower()
]

if sort == "Due date":
    filtered.sort(key=lambda x: x["due"])

elif sort == "Task name":
    filtered.sort(key=lambda x: x["text"].lower())
    
else:
    filtered.sort(key=lambda x: x["done"])

# Display tasks
for i, task in enumerate(filtered):
    col1, col2, col3 = st.columns([1, 5, 1])

    done = col1.checkbox(
        "Done",
        value=task["done"],
        key=f"task_{tasks.index(task)}"
    )

    if done != task["done"]:
        task["done"] = done
        st.rerun()

    col2.write(task["text"])

    if col3.button("Delete", key=f"delete_{tasks.index(task)}"):
        tasks.remove(task)
        st.rerun()