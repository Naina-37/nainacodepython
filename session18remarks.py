""" create table remarks(
        remark_id int primary key auto_increment, 
        task_id int, 
        remarked_by varchar(256), 
        remarked_to varchar(256), 
        remarks varchar(256), 
        created_on datetime,
        FOREIGN KEY (task_id) REFERENCES task(task_id)
    );
"""
import datetime
class remarks:
    def __init__(self,remark_id=0,task_id=0,remarked_by="",remarked_to="",remarks=""):
        self.remark_id=remark_id
        self.task_id=task_id
        self.remarked_by=remarked_by
        self.remarked_to=remarked_to
        self.remarks=remarks
        self.created_on=datetime.datetime.now()
    def add_remarks(self):
        self.task_id = input("Enter TASK ID: ")
        self.remarked_by=input("Enter Manager name who remarked the task")
        self.remarked_to=input("Enter name to who's task remark was given")
        self.remarks=input("Enter remarks :)      ")
    def update_remark_details(self):
        remarked_by = input("Enter REMARKED BY: ")
        if len(remarked_by) != 0:
            self.remarked_by = remarked_by

        remarked_to = input("Enter Remarked to: ")
        if len(remarked_to) != 0:
            self.remarked_to = remarked_to

        remarks= input("Enter Remarks : ")
        if len(remarks) != 0:
            self.remarks = remarks
        
            
    def show(self):
        print("~~~~~~~~~~~REMARKS~~~~~~~~~~~~~~~~~~")
        new_remarks="""{remark_id}|{task_id}|{remarked_by}|{remarked_to}|{remarks}
                   {created_on}
        """.format_map(vars(self))
        print(new_remarks)