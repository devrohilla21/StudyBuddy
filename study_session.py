import time 
import datetime


class StudySession:
    def __init__(self, subject: str):
        self.subject = subject
        self.start_time = None 
        self.end_time = None
        self.duration_ = None
        
    def timer_start(self):
        print("Timer Starts")
        self.start_time = datetime.datetime.now()
        self.timer_starts_from = datetime.datetime.now().strftime("%I:%M %p %B %Y")
        
    
    def timer_stop(self):
        print("Timer Stops")
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
        


def main():
    
    tracker = Tracker() #permanent object of Tracker class so we can use it later to call class1 objects
    
    while True:
        session_name = input("Enter Subject name and type 'exit' for exit : ").strip()
        if session_name == "exit":
            break
            
        session_ = StudySession(subject= session_name)
        session_.timer_start()
        while input("Press Enter to stop the time: ") != "":
            pass
        session_.timer_stop()
        
        tracker.add_session(session_)

    for session in tracker.session:
        print(f"Subject name : {session.subject}\n{session.duration()}")
    
    print(tracker.grand_duration())

main()




    
    









