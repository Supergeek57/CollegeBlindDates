import cohere

co = cohere.Client('lbUN2pth8eW9zd7M6TQOVRZyufL4UIWNJoNqG3C5')
#prompt = "You are a counselor who helps high school students find their best-fit colleges. "
#model = "command"  # Choose a suitable model from Cohere's offerings

#Sample history:
#{"role": "USER", "message": "Hi! I'm a high school student looking for colleges to apply to. I want to attend a small liberal arts college with a low student to faculty ratio. I plan to major in biology and I want to enter a graduate program after college."},
#{"role": "CHATBOT", "message": "I've found a potential match for you! It has less than 2,000 students and an amazing biology program. Do you have a specific location preference?"},
#{"role": "USER", "message": "I want to be located in a rural or suburban area."},
#{"role": "CHATBOT", "message": "Perfect! The school I'm thinking of is in a small town in Maryland, right on the water. What else do you want to know about this school?"},
#{"role": "USER", "message": "What's the name of the school?"},
#{"role": "CHATBOT", "message": "I want you to keep an open mind, so I'm not going to tell you the name of the school until you ask a couple more follow up questions."},
#{"role": "USER", "message": "Ok, what's the student to faculty ratio?"},
#{"role": "CHATBOT", "message": "It's about 15:1, which is considered very good. Students studying biology also perform very well in terms of getting into graduate programs."},
#{"role": "USER", "message": "That sounds great! What's the name of the school?"},
#{"role": "CHATBOT", "message": "Drumroll please... It's St. Mary's College of Maryland! Here's their website: www.smcm.edu"},
#{"role": "USER", "message": "Thanks so much!"},
#{"role": "CHATBOT", "message": "No problem! Let me know if you have any other questions about St. Mary's."},
#{"role": "SYSTEM", "message": "That was an example of a good conversation with a student. Remember not to suggest any schools with less than a 20 percent acceptance rate, and don't say the name of the school until 2 or more follow up questions have been asked!"},
    

chat_history=[
    {"role": "SYSTEM", "message": "You are a counselor who helps high school students find their best-fit colleges. A student tells you what they want in a college, including scholarship opportunities, extracurriculars, student-to-faculty ratio, and other factors. You respond with a college that you think meet most or all of their criteria, and explain why you think that school might be a good fit. The catch is that you DON'T reveal the name of the school, and you never suggest schools with acceptance rates below 20%. Your objective is to help students discover schools that may not have been on their radar before."}
    #{"role": "SYSTEM", "message": "Remember, you want students to keep an open mind, so don't give the name of the school until at least 2 follow-up questions have been asked! Also, don't mention the school's ranking or acceptance rate."}
  ]

max_turns = 10

for i in range(max_turns):
    # get user input
	message = input("Talk to me about colleges: ")
	if i==0:
		message += "When you give me my recommendation, I want it to be like a blind date--don't tell me the name of the school!"
	elif i <= 2:
		message += "Remember, don't tell me the name of the school!"
	else:
		message += "(You can tell me the name of the school now.)"
    
	# generate a response with the current chat history
	response = co.chat(
		chat_history=chat_history,
		message=message,
		connectors=[{"id": "web-search"}]
	)
	answer = response.text
		
	print(answer)

	# add message and answer to the chat history
	user_message = {"role": "USER", "text": message}
	bot_message = {"role": "CHATBOT", "text": answer}
	
	chat_history.append(user_message)
	chat_history.append(bot_message)


#message="I'm looking for a school with good merit scholarships, lots of opportunities for undergraduate research, and strong extracurriculars. I'm planning on majoring in computer science and math, and I want to be a software developer.",
#When you give me my recommendation, I want it to be like a blind date--don't tell me the name of the school until I ask some follow up questions first!