import time 
import datetime
import sys


class StudySession:
    def __init__(self, subject: str):
        self.subject = subject
        self.start_time = None 
        self.end_time = None
        self.duration_ = None
        
    def timer_start(self):
        print("Server Message <--  Timer Starts")
        self.start_time = datetime.datetime.now()
        
    
    def timer_stop(self):
        print("Server Message <-- Timer Stops")
        self.end_time = datetime.datetime.now()
        
        
    
    def print_start_and_stop_time(self):
        return f"Start Time: {self.start_time.strftime("%I:%M %p %B %Y")}\nEnd Time: {self.end_time.strftime("%I:%M %p %B %Y")}"
    
    def duration(self):
           self.duration_ = self.end_time - self.start_time
           formated = str(self.duration_).split(".")
           return f"Total Duration: {formated[0]}"


class Tracker:
    def __init__(self):
        self.session = []
    
    def add_session(self,subjectsession):
        self.session.append(subjectsession)
        
    def grand_duration(self):
        total_duration = datetime.timedelta()
        total_subs = 0
        for session in self.session:
            total_duration += session.duration_
            total_subs += 1   
        return f"Grand Duration of all {total_subs} Subjects: {str(total_duration).split('.')[0]}"
    
    def target_duration(self,target_subject:str):
        
        duration = datetime.timedelta()
        for session in self.session:
            if target_subject == session.subject: 
                duration += session.duration_ 
        return f"Total duration of {target_subject} subject : {str(duration).split('.')[0]}"
    
def show_menu():
    print("-------------------------------------")
    print("| 1. Start new session              |")
    print("| 2. View all sessions log          |")
    print("| 3. View subject total duration    |")
    print("| 4. Exit                           |")    
    print("-------------------------------------")



def main():
    tracker = Tracker() #permanent object of Tracker class so we can use it later to call class1 objects
    is_running = True
    while is_running:
        try:
            show_menu()
            user = int(input("--> Enter 1/2/3/4 to perform task : "))
            if user >4 or user <1:
                raise ValueError
            
        except ValueError:
            print("ERROR REASON: Enter a number Between 1 to 4")
        else:
            a = "."
            sys.stdout.write("Server Message <-- Initializing")
            sys.stdout.flush()
            for i in range(3):
                sys.stdout.write(f"{a}")
                sys.stdout.flush()
                time.sleep(0.5)
            print()
            
            if user == 1:   
                    print("------------------------------- 1. Add Session Window -------------------------------------")
                    session_name = input("--> Enter Subject name : ").strip().lower()
                    session = StudySession(subject=session_name)
                    session.timer_start()
                    input("--> Do anything to stop the session: ")
                    
                    session.timer_stop()
                    session.duration()
                    
                    #adding obj of class 1 into class2 
                    tracker.add_session(subjectsession=session)
                    print("x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x")
                    continue
            elif user == 2:
                if tracker.session == []:
                    print("Server Message <-- Session is Empty")
                    continue
                else:
                    print("-------------------------- 2. View all Session log Window ---------------------------------")
                    session_index = 0
                    for session in tracker.session:
                        session_index+=1
                        print(f"Session #{session_index} ")
                        print(f"Subject Name: {session.subject.capitalize()}, Start Time: {session.start_time.strftime('%I:%M %p')}, End Time: {session.end_time.strftime('%I:%M %p')},Total Duration: {session.duration()} Approx.\n")
                    print(f"TOTAL SESSION : {session_index}")
                    print("x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x")
            elif user == 3:
                
                if tracker.session == []:
                    print("Server Message <-- You didnt Study Yet")
                
                else:
                    print("--------------------------- 3. View Subject Duration Window -----------------------------------")
                    subjects = []
                    sys.stdout.write("Total Subjects : ")
                    sys.stdout.flush()
                    for sub in tracker.session:
                        if sub.subject not in subjects:
                            subjects.append(sub.subject)
                            sys.stdout.write(f"{sub.subject}, ")
                            sys.stdout.flush()
                            
                    print()        
                    search = input("--> Enter subject name to view duration : ").strip().lower()
                    while search not in subjects:
                        print(f"Server Message <-- {search} Not found")
                        search = input("--> Enter subject name to view duration : ").strip().lower()
                    
                    print(tracker.target_duration(target_subject=search))
                    print("x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x")
            else:
                print("THANKS TO RUN THIS PROGRAM")
                is_running = False
       
main()  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     while True:
#         session_name = input("Enter Subject name and type 'exit' for exit : ").strip()
#         if session_name == "exit":
#             break
            
#         session_ = StudySession(subject= session_name)
#         session_.timer_start()
#         while input("Press Enter to stop the time: ") != "":
#             pass
#         session_.timer_stop()
        
#         tracker.add_session(session_)

#     for session in tracker.session:
#         print(f"Subject name : {session.subject}\n{session.duration()} approx")
    
#     print(tracker.grand_duration())

#     print(tracker.target_duration(target_subject="english"))
# main()




    
    









