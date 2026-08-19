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

#for object creation 
# subject = StudySession(subject= "Math")

# subject.timer_start()
# while input("Press Enter When to stop : ") != "":
#     pass
# subject.timer_stop()
# print()
# print(subject.duration())
# print()
# print(subject.print_start_and_stop_time())

class Tracker:
    def __init__(self):
        self.session = []
    
    def add_session(self,subjectsession):
        self.session.append(subjectsession)
        
tracker = Tracker() #permanent object of Tracker class so we can use it later to call class1 objects

is_running = True
while is_running:
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
    
    
    













       
# s1 = StudySession("Math")
# s1.timer_start()
# while input("Press Enter to stop the time: ") != "":
#     pass
# s1.timer_stop()

# s2 = StudySession("Physics")
# s2.timer_start()
# while input("Press Enter to stop the time: ") != "":
#     pass
# s2.timer_stop()

# tracker = Tracker()
# tracker.add_session(s1)
# tracker.add_session(s2)
    
# for session in tracker.session:
#     print(f"s_name = {session.subject}, duration = {session.duration()}")









