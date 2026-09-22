import streamlit as st
import datetime

from study_session import StudySession, Tracker

# current day
def day():
    hour = datetime.datetime.now().hour
    
    if 5<=hour<=12:
        return "Good Morning"
    elif 12<hour<=18:
        return "Good Afternoon"
    elif 18<hour<=24:
        return "Good Evening"
    else:
        return "Late-Night Session"

st.header("Study Buddy Web Application") #1st header

#permanent variables name
if "name" not in st.session_state:
    st.session_state.name = ""
if "choice" not in st.session_state:
    st.session_state.choice = ""
    
#Sidebar for Inputs (name)
st.sidebar.header("Information")
st.session_state.name = st.sidebar.text_input("Enter Name",placeholder= "Like Himanshu")
if st.session_state.name:
    st.subheader(f"{day()}, {st.session_state.name}")

#permanent obj creation for Tracker class (1)
if "tracker" not in st.session_state:
    st.session_state.tracker = Tracker()

if "first_time" not in st.session_state:
    st.session_state.first_time = True
if st.session_state.first_time:
    st.session_state.tracker.to_load_obj() #in each click the entire code get rerun and then it load obj again and again in st.session_state.tracker.sesison
    st.session_state.first_time = False # hahahhah 
    
#main option (menu)
menu = st.radio("Choose one:",["Add New Session","View Session Logs","View Subject Duration","View Grand Duration"])

if st.button("Submit"):  #button for submittion update chocie in every click
    st.session_state.choice = menu
    
if st.session_state.choice == "Add New Session": #1
    st.write("#### Add New Session")
    
    if "notdisable" not in st.session_state:
        st.session_state.notdisable = True
    
    if st.session_state.notdisable:
        session_name = st.text_input("Session Name",placeholder= "Like English, Physics",disabled=False).strip().capitalize()
    
    else:
        session_name = st.text_input("Session Name",placeholder= "Like English, Physics",disabled=True).strip().capitalize()
        
    if session_name != "": 
        
        if 'result' not in st.session_state:        
            st.session_state.result = True
            
        if not st.session_state.result:
            if "obj" not in st.session_state:
                st.session_state.obj = StudySession(subject=session_name)
            else:
                st.session_state.obj.subject = session_name
        
        

        ### temp code 

        if "is_active" not in st.session_state:
            st.session_state.is_active = False
    

        if st.session_state.is_active:
            st.write("Status : Running ")
            if st.button("Stop"):
                st.session_state.is_active = False
                st.session_state.obj.timer_stop()
                st .session_state.tracker.add_session(subjectsession=st.session_state.obj)
                del st.session_state.obj
                st.session_state.tracker.overwrite_file_save()
                st.session_state.result = False
                st.session_state.notdisable = True
                st.rerun()

        else:
            if st.session_state.result :
                st.write("Status : Not Started")
            else:
                st.write("Status : Stopped")
            if st.button("Start"):
                st.session_state.is_active = True
                st.session_state.obj = StudySession(subject=session_name)
                st.session_state.obj.timer_start()
                st.session_state.result = True
                st.session_state.notdisable = False
                st.rerun()
            
        
        ### temp code 
        
        # if st.button("START"):
        #     st.session_state.obj.timer_start()
        #     st.session_state.result = "start"
        # try:
        #     if st.button("STOP"):
        #         st.session_state.obj.timer_stop()
        #         st.session_state.result = "stop"
        # except TypeError:
        #     st.write("Session Not Started Yet")
            
        # if st.session_state.result == "start":
        #     st.write(f"Status : {st.session_state.result}")
        
        # elif st.session_state.result == "stop":
        #     st.write(f"Status : {st.session_state.result}")
        #     st.session_state.tracker.add_session(subjectsession=st.session_state.obj)
        #     del st.session_state.obj
        #     st.session_state.tracker.overwrite_file_save()
elif st.session_state.choice == "View Session Logs": #2
    st.write("#### View Session Logs")
    
    #index permanent variable
    index = 0 
    for session in st.session_state.tracker.session:
        index +=1
        st.write(f"#### Session #{index}")
        st.write(f"Session Name : {session.subject}")
        st.write(f"Session Start Time : {session.start_time.strftime("%H:%M:%S, %d %B")}")
        st.write(f"Session End Time : {session.end_time.strftime("%H:%M:%S, %d %B")}")
        st.write(f"Session Duration : {str(session.duration_).split(".")[0]} Approx.")
    
    st.write(f"#### Total Session : {index}")

    
elif st.session_state.choice == "View Subject Duration": #3
    st.write("#### View Subject Duration")
    
    subject = []
    st.session_state.index = 0
    for idx,session in enumerate(st.session_state.tracker.session):
        if session.subject not in subject:
            subject.append(session.subject)
            st.session_state.index +=1
    search1 = st.selectbox("Total Subjects : ",subject)
    
    st.write("#### Subject Total Duraiton")
    st.write(f"Subject Name : {search1}")
    st.write(f"Total Duration : {str(st.session_state.tracker.target_duration(target_subject=search1)).split('.')[0]} Approx.")
        
elif st.session_state.choice == "View Grand Duration": #4
    st.write("#### View Grand Duration")
    
    index,duration = st.session_state.tracker.grand_duration()
        
    st.write(f"Total Numbers of Session : {index}")
    st.write(f"Grand Duration of all Session : {str(duration).split('.')[0]}")






