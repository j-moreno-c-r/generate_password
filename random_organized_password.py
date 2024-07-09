import random

with open('list_of_words.txt') as f:
    lines = f.read().splitlines() 

def generate_password(number_of_words,text_spacer):
    password = []
    word = ""
    while len(password) != number_of_words * 2:
        word = random.choice(lines) 
        password.append(word)
        password.append(text_spacer) 
    key = ''.join(password)
    return key            

print(":-"*30)
print("Lets made a fucking strong pasword!!!")
input_number_words = int(input("How many sub-words do you want in your password? "))
print(":-"*30)
input_spacer_text = input("Enter the spacer text!(One caracter)")
print(":-"*30)

try:
    print(generate_password(input_number_words, input_spacer_text))
except ValueError as e:
    print(f"Error: {e}")

print(":-"*30)
