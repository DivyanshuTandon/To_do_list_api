from app import db ,Task
#from app.models import Task

# create a new task object
new_task = Task(title="Go for a run", description="Run for 30 minutes")

# add the task to the database
db.session.add(new_task)
db.session.commit()
