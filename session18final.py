from session18taskpp import task
from session18remarks import remarks
from session16A import Database
from tabulate import tabulate

def main():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::") 
    print("::::::::::::::::: TASK MANAGEMENT APP ::::::::::::::::::::::::::::::::::::")
    print("~~~~~~~~~~~~~~~~~~~~~~~    :)   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    db = Database()
    
    while True:
        print("1: Create a task:")
        print("2: Update task:")
        print("3: Delete task:")
        print("4: To display task list by priority:")
        print("5: View List of Task by task_id:")
        print("6: View List of Task by Due Date:")
        print("7: To Add REMARKS:")
        print("8: To Update Remarks")
        print("9: To Delete REMARKS")
        print("10: To View Remarks by Task_id")
        print("11: To View All TASK :)")
        print("12: To View All Remarks")
        print("0: To Quit TASK MANAGEMENT APP :) ")

        choice = int(input("ENTER YOUR CHOICE: "))
        
        if choice == 1:
            new_task = task()  
            new_task.add_task()  
            sql = "insert into task values (null, '{title}', '{description}', '{priority}', '{due_date}', '{status}', '{created_on}')".format_map(vars(new_task))
            db.write(sql)
            print("TASK CREATED :)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            
        
        elif choice == 2:
            task_id = int(input("Enter TASK ID to Update: "))
            sql = "select * from task where task_id = {}".format(task_id)
            rows = db.read(sql)
            print(rows)
            
            new_task = task(task_id=rows[0][0], title=rows[0][1], description=rows[0][2], priority=rows[0][3], due_date=rows[0][4], status=rows[0][5])

            print("Patient to Update:")
            new_task.show()
            new_task.update_task_details()

            sql = "update task set title = '{title}', description='{description}', priority='{priority}', due_date='{due_date}', status='{status}', created_on='{created_on}' ".format_map(vars(new_task))

            db.write(sql)

            new_task.show()
        
        elif choice == 3:
            task_id = int(input("Enter TASK ID to be Deleted: "))
            sql = "delete from patient where task_id = {}".format(task_id)

            ask = input("Are you sure to delete? (yes/no): ")
            if ask == "yes":
                db.write(sql)
                print("[TASK MANAGEMENT App]", task_id, "Deleted from DataBase")
            else:
                print("Delete Operation Skipped")
        
        elif choice == 4:
            priority = input("Enter TASK PRIORITY ")
            sql = "select * from task where priority = '{}'".format(priority)
            rows = db.read(sql)
            columns = ["task_id", "title", "description", "priority", "due_date", "status", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            
        elif choice == 5:
            task_id = input("Enter TASK ID: ")
            sql = "select * from task where task_id = '{}'".format(task_id)
            rows = db.read(sql)
            columns = ["task_id", "title", "description", "priority", "due_date", "status", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            
            
        
        elif choice == 6:
            due_date = input("Enter Due Date: ")
            sql = "select * from task where due_date = '{}'".format(due_date)
            rows = db.read(sql)
            columns = ["task_id", "title", "description", "priority", "due_date", "status", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            
        
        elif choice == 7:
            new_remarks = remarks()  
            new_remarks.add_remarks() 
            sql = "insert into remarks values (null, {task_id}, '{remarked_by}', '{remarked_to}', '{remarks}', '{created_on}')".format_map(vars(new_remarks))
            db.write(sql)
            print("REMARK CREATED :)")
            
        elif choice == 8:
            remark_id = int(input("Enter REMARK ID to Update: "))
            sql = "select * from remarks where remark_id = {}".format(remark_id)
            rows = db.read(sql)
            print(rows)
            
            new_remarks = task(remark_id=rows[0][0], remarked_by=rows[0][1], remarked_to=rows[0][2], remarks=rows[0][3])

            print("Remark to Update:")
            new_remarks.show()
            new_remarks.update_remark_details()

            sql = "update task set remarked_by = '{remarked_by}', remarked_to='{remarked_to}', remarks='{remarks}', created_on='{created_on}' ".format_map(vars(new_remarks))

            db.write(sql)

            new_remarks.show()
        
        elif choice == 9:
            remark_id = int(input("Enter REMARK ID to be Deleted: "))
            sql = "delete from remarks where remark_id = {}".format(remark_id)

            ask = input("Are you sure to delete? (yes/no): ")
            if ask == "yes":
                db.write(sql)
                print("[TASK MANAGEMENT App]", remark_id, "Deleted from DataBase")
            else:
                print("Delete Operation Skipped")
        
        
        elif choice == 10:
            task_id = input("Enter TASK ID: ")
            sql = "select * from remarks where task_id = '{}'".format(task_id)
            rows = db.read(sql)
            columns = ["remark_id","task_id","remarked_by","remarked_to","remarks", "created_on"]
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        elif choice == 11:
            sql = "select * from task"
            rows = db.read(sql)

            columns = ["task_id", "title", "description", "priority", "due_date", "status", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        elif choice == 12:
            sql = "select * from remarks"
            rows = db.read(sql)

            columns = ["remark_id","task_id","remarked_by","remarked_to","remarks", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        
        elif choice == 0:
            break
        
        else:
            print("INVALID CHOICE")

if __name__ == "__main__":
    main()
