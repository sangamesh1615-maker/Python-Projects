# My To-do List

A simple to-do list application built with Python and Streamlit. It uses `Task` and `TodoList` classes, a list to hold task objects, and `tasks.json` for file storage. The `TodoList` class includes create, view, update, and delete operations (CRUD).

## Run it

1. Install Python.
2. Open a terminal in this folder and run `pip install -r requirements.txt`.
3. Start the app with `streamlit run app.py`.

Tasks can be added with optional due dates and due times, marked complete, searched, sorted, and deleted. The app shows reminders for tasks due today or overdue. Tasks are saved in `tasks.json` beside `app.py` and remain available after the app is closed.
