#program will output a random 'magic 8 ball' message
import random

messages=['It is certain',
          'Decidedly so',
          'Definitely',
          'Ask again later',
          'It is doubtful',
          'Sorry, no']

print('Ask a question')
input()
print(messages[random.randint(0,len(messages) -1)])
