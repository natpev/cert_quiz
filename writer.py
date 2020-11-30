#!/bin/python3
import signal
import os
from os import system
import readline
readline.parse_and_bind("tab: complete")




#signal.signal(signal.SIGINT, signal.SIG_IGN)
#signal.signal(signal.SIGTSTP, signal.SIG_IGN)

quiz = 'x'

resp_bank = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
resp_num = 0
ans_bank = ['Y','N']
char = ['','\n']
first = 0

def complete(text,state):
    results = [x for x in filelist if x.startswith(text)] + [None]
    return results[state]

readline.set_completer(complete)




def clear():
#    pass
    _ = system('clear')


new = input('New quiz? Y|N  ')

while True:
    if new.upper() in ans_bank:
        break
    else:
        print('INVALID')
        new = input('New quiz? Y|N  ')
if new.upper() == 'Y':
    quiz = ('quiz_files/' + input('filename? (without extension)  :') + '.txt')
    title = (input('quiz title  :'))
    with open(quiz, mode='a') as myfile:
        myfile.write('QUIZ:' + title + '\nTOTAL:\n\n\n\n')
    q_num = 1







else:            ##continue old quiz
    print('\n')
    filelist = (os.listdir(os.getcwd()+ '/quiz_files'))
    for i in filelist:
        print(i)
    quiz = input('\nchoose quiz to edit  :')
    while True:
        if quiz in filelist:
            break
        else:
            quiz = input('choose quiz to edit  :')
    quiz = ('quiz_files/' + quiz)
    flength = sum(1 for line in open(quiz))
    print(flength)
    for line in reversed(open(quiz).readlines()):
        if 'QUESTION' in line:
            q_num = (int(line[8:]) + 1)
            break






try:
    clear()

    while True:
        addq = input('\nadd question Y|N : ')
        while True:
            if addq.upper() not in ans_bank:
                addq = input('\nadd question Y|N : ')
            else:
                break
        clear()
        if addq.upper() == 'Y':
            question = input('\nenter question: ' + str(q_num) + '\n')
            question = question.replace('\\n', '\n')
            with open(quiz, mode='a') as myfile:
                myfile.write(char[first] + '\n\nQUESTION ' + str(q_num) + '\n\n' + question + '\n\n')
            first = 1
        else:
            with open(quiz, mode='a') as myfile:
                myfile.write('\n')
            clear()
            print('\n\ndone at ' + str(q_num - 1))
            break

        while True:
            while True:
                try:
                    adda = input('number of responses : ')
                    if int(adda) >26:
                        raise ValueError("value too great")
                    elif int(adda) <1:
                        raise ValueError("value too small")
                    else:
#                        print(adda)
                        break
                except:
                    print('INVALID')
            while  int(adda) > 0:
                resp = input('\nenter option  ' + resp_bank[resp_num] + '. ')
                with open(quiz,mode='a') as myfile:
                    myfile.write(resp_bank[resp_num] + '. ' + resp + '\n')
                resp_num += 1
                adda = (int(adda) - 1)
            else:
                correct = input('\ncorrect answer: ')
                with open(quiz,mode='a') as myfile:
                    myfile.write('\nCorrect Answer: ' + correct.upper())
                resp_num = 0
                q_num = (int(q_num) + 1)
                break
        expl = input('Explination: ')
        with open(quiz,mode='a') as myfile:
            myfile.write('\n\nExplination: ' + expl)
        clear()
except KeyboardInterrupt:
    print('hi')

