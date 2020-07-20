from datetime import datetime,timedelta
from job_sche_bst import Node,BST

def get_job_input_details():
    start_time = input("Enter the starting time of the job in hh:mm format ex:21:00 or 6:30 ->")
    while True:
        try:
            datetime.strptime(start_time,"%H:%M")
        except ValueError:
            print("Incorrect time format. Please enter again")
            start_time = input("Enter the starting time in hh:mm format ->")
        else:
            break
    duration = input("Enter the duration of job in minutes ex 30 or 5 ->")
    while True:
        try:
            int(duration)
        except ValueError:
            print("Incorrect format entered. Please enter again")
            duration = input("Enter the duration of job in minutes")
        else:
            break
    name_of_job = input("Enter the name of the job(case sensitive) ->")
    return start_time,duration,name_of_job

tree = BST()

with open("data.txt") as f:
    for line in f:
        tree.insert(line)

while True:
    print("-"*60)
    print("Enter 1 to view the job schedule")
    print("Enter 2 to enter a new job")
    print("Enter 3 to remove a job")
    print("Enter 4 to exit")
    choice = input("Select a number from above options")
    print("-"*60)
    try:
        entry = int(choice)
    except ValueError:
        print("Please enter a valid number")
        continue
    if int(choice) == 1:
        tree.in_order()
    elif int(choice) == 2:
        print("You have chosen to add a job to the schedule")
        sch_time, duration, name_of_job = get_job_input_details()
        new_entry = sch_time+","+duration+","+name_of_job
        num = tree.length()
        tree.insert(new_entry)
        if num == tree.length() - 1:
            with open("data.txt", "a+") as f:
                f.write(new_entry+"\n")
        input("Enter any key to continue ->")
    elif int(choice) == 3:
        print("You have chosen to remove a job from the schedule")
        sch_time, duration, name_of_job = get_job_input_details()
        key = datetime.strptime(sch_time,"%H:%M")
        result = tree.find_val(key)
        if result:
            if result.name_of_job == name_of_job and result.duration == duration:
                print(f"Deleting the job: {name_of_job}...")
                tree.delete_val(key)
                print("Job successfully deleted")
                with open("data.txt","r") as f:
                    lines = f.readlines()
                with open("data.txt","w") as f:
                    for line in lines:
                        if line.strip("\n") != sch_time+","+duration+","+name_of_job:
                            f.write(line)
                input("Press any key to continue")
            else:
                print("The name and/or duration of the match dont match")
                input("Enter any key to continue")
        else:
            print("The given starting time does not match with any job")
            input("Enter any key to continue")
    elif int(choice) == 4:
        print("Exiting program...")
        break
    else:
        print("Please enter a number between 1 and 4")
