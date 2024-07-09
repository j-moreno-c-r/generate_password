import random 
import string 

def generate_password(number_of_words,size_of_words,text_spacer):
    password = ""
    word = ""
    word_size = " " * size_of_words
    keyboard = string.ascii_lowercase + string.ascii_uppercase +  string.digits + string.punctuation
    digits_password  = number_of_words * size_of_words
    total_digits = digits_password + number_of_words
    while len(password) != total_digits:
        if len(word) < size_of_words:
                for i in word_size:
                    i = random.choice(keyboard)
                word +=  i 
        elif len(word) == size_of_words:
            password += word + text_spacer
            word = ""
           
    return password

print(":-"*30)
print("Lets made a fucking strong pasword!!!")
input_size_words= int(input("How long do you want the size of the sub-words ? "))
print(":-"*30)
input_number_words = int(input("How many sub-words do you want in your password? "))
print(":-"*30)
input_spacer_text = input("Enter the spacer text!(One caracter)")
print(":-"*30)

try:
    print(generate_password(input_number_words, input_size_words, input_spacer_text))
except ValueError as e:
    print(f"Error: {e}")

print(":-"*30)
