print('Welcome to the ultimate Naruto quiz!')

playing = input('Would you like to play? ')

if playing.lower() != 'yes':
    quit()

print("Let's go! Spelling is important here ;)")
score = 0

# 1st quiz question
answer = input("Which member of the Konoha 11 cannot use ninjutsu or genjutsu? ")
if answer.lower() == "rock lee":
    score += 1
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 0/10 questions correctly.')
    quit()

# 2nd quiz question
answer = input('Who is the leader of Team 7? ')
if answer.lower() == 'kakashi' or answer.lower() == 'kakashi hatake':
    score +=1
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 1/10 questions correctly.')
    quit()

# 3rd quiz question BONUS
answer = input('BONUS QUESTION! What is the name of the ramen guy? ')
if answer.lower() == 'teuchi':
    score += 2
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 2/10 questions correctly.')
    quit()

# 4th quiz question
answer = input('Who did Rock Lee fight drunk? ')
if answer.lower() == 'kimimaro' or answer.lower() == 'kimimaro kaguya':
    score += 1
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 3/10 questions correctly.')
    quit()

# 5th quiz question
answer = input('Who was the hokage when Naruto was born? ')
if answer.lower() == 'minato' or answer.lower() == 'minato namikaze':
    score += 1
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 4/10 questions correctly.')
    quit()

# 6th quiz question BONUS
answer = input('BONUS QUESTION! The lotus of the Leaf Village blooms how many times? ')
if answer.lower() == 'twice' or answer.lower() == '2':
    score += 2
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 5/10 questions correctly.')
    quit()

# 7th quiz question
answer = input('The first time we saw Naruto use the Kyuubi Chakra cloak, who was he fighting? ')
if answer.lower() == 'haku':
    score += 1
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 6/10 questions correctly.')
    quit()

# 8th quiz question
answer = input("Who calls themself Naruto's biggest rival? ")
if answer.lower() == 'konohamaru' or answer.lower() == 'konohamaru sarutobi':
    score += 1
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 7/10 questions correctly.')
    quit()

# 9th quiz question BONUS
answer = input("What does 'Chidori' mean? ")
if answer.lower() == 'one thousand birds' or answer.lower() == '1000 birds' or answer.lower() == 'a thousand birds':
    score += 2
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 8/10 questions correctly.')
    quit()

# 10th quiz question
answer = input("What is the name of The Sage of Six Path's two children? ")
if answer.lower() == 'asura and indra' or answer.lower() == 'indra and asura' or answer.lower() == 'asura and indra otsutsuki' or answer.lower() == 'indra and asura otsutsuki':
    score += 1
    print('Correct! Your score is now ' + str(score) + '!')
else:
    print('Sorry, that is incorrect.')
    print('You got ' + str(score) + ' points and answered 9/10 questions correctly.')
    quit()

# final result
print('You got ' + str(score) + ' points and answered all 10 questions correctly!')
