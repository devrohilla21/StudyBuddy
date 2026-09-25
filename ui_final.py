import streamlit as st
import datetime
import json
from study_session import StudySession, Tracker

# current day
def day():
    hour = datetime.datetime.now().hour
    
    if 5<=hour<12:
        return "Good Morning"
    elif 12<hour<18:
        return "Good Afternoon"
    elif 18<hour<24:
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
st.session_state.name = st.sidebar.text_input("Enter Name",placeholder= "Like Himanshu",value="Dev Rohilla")

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
# menu = st.radio("Choose one:",["Add New Session","View Session Logs","View Subject Duration","View Grand Duration"]) #tabs 

# if st.button("Submit"):  #button for submittion update chocie in every click
#     st.session_state.choice = menu
    
tab1,tab2,tab3,tab4 = st.tabs(["Add New Session","View Session Logs","View Subject Duration","View Grand Duration"])    

with tab1: #1
    st.write("#### Add New Session")
    
    if "is_active" not in st.session_state:
        st.session_state.is_active = False
        
    if not st.session_state.is_active:
        session_name = st.text_input("Session Name",placeholder= "Like English, Physics",disabled=False).strip().capitalize()
    else:
        session_name = st.text_input("Session Name",placeholder= "Like English, Physics",value=st.session_state.obj.subject,disabled=True,).strip().capitalize()

    
    if session_name != "":
        if "pause" not in st.session_state:
            st.session_state.pause = False
            
        if st.session_state.is_active:   
            
            if not st.session_state.pause:
                st.write("Status : Running")
                if st.button("Pause"):
                    st.session_state.pause = True
                    st.session_state.obj.time_pause()
                    st.rerun()
            else:
                st.write("Status : Pause")
                if st.button("Resume"): 
                    st.session_state.pause = False
                    st.session_state.obj.time_resume()
                    st.rerun()

            if st.button("Stop"):
                st.session_state.is_active = False
                st.session_state.pause = False
                st.session_state.obj.timer_stop()
                st .session_state.tracker.add_session(subjectsession=st.session_state.obj)
                del st.session_state.obj
                st.session_state.tracker.overwrite_file_save()
                # st.session_state.result = False
                st.rerun()

        else:
            if not st.session_state.is_active : ## result 
                st.write("Status : Not Started")
                
            if st.button("Start"):
                st.session_state.is_active = True
                st.session_state.obj = StudySession(subject=session_name)
                st.session_state.obj.timer_start()
                # st.session_state.result = True
                st.rerun()
            
    
with tab2: #2
    st.write("#### View Session Logs")
    
    #index permanent variable
    index = 0 
    for session in st.session_state.tracker.session:
        index +=1
        st.write(f"#### Session #{index}")
        st.write(f"1. Session Name : {session.subject}")
        st.write(f"2. Session Start Time : {session.start_time.strftime("%I:%M:%S, %d %B")}")
        st.write(f"3. Session End Time : {session.end_time.strftime("%I:%M:%S, %d %B")}")
        st.write(f"4. Session Duration : {str(session.duration_).split(".")[0]} Approx.")
        
        if len(session.pause_net_time) !=0:
            pause_duraiton = datetime.timedelta()
            st.write(f"5. Pause Status : ")
            for tup in session.pause_net_time:
                start , end = tup 
                pause_duraiton+= end - start
                start = start.strftime("%I:%M:%S %p %d %B")
                end = end.strftime("%I:%M:%S %p %d %B")
                st.write(f"Pause Time : {start}, Resume Time : {end}")
            st.write(f"6. Pause Duration : {str(pause_duraiton).split(".")[0]}")
        else:
            st.write(f"5. Pause Status : None")
            st.write(f"6. Pause Duration : None")
        
    st.write(f"#### Total Session : {index}")

    
with tab3: #3
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
        
with tab4: #4
    st.write("#### View Grand Duration")
    
    index,duration = st.session_state.tracker.grand_duration()
        
    st.write(f"Total Numbers of Session : {index}")
    st.write(f"Grand Duration of all Session : {str(duration).split('.')[0]}")






