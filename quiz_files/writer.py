#!/bin/python3
from os import system

quiz = 'CySA+_questions.txt'
resp_bank = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
resp_num = 0
ans_bank = ['Y','N']
char = ['','\n']
first = 0

def clear():
    _ = system('clear')

clear()
q_num = input('starting point: ')

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
        clear()
        print('\n\ndone at ' + str(q_num - 1))
        break

    while True:
        adda = input('add answer Y|N : ')
        while True:
            if adda.upper() not in ans_bank:
                adda = input('add answer Y|N : ')
            else:
                break
        if adda.upper() == 'Y':
            resp = input('\nenter option  ' + resp_bank[resp_num] + '. ')
            with open(quiz,mode='a') as myfile:
                myfile.write(resp_bank[resp_num] + '. ' + resp + '\n')
            resp_num += 1
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
