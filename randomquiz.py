import os, json, random
'''
create 35 different quiz into a folder for students and
create a marker to mark the scripts
'''

def make_folders():
    for fold in folder:
        os.makedirs(fold, exist_ok=True)  #Creates folder for the each items in folderlist

def read_in_capitals():
    # Create quiz with question and answers in random order, along with the answerkey
    with open('capitals.json') as fp:
        capitals = json.load(fp)
    return capitals

def states_works(answerKeyFile, quizFile, states):
    # Loop through all 50 states, making a question for each  
    for questionNum in range(50):
        # Get right and wrong anwers.
        correctAnswer = capitals[ states[questionNum] ]
        wrongAnswers = list(capitals.values())

        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file
        quizFile.write('%s.What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        
        for i in range(4):
            quizFile.write('    %s.%s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        #Write the answer key to a file.
        answerKeyFile.write('%s\n' % ( 'ABCD'[answerOptions.index(correctAnswer)]))

def quiz(num):
    for quizNum in range(num):
        # Create the quiz and answer key files
        quizFile = os.path.join(folder[0], 'capitalsquiz%s.txt' % (quizNum + 1))
        quizFile = open(quizFile, 'w')

        answerKeyFile = os.path.join(folder[1],'quiz_answers%s.txt' % (quizNum + 1))
        answerKeyFile = open(answerKeyFile, 'w')
        # Write out the header for the quiz
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')

        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')
        # shuffle the order of the states
        states = list(capitals.keys())
        random.shuffle(states)
        states_works(answerKeyFile, quizFile, states)
        quizFile.close()
        answerKeyFile.close()

if __name__ == "__main__":
    folder =  [ 
                'Questions',
                'Answers',
            ]

    make_folders()
    capitals = read_in_capitals()
    quiz(5)