import streamlit as st

st.set_page_config(
    page_title="Hi! :wave:",
    page_icon="",
    )

st.write("# Hi there! We're College Safari.")

#st.sidebar.success("Navigation")

with st.sidebar:
    #openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    #"[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    #"[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![See it on GitHub](https://github.com/codespaces/badge.svg)](https://github.com/supergeek57)"


st.markdown(
"""
Can we all agree that the college application process is pretty terrible? 
\n:poop: You have to 'be yourself,' yet you're somehow being judged on how well you do that, which makes absolutely no sense.
\n:poop: Financial aid policies are so confusing that it can be hard to figure out if you can even afford a school.
\n:poop: And worst of all...you're probably getting massive pressure to go to a 'good' (read: highly ranked, highly selective) school, **regardless of what you actually want**.

The good news is...**College Safari is here to help! (Especially with that last one.)**
We've compiled some awesome resources (including peer-reviewed journals!) on 
- why going to an Ivy League or similar university isn't actually a golden ticket to success
- why the argument that you'll only get hired at a top company if you go to an Ivy(+) school is wrong (and why lots of people still think it's true)
- why you should go to the school that's actually the best fit for YOU!

But debunking the "Ivy or Bust!" myth doesn't actually get you any closer to that right-fit school, so we've also created **College Blind Dates** to get you started!
Think of it like Tinder, but for colleges. You take a quick (and fun!) quiz about what you want in a school--everything from academics to clubs to scholarship opportunities--and we send it to a large-language model (think College-GPT) to recommend a possible fit for you.

There are a few catches though!
- It's a blind date, so you won't know the name of the school until you've asked some follow-up questions first.
- To make sure we're expanding your horizons, College Blind Dates won't return any schools with less than a 20 percent acceptance rate. So to our fellow Type A students: This literally can't turn into a competition for who can get low acceptance rate matches! :wink:
- Our quiz won't ask you for things like GPA and test scores. Median GPA and test scores of admitted students are closely correlated with school rankings, and we don't want CollegeGPT to consider that in generating matches for you.

We hope we can make the college search less :poop: and more :star-struck:. This is a super exciting time because you get to find a place you're genuinely excited about!
Happy adventuring,

The College Safari team

"""
)

