#!/bin/python3

################################################################
#                                                              #
#                    Created by Nathan P.                      #
#   Free for all but dont be a dick and remove the credit.     #
#                                                              #
#                         v0.9.7                               #
#                          LINUX                               #
#                                                              #
#             Now on Malware I mean Windows 10                 #
#                                                              #
################################################################


### Change this line to the file path to properly formated .txt file that you wish to be quized on. ####
txt = 'quiz_files/Network+_questions.txt'
######################################



######must be in the following format##########
####################################################################################################################################
# TOTAL:2                                                                                                                          #
#                                                                                                                                  #
# QUESTION 1                                                                                                                       #
#                                                                                                                                  #
# what is the best food combo from lakeside pizza? (Choose 3)                                                                      #
#                                                                                                                                  #
# A. Lunch Special                                                                                                                 #
# B. Large Peperoni pizza                                                                                                          #
# C. tea                                                                                                                           #
# D. medium sasuage pizza                                                                                                          #
# E. vanilla ice cream                                                                                                             #
# F. chocolate ice cream                                                                                                           #
# G. strawberry ice cream                                                                                                          #
# H. Rootbeer                                                                                                                      #
# I. Pepsi                                                                                                                         #
#                                                                                                                                  #
# Correct Answer: ACG                                                                                                              #
#                                                                                                                                  #
#                                                                                                                                  #
# QUESTION 2                                                                                                                       #
#                                                                                                                                  #
# what is the best flavor of ice cream at lakeside pizza?                                                                          #
#                                                                                                                                  #
# A. vanilla                                                                                                                       #
# B. chocolate                                                                                                                     #
# C. straberry                                                                                                                     #
# D. neopolitan                                                                                                                    #
# E. blueberry                                                                                                                     #
# E. moosetracks                                                                                                                   #
#                                                                                                                                  #
# Correct Answer: C                                                                                                                #
####################################################################################################################################
#
# Can have up to 26 answers one for each letter. answers must be A. B. C. ect.
#


import linecache
from time import sleep
from os import system, name
import os
from termcolor import colored, cprint




def credits():
    print('################################################################'.center(int(columns)))
    sleep(.1)
    print('#                                                              #'.center(int(columns)))
    sleep(.1)
    print('#                     Created by Nathan P.                     #'.center(int(columns)))
    sleep(.1)
    print('#    Free for all but dont be a dick and remove the credit.    #'.center(int(columns)))
    sleep(.1)
    print('#                                                              #'.center(int(columns)))
    sleep(.1)
    print('#                            v0.9.7                            #'.center(int(columns)))
    sleep(.1)
    print('#                             LINUX                            #'.center(int(columns)))
    sleep(.1)
    print('#                                                              #'.center(int(columns)))
    sleep(.1)
    print('#               Now on Malware I mean Windows 10               #'.center(int(columns)))
    sleep(.1)
    print('#                                                              #'.center(int(columns)))
    sleep(.1)
    print('################################################################'.center(int(columns)))
    print("\n")
    sleep(.5)


def term_size():
    global rows
    global columns
    if name == 'nt':
        rows = os.get_terminal_size().lines
        columns = os.get_terminal_size().columns
    else:
        rows, columns = os.popen('stty size', 'r').read().split()
    
    



###clear sceen
def clear():
    ###if windows
    if name == 'nt':
        _ = system('cls')
    ##if mac or linux
    else:
        _ = system('clear')


###wait for enter
def enter():
    ###if windows
    if name == 'nt':
        _ = system('read -sn 1 -p "Press any key to continue..."')
        print
    ##if mac or linux
    else:
        _ = system("pause")


##quiz_select
def quiz_select():
    global quizes
    global quizes_files
    global direct
    global txt

    directory = (os.getcwd() + '/quiz_files')
    file_list = (os.listdir(directory))

    for i in file_list:
        quizes_files = (directory + '/' +  i)
        titleline = (linecache.getline(quizes_files,int(1))[5:-1])
        quizes.append(titleline)
        direct[titleline] = quizes_files

    while True:
        for i in quizes:
            print(i.rjust(int(int(columns)/2 - 32 + len(i))))
        print('\n')
        ans = input('Which quiz would you like to take? '.rjust(int(int(columns)/2 + 3)))
        if ans in quizes:
            txt = direct[ans]
            break
        else:
            print(colored('INVALID'.rjust(int(int(columns)/2 -32 + 7)), 'red'))
            sleep(1)
            clear()


###function to select the starting question
def start_q():
    is_it_there = 0
    global resp
    resp = input('Starting question:  '.rjust(int(int(columns)/2 -12)))
    global q_num
    q_num = int(resp)
    while is_it_there != 1:
        lookup = ("QUESTION " + str(resp) + '\n')
        with open(txt, encoding='utf-8') as f:
            for num, line in enumerate(f, 1):
                if lookup in line:
                    print(line)
                    question_num = (num + 2)
                    is_it_there = 1
        resp = int(resp) + 1
    clear()    
    return question_num


###prints out question and defines answers
def pr_ques(num):
    global ans_bank
    global resp
    global question_num
    ###print the questions
    print(num)
    is_it_there = 0
    while is_it_there != 1:
        lookup = ("QUESTION " + str(resp) + '\n')
        with open(txt, encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if lookup in line:
                    #print(line)
                    #print(i)
                    question_num = (i + 2)
                    is_it_there = 1
        resp = int(resp) + 1

    print('\n' + linecache.getline(txt,int(num)))
    num += 2
    while True:
    ###print off the answers
        line = linecache.getline(txt,int(num))
        if line == '\n':
            num+=2
            break
        else:
            ans = line[0]
            ans_bank.append(ans)
            print(line, end="")
            sleep(.25)
            num += 1
    #print(ans_bank)
    return num





###prints answers
def pr_ans(num):
    num -= 1
    line = linecache.getline(txt,int(num))
    global correct
    correct = line[16:]
    correct = list(correct)
    correct.pop()
    #print('\n\n' + line, end="")
    #print(correct)
    num +=5
    return num



### answer validation
def check_answer():
    global my_ans
    global ans_bank
    global correct
    global RANS
    global WANS
    ct = 0
    wr = 0
    while True:
        while True:
            if len(my_ans) != len(correct):
                #print(my_ans)
                #print(correct)
                my_ans = input("incorrect answer length\n    try again: ")
            else:
                break
        for i in my_ans:
            if i not in ans_bank:
                ct = 1
        if ct == 1:
            my_ans = input("invalid answers\n    Try again : ")
            my_ans = list(my_ans.upper())
            ct = 0
        else:
            break
    for i in my_ans:
        if i not in correct:
            wr = 1
    if wr == 1:
        sleep(.5)
        print('WRONG')
        print("\n\nCorrect Answers:")
        for i in correct:
            print('  '+i, end = '')
        print('\n')
        WANS += 1
        sleep(1)
    else:
        sleep(.5)
        print('CORRECT!!')
        RANS += 1



################
## here we go ##
################

try:
    rows = 0
    columns = 0

    quizes = []
    quizes_files = []
    direct = {}

    correct = []
    q_num = 0
    my_ans = ''
    resp = 0

    RANS = 0
    WANS = 0
    clear()
    ans_bank = []

    question_num = ''
    term_size()
    credits()
    quiz_select()
    question_num = start_q()

    while linecache.getline(txt,int(question_num)) != 'END\n':
        if (RANS + WANS) == 0:
            print('Right/Wrong: ' + str(RANS) + '/' + str(WANS) + '   ---   TOTAL: ' + str(RANS + WANS) + '\n\nQUESTION ' + str(resp - 1))
        else:
            print('Right/Wrong: ' + str(RANS) + '/' + str(WANS) + '   ---   ' + str((RANS/(RANS + WANS))*100) + '%   ---   TOTAL: ' + str(RANS + WANS) + '\n\nQUESTION ' + str(resp - 1))
        q_num += 1
        question_num = pr_ques(question_num)
        #print(question_num)
        sleep(1)
        my_ans = input("\nENTER to submit answer\n    : ")
        my_ans = list(my_ans.upper())
        question_num = pr_ans(question_num)
        check_answer()
        input("ENTER to continue...")
        clear()
        ans_bank = []
        if linecache.getline(txt,int(question_num)) == 'END\n':
            question_num = 3
            q_num = 1
    print('\n\n\nALL DONE')
    clear()



except KeyboardInterrupt:
    print("\n\nexiting......")
    sleep(1.5)
    clear()


except UnboundLocalError:
    print("\n\nInvalid Number\n    Exiting......")
    sleep(1.5)
    clear()
