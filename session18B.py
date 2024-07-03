from session18 import Patient
from session18A import Consultation
from session16A import Database
from tabulate import tabulate 

def main():
    print("=======================")   
    print("Welcome to Doctor's App")
    print("=======================")

    db = Database()

    while True:
        print("1: Add New Patient")
        print("2: Update Existing Patient")
        print("3: Delete Existing Patient")
        print("4: View Patient By Phone")
        print("5: View Patient By PID")
        print("6: View All Patients")
        print("7: Add Consultation For Patient")
        print("8: View All Consultations")
        print("9: View Consultations of a Patient")
        print("10: View FollowUps")
        print("0: To Quit App")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "insert into Patient values(null, '{name}', '{phone}', '{email}', '{dob}', '{gender}', '{created_on}')".format_map(vars(patient))
            db.write(sql)
            print("Patient Created..")
        elif choice == 2:
            pid = int(input("Enter Patient ID to Update: "))
            sql = "select * from Patient where pid = {}".format(pid)
            rows = db.read(sql)
            print(rows)
            
            patient = Patient(pid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3], dob=rows[0][4], gender=rows[0][5])

            print("Patient to Update:")
            patient.show()
            patient.update_patient_details()

            sql = "update Patient set name = '{name}', phone='{phone}', email='{email}', dob='{dob}', gender='{gender}', created_on='{created_on}' ".format_map(vars(patient))

            db.write(sql)

            patient.show()
        elif choice == 3:
            pid = int(input("Enter Patient ID to be Deleted: "))
            sql = "delete from patient where pid = {}".format(pid)

            ask = input("Are you sure to delete? (yes/no): ")
            if ask == "yes":
                db.write(sql)
                print("[Doctor's App]", pid, "Deleted from DataBase")
            else:
                print("Delete Operation Skipped")

        elif choice == 4:
            phone = input("Enter Patients Phone Number: ")
            sql = "select * from patient where phone = '{}'".format(phone)
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 5:
            pid = int(input("Enter Patient ID: "))
            sql = "select * from patient where pid = {}".format(pid)
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
        
        elif choice == 6:
            sql = "select * from Patient"
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 7:
            consultation = Consultation()
            consultation.add_connsulation_details()
            sql = "insert into Consultation values(null, {pid}, '{remarks}', '{medicines}', '{next_followup}', '{created_on}')".format_map(vars(consultation))
            db.write(sql)
            print("Consultation Created..")


        elif choice == 8:
            sql = "select * from Consultation"
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicines", "next_followup", "created_on"]  
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 9:
            pid = int(input("Enter Patient ID: "))
            sql = "select * from Consultation where pid = {}".format(pid)
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicines", "next_followup", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))         

        elif choice == 10:
            start_date = input("Enter Start Date Time(yyyy-mm-dd hh:mm:ss): ")
            end_date = input("Enter End Date Time(yyyy-mm-dd hh:mm:ss): ")
            
            sql = "select * from Consultation where next_followup >= '{}' and next_followup <= '{}'".format(start_date, end_date)
            rows = db.read(sql)

            columns = ["cid", "pid", "remarks", "medicines", "next_followup", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))     

        elif choice == 0:
            break
        else:
            print("Inavlid Choice")


if __name__ == "__main__":
    main()