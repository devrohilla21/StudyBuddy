import time 
import datetime
import sys
import json

class StudySession: # this class make objects for every session 
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
        self.duration_ = self.end_time - self.start_time
        
    
    def duration(self):
           formated = str(self.duration_).split(".")
           return formated[0]
    
    def to_dict(self):
        dic = {
            "subject" : self.subject,
            "start_time": self.start_time.strftime("%H:%M:%S %d %B %Y"),
            "end_time": self.end_time.strftime("%H:%M:%S %d %B %Y"),
            "duration": str(self.duration_).split(".")[0]
        }
        return dic
 
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
        return total_subs,total_duration
    
    def target_duration(self,target_subject:str):
        
        duration = datetime.timedelta()
        for session in self.session:
            if target_subject == session.subject: 
                duration += session.duration_ 
        return duration
    
    def overwrite_file_save(self):
        data = []
        
        for session in self.session:
            data.append(session.to_dict())
        
        with open("history.json","w") as f:
            json.dump(data,f,indent=4)
            
    def to_load_obj(self):
        try:
            
            with open("history.json","r") as f:
                load = json.load(f)
               
            for rowindict in load:
                data = StudySession(subject=rowindict["subject"])
                    
                data.start_time = datetime.datetime.strptime(rowindict["start_time"],"%H:%M:%S %d %B %Y")
                    
                data.end_time = datetime.datetime.strptime(rowindict["end_time"],"%H:%M:%S %d %B %Y")
                    
                h,m,s = map(int,rowindict["duration"].split(":"))
                data.duration_ = datetime.timedelta(hours=h,minutes=m,seconds=s)

                self.session.append(data)
                
        except FileNotFoundError:
            pass # becz file not even exist so how do we take data and put in self.session()
        except json.decoder.JSONDecodeError:
            pass
            
def show_menu():
    print("----------------------------------------")
    print("| 1. Start New Session                 |")
    print("| 2. View All Sessions Log             |")
    print("| 3. View Subject Total Duration       |")
    print("| 4. View Grand Duration               |")
    print("| 5. Exit                              |")    
    print("----------------------------------------")

# test run that our to_dict method is working or not
# subject = StudySession(subject="english")
# subject.timer_start()
# time.sleep(10)
# subject.timer_stop()
# print(subject.to_dict())


def main():
    tracker = Tracker() #permanent object of Tracker class so we can use it later to call class1 objects
    is_running = True
    tracker.to_load_obj()
    while is_running:
        try:
            show_menu()
            user = int(input("--> Enter 1/2/3/4 to perform task : "))
            if user >5 or user <1:
                raise ValueError
            
        except ValueError:
            print("ERROR REASON: Number Out of Range")
        else:
            a = "."
            sys.stdout.write("Server Message <-- Initializing")
            sys.stdout.flush()
            for _ in range(3):
                sys.stdout.write(f"{a}")
                sys.stdout.flush()
                time.sleep(0.5)
            print()
            
            if user == 1:   
                    print("------------------------------- 1. Add Session Window -------------------------------------")
                    session_name = input("--> Enter Subject name : ").strip().capitalize()
                    if session_name in ["b","back"]:
                        print("Server Message <-- Back Operation Performed")
                        continue
                    session = StudySession(subject=session_name)
                    session.timer_start()
                    input("--> Do anything to stop the session: ")
                    
                    session.timer_stop()
                    
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
                    search = input("--> Enter subject name to view duration : ").strip().capitalize()
                    if search in ["b","back"]:
                        print("Server Message <-- Back Operation Performed")
                        continue
                    back = False
                    while search not in subjects:
                        if search in ["b","back"]:
                            print("Server Message <-- Back Operation Performed")
                            back = True
                            break
                        print(f"Server Message <-- {search} Not found")
                        search = input("--> Enter subject name to view duration : ").strip().capitalize()
                    if back :
                        continue
                    
                    print(f"Session Name : {search}")
                    print(f"Total Duration : {tracker.target_duration(target_subject=search)}")
                    print("x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x----x")
            elif user == 4:
                print("------------------------------- 4. View Grand Duration Window -------------------------------------")
                
                index, duration = tracker.grand_duration()
                print(f"Total Numbers of Session : {index}")
                print(f"Grand Duration of all Session : {str(duration).split('.')[0]}")
                print("-------------------------------------------------------------------------------------------")
                
            else:
                print("THANKS TO RUN THIS PROGRAM")
                is_running = False
                
    if len(tracker.session) != 0:
        tracker.overwrite_file_save()
if __name__ == "__main__":       
    main()  
    
    
    
