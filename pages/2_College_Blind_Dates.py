import streamlit as st
import time

st.write("# College Blind Dates")
st.write("## Ready to find awesome colleges you didn't even know existed?")

st.markdown(
"""
Just complete the quiz below, wait a minute, and CollegeGPT will set you up on your first blind date!
"""
)

q1_dict = {"id": 1,
           "question": "What kind of campus are you looking for?",
           "options": ["Cohesive", "Sprawling", "Somewhere in between"]}
q2_dict = {"id": 2,
           "question": "At your ideal college, what are your surroundings like?",
           "options": ["City for sure!", "Cute college town!", "Lots of natural beauty!"]}
q3_dict = {"id": 3,
           "question": "When you're not in class, what do you imagine yourself doing?",
           "options": ["Finding a cozy place to read in the library", "Hanging out with friends", "Participating in (or leading!) a super slay club or team"]}
q4_dict = {"id": 4,
           "question": "What's your #payingforcollege situation? If you're not sure, check out the resources on the Money Honey tab!",
           "options": ["Most schools would give me enough need-based aid to afford it", "Generous schools would give me enough need-based aid to afford it", "I'm chasing merit, baby!", "Money isn't a factor in my decision"]}
q5_dict = {"id": 5,
           "question": "How important is undergraduate research to you?",
           "options": ["Super important! I want to start right away!", "Interested, but I'd be fine with starting research later in college", "Meh...not a must"]}
q6_dict = {"id": 6,
           "question": "How important is study abroad to you?",
           "options": ["Super important!!", "Interested but it's not a make or break", "Not so much"]}
q7_dict = {"id": 7,
           "question": "What's your ideal school size?",
           "options": ["Big school! Over 20,000 students.", "Medium-big school, maybe 10,000 to 20,000 students", "Medium-small, between 5,000 and 10,000 students", "Small for the win! Less than 5,000 students", "Big school with a small school feel"]}

quiz_questions = [q1_dict, q2_dict, q3_dict, q4_dict, q5_dict, q6_dict, q7_dict]


#Text inputs: Major field(s) of study
#Size? Class sizes?

state = st.session_state
if 'counter' not in state:
    state['counter'] = 0
if 'button_label' not in state:
    state['button_label'] = ['START', 'SUBMIT', 'RELOAD']
if 'user_answers' not in state:
    state['user_answers'] = []
if 'start' not in state:
    state['start'] = False
if 'stop' not in state:
    state['stop'] = False
if 'quiz' not in state:
    state['quiz'] = []
if 'q1' not in state:
    state['q1'] = ""
if 'q2' not in state:
    state['q2'] = ""
if 'q3' not in state:
    state['q3'] = ""
if 'q4' not in state:
    state['q4'] = ""
if 'q5' not in state:
    state['q5'] = ""
if 'q6' not in state:
    state['q6'] = ""
if 'q7' not in state:
    state['q7'] = ""

def btn_click():
    state.counter += 1
    if state.counter > 2:
        state.counter = 0
        state.clear()
    else:
        update_session_state()
        with st.spinner("*loading awesomeness*"):
            time.sleep(2)

def update_session_state():
    if state.counter == 1:
        state['start'] = True
        state['quiz'] = quiz_questions
    elif state.counter == 2:
        state['start'] = False
        state['stop'] = True


st.button(label=state.button_label[state.counter], key='button_press', on_click=btn_click)


with st.container():
    q1 = ""
    if(state.start):
        q1 = st.radio(quiz_questions[0]["question"], quiz_questions[0]["options"])
        #st.write(q1)
        
        st.session_state['q1'] = q1

        q2 = st.radio(quiz_questions[1]["question"], quiz_questions[1]["options"])
        #st.write(q2)
        st.session_state['q2'] = q2

        q3 = st.radio(quiz_questions[2]["question"], quiz_questions[2]["options"])
        st.session_state['q3'] = q3

        q4 = st.radio(quiz_questions[3]["question"], quiz_questions[3]["options"])
        st.session_state['q4'] = q4

        q5 = st.radio(quiz_questions[4]["question"], quiz_questions[4]["options"])
        st.session_state['q5'] = q5

        q6 = st.radio(quiz_questions[5]["question"], quiz_questions[5]["options"])
        st.session_state['q6'] = q6

        q7 = st.radio(quiz_questions[6]["question"], quiz_questions[6]["options"])
        st.session_state['q7'] = q7


    if(state.stop):
        st.write(state.get('q1'))
        st.write(state.get('q2'))
        st.write(state.get('q3'))
        st.write(state.get('q4'))
        st.write(state.get('q5'))
        st.write(state.get('q6'))
        st.write(state.get('q7'))
