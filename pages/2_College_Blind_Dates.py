import streamlit as st
import time
from openai import OpenAI
client = OpenAI()

st.write("# College Blind Dates")
st.write("## Ready to find awesome colleges you didn't even know existed?")

st.markdown(
"""
Just complete the quiz below, wait a minute, and CollegeGPT will set you up on your first blind date!
Attribution: CollegeGPT is powered by the OpenAI GPT-3.5 Turbo model, with prompt engineering by Holland Henderson-Boyer.
"""
)

q1_dict = {"id": 1,
           "question": "What kind of campus are you looking for?",
           "options": ["Cohesive", "Sprawling", "Unique"]}
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
           "options": ["Super important", "Interesting, but I'd be fine with starting research later in college", "Meh...not a must"]}
q6_dict = {"id": 6,
           "question": "How important is study abroad to you?",
           "options": ["Super important", "Interested but it's not a make or break", "Not so much"]}
q7_dict = {"id": 7,
           "question": "What's your ideal school size?",
           "options": ["Over 20,000 students", "10,000 to 20,000 students", "5,000 to 10,000 students", "Less than 5,000 students"]}

quiz_questions = [q1_dict, q2_dict, q3_dict, q4_dict, q5_dict, q6_dict, q7_dict]


#Text inputs: Major field(s) of study
#Size? Class sizes?

state = st.session_state
if 'counter' not in state:
    state['counter'] = 0
if 'button_label' not in state:
    state['button_label'] = ['START', 'SUBMIT', 'SUBMIT', 'SUBMIT']
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
if 'curr_input' not in state:
    state['curr_input'] = ""
if 'text_field' not in state:
    state['text_field'] = False
if 'num_llm_turns' not in state:
    state['num_llm_turns'] = 0

def btn_click():
    state.counter += 1
    if state.counter > 2:
        state.counter = 0
        state.clear()
    else:
        update_session_state()
        with st.spinner("*loading awesomeness*"):
            time.sleep(2)

def text_field_btn_click():
    state.counter = 3
    update_session_state()
    with st.spinner("*loading more awesomeness*"):
        time.sleep(2)


def update_session_state():
    if state.counter == 1:
        state['start'] = True
        state['text_field'] = False
        state['quiz'] = quiz_questions
    elif state.counter == 2:
        state['start'] = False
        state['stop'] = True
        state['text_field'] = False
    elif state.counter == 3:
        state['text_field'] = True


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
        #st.write(state.get('q1'))
        #st.write(state.get('q2'))
        #st.write(state.get('q3'))
        #st.write(state.get('q4'))
        #st.write(state.get('q5'))
        #st.write(state.get('q6'))
        #st.write(state.get('q7'))

        campus_type = state.get('q1')
        urban_rural = state.get('q2')
        hobbies = state.get('q3')
        financial_sitch = state.get('q4')
        research_importance = state.get('q5')
        study_abroad_importance = state.get('q6')
        size_pref = state.get('q7')


        chat_history=[
        {"role": "system", "content": "You are a counselor who helps high school students find their best-fit colleges. A student tells you what they want in a college, including scholarship opportunities, extracurriculars, student-to-faculty ratio, and other factors. You respond with a college that you think meet most or all of their criteria, and explain why you think that school might be a good fit. The catch is that you DON'T reveal the name of the school, and you never suggest schools with acceptance rates below 20%. Your objective is to help students discover schools that may not have been on their radar before."},
        #{"role": "SYSTEM", "message": "The student's prompt will be sent in multiple parts. Don't respond until you see the full prompt, indicated by 'this is the end of the prompt.'"}
        #{"role": "SYSTEM", "message": "Remember, you want students to keep an open mind, so don't give the name of the school until at least 2 follow-up questions have been asked! Also, don't mention the school's ranking or acceptance rate."}
        ]

        max_turns = 10

        message = "Hi! I'm a high school student looking to find a great college that isn't currently on my radar. I enjoy " + hobbies.lower() + " and I'm looking for a school with a " + campus_type.lower() + " campus. I'm looking for a school with a student body of " + size_pref + "."
        if financial_sitch == "Most schools would give me enough need-based aid to afford it":
            message += "Financial aid is a big factor in my college decision; I'm looking for a school that would give me enough need-based and/or merit-based aid to afford it. I'm generally eligible for the maximum amount of need-based aid schools offer."
        elif financial_sitch == "Generous schools would give me enough need-based aid to afford it":
            message += "Financial aid is a big factor in my college decision; I'm looking for a school that would give me enough need-based or merit-based aid to afford it. I'm generally eligible for partial need-based scholarships; only a few schools would allow me to afford attendance with need-based aid alone."
        elif financial_sitch == "I'm chasing merit, baby!":
            message += "Money is a big factor in my college decision; I'm looking for a school that would give me enough merit-based aid to afford it. I'm not eligible for any significant amount of need-based aid."
        else:
            message += "Money isn't a factor in my college decision; I'm looking for a school that's a great fit for me academically and socially, regardless of cost."
        
        if research_importance == "Super important":
            message += "I'm looking for a school that has a strong undergraduate research program. I'm interested in getting involved in research as early as possible in my college career."
        elif research_importance == "Interesting, but I'd be fine with starting research later in college":
            message += "I'm interested in undergraduate research, but it's not a make or break factor in my college decision. I'm open to starting research later in my college career."
        else:
            message += "I'm not particularly interested in undergraduate research; I'm looking for a school that has a strong academic program and a vibrant campus life."
        
        if study_abroad_importance == "Super important":
            message += "I'm looking for a school that has a strong study abroad program. I see study abroad as an important part of my college journey."
        elif study_abroad_importance == "Interested but it's not a make or break":
            message += "I'm interested in studying abroad, but it's not a make or break factor in my college decision."
        else:
            message += "I'm not particularly interested in studying abroad; I'm looking for a school that has a strong academic program and a vibrant campus life."

        message += "Please recommend a college I'm not likely to be familiar with based on these factors. When you give me my recommendation, I want it to be like a blind date--don't tell me the name of the school! Call it School X or a similar pseudonym, and give me a summary of why you think it's a good fit."

        #st.write(message)

        #response = co.chat(
        #        chat_history=chat_history,
        #        message=message,
        #        connectors=[{"id": "web-search"}]
        #)

        print(message)
        message_dict = {"role": "user", "content": message}
        chat_history.append(message_dict)

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= chat_history
        )

        answer = response.choices[0].message.content
        print(answer)
        st.write("CollegeGPT: " + answer)

        user_message = {"role": "user", "content": message}
        bot_message = {"role": "assistant", "content": answer}
            
        chat_history.append(user_message)
        chat_history.append(bot_message)

     
            # get user input

        message = st.text_area("Talk to me about colleges: ")
        #st.write(q1)
        st.session_state['curr_input'] = message

        st.button(label=state.button_label[state.counter], key='button_press_2', on_click=text_field_btn_click)

        if state.text_field:
            state.num_llm_turns += 1
            if state.num_llm_turns <= 2:
                message += "Remember, don't tell me the name of the school! Use School X or a similar pseudonym."
            else:
                message += "You can tell me the name of the school now, but first give me a summary of all the information we've discussed so far."
            
            # generate a response with the current chat history
            #response = co.chat(
            #    chat_history=chat_history,
            #    message=message,
            #    connectors=[{"id": "web-search"}]
            #)
                
            message_dict = {"role": "user", "content": message}
            chat_history.append(message_dict)

            response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages= chat_history
            )

            answer = response.choices[0].message.content
                
            st.write("CollegeGPT: " + answer)

            # add message and answer to the chat history
            user_message = {"role": "user", "content": message}
            bot_message = {"role": "assistant", "content": answer}
            
            chat_history.append(user_message)
            chat_history.append(bot_message)
            state.text_field = False
            state.counter = 2




