import os, re

def get_name_date(quiz):
    getname = re.compile(r'Name:(.*)')
    getdate = re.compile(r'Date:(.*)')
    name = re.search(getname, quiz).groups()[-1].strip()
    date = re.search(getdate, quiz).groups()[-1].strip()
    return name, date

def mark(answer, quiz):
    res = r'(\d+\.What\sis\sthe\scapital\sof\s\w+(\s+\w+)*\?\s(\w+))'
    answeredquestions = re.findall(res, quiz)
    correctAnswers = answer.split()
    score = 0
    for question, answer in zip(answeredquestions, correctAnswers):
        if question[-1] == answer:
            score += 1
    return score

def main():
    quest_list = os.listdir('Questions')
    answer_list = os.listdir('Answers')
    quest_answer = zip(quest_list, answer_list)
    pairs = list(quest_answer)
    
    # formatting
    # this is our header
    name, date, score = 'Name', 'Date', 'Score'
    fmt = '|{0:<30}| {1:10} |{2}'
    print('-'*50)
    print(fmt.format(name, date, score))
    print('-'*50)

    for pair in pairs:
        questionfile, answerfile = pair
        quiz = open(f'Questions/{questionfile}').read()
        answer = open(f'Answers/{answerfile}').read()
        name, date = get_name_date(quiz)
        score = mark(answer, quiz)
        print(fmt.format(name, date, score))
        print('-'*50)

main()