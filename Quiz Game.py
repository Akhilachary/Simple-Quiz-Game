import random
import diction
print("***********************************************")
print("Welcome to Quiz Game")
score=0
rounds=0
something=[]
while(rounds<10):
    questionn=random.choice(diction.data)
    value=questionn['question']
    if value in something:
        continue
    something.append(questionn['question'])
    print(questionn['question'])
    print("A. "+questionn['A'])
    print("B. "+questionn['B'])
    print("C. "+questionn['C'])
    print("D. "+questionn['D'])
    chc=input("Enter your answer (A/B/C/D): ").upper()
    if chc not in ['A', 'B', 'C', 'D']:  # Validate input
        print("Invalid choice. Please select A, B, C, or D.")
        continue  # Skip this round if input is invalid
    rounds+=1
    if questionn[chc]==questionn['answer']:
        print("Correct Answer")
        score+=1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is: {questionn['answer']}")
    print(f"Your current score is {score}/{rounds}")
    print("***********************************************")

print(f"you have given {score} correct answer")
print(f"Your score is {score/rounds*100}% ")
