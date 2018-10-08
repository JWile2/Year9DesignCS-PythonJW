questions = ("2 x 5:""10", "25 x 5""125") 
for q in questions.keys(): 
	user_answer = input(q) 
	if questions.get(q) == user_answer: 
  	print("Correct:") 
else: 
  	print("Incorrect:")