from tasks_utils import create_update

def scheduled_task_run():
    check_task_execution()
    create_update()

def check_task_execution():
    with open("test_hesam.txt","w") as writer:
        writer.write("it executed write")



