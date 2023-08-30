import random 

with open('pollution.txt','r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

allowed_errors = 6
guesses = []
done = False

while not done:
  for letter in word:
    if letter.lower() in guesses:
       print(letter, end=" ")
    else:
       print("_",end=" ")
  print("")

  guess = input(f"allowed errors left {allowed_errors}, Next guess: ") 
  guesses.append(guess.lower())
  if guess.lower() not in word.lower():
      allowed_errors -= 1
      if allowed_errors == 0:
          break

  done = True
  for letter in word:
      if letter.lower() not in guesses:
          done = False 

if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"game over! The word was {word}!")