"""
task Management app

Create table(
     task_id int primary key auto_increment, 
        title varchar(256), 
        description varchar(256), 
        priority varchar(256), 
        due_date, 
        status varchar(20), 
        created_on datetime
    );

"""
import datetime
class task:
    def __init__(self,task_id=0,title="",description="",priority="",due_date="",status=""):
        self.task_id=task_id
        self.title=title
        self.description=description
        self.priority=priority
        self.due_date=due_date
        self.status=status
        self.created_on = datetime.datetime.now()
    
    def add_task(self):
      self.title = print=input("ENTER TITLE OF YOUR TASK  :)   ")
      self.description=print=input("GIVE DESCRIPTION FOR YOUR TASK :  ")
      self.priority =print=input("Enter the (PRIORITY):-High/Medium/Low  :  " )
      self.due_date=print=input("Enter Due Date of the Created Task (yyyy-mm-dd)  :    " )
      self.status=print=input("Enter status of your task :) (to-do  // in progress // Done):    " )
      
    def update_task_details(self):
        title = input("Enter TITLE: ")
        if len(title) != 0:
            self.title = title

        description = input("Enter  task description: ")
        if len(description) != 0:
            self.description = description

        priority= input("Enter priority : ")
        if len(priority) != 0:
            self.priority = priority
        
        due_date= input("Enter Due Date: ")
        if len(due_date) != 0:
            self.due_date = (due_date)


        status = input("Enter status: ")
        if len(status) != 0:
            self.status = status


    def show(self):
        print("~~~~~~~~~~~~~~Task~~~~~~~~~~~~~~~~~~~~~~~")
        new_task="""{task_id}|{title}|{description}|{priority}
                {due_date}|{status}|{created_on}
        """.format_map(vars(self))
        print(new_task)