#!/bin/python3
import signal
from os import system

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)

quiz = 'quiz_files/Pentest+_questions.txt'

resp_bank = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
resp_num = 0
ans_bank = ['Y','N']
char = ['','\n']
first = 0

def clear():
    _ = system('clear')

try:
        clear()
        while True:
            try:
                q_num = int(input('starting point: '))
                if int(q_num) < 1:
                    raise ValueError('value too small')
                else:
                    break
            except:
                print('INVALID')
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
                while True:
                    try:
                        adda = input('number of responses : ')
                        if int(adda) >26:
                            raise ValueError("value too great")
                        elif int(adda) <1:
                            raise ValueError("value too small")
                        else:
                            print(adda)
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
except:
    pass
