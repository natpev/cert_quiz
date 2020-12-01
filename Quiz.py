#!/bin/python3

################################################################
#                                                              #
#                    Created by Nathan P.                      #
#   Free for all but dont be a dick and remove the credit.     #
#                                                              #
#                         v1.0.2                               #
#                          LINUX                               #
#                                                              #
#             Now on Malware I mean Windows 10                 #
#                                                              #
################################################################


import linecache
from time import sleep
from os import system, name
import os
import random
import shutil
try:
    import readline
except:
    pass
readline.parse_and_bind("tab: complete")





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
    print('#                            v1.0.2                            #'.center(int(columns)))
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
    elif name == 'posix':
        #rows, columns = os.popen('stty size', 'r').read().split()
        columns, rows = shutil.get_terminal_size((65, 30))
    else:
        rows = 30
        columns = 65
    
    



###clear sceen
def clear():
    ###if windows
    if name == 'nt':
        _ = system('cls')
    ##if mac or linux
    else:
        _ = system('clear')



###tab complete
def complete(text,state):
    results = [x for x in quizes if x.startswith(text)] + [None]
    return results[state]

readline.set_completer(complete)


##quiz_select
def quiz_select():
    global quizes
    global quizes_long
    global quizes_files
    global direct
    global txt
    global file_len

    directory = (os.getcwd() + '/quiz_files')
    file_list = (os.listdir(directory))

    for i in file_list:
        quizes_files = (directory + '/' +  i)
        titleline = (linecache.getline(quizes_files,int(1))[5:-1])
        totalline = ('  ' + linecache.getline(quizes_files,int(2))[6:-1])
        quizes_long.append(titleline + '  ' + totalline.rjust(61 - len(titleline), '-') + 'Q')
        quizes.append(titleline)
        direct[titleline] = quizes_files

    while True:
        for i in quizes_long:
            print(i.rjust(int(int(columns)/2 - 31 + len(i))))
        print('\n')
        ans = input('Which quiz would you like to take? '.rjust(int(int(columns)/2 + 4)))
        if ans in quizes:
            txt = direct[ans]
            file_len = ((linecache.getline(txt,2))[6:-1])
            break
        else:
            print('INVALID'.rjust(int(int(columns)/2 -24)))
            sleep(1)
            clear()


###function to select the starting question
def start_q():
    global random_choice
    global file_len
#    global ans_bank
    is_it_there = 0
#    print(yesno_bank)
    random_choice = input('Randomize Questions? Yes|No  '.rjust(int(int(columns)/2 - 2)))
    while True:
        if random_choice.upper() in yesno_bank:
            break
        else:
            print('INVALID')
            random_choice = input('Randomize Questions? Yes|No  '.rjust(int(int(columns)/2 - 2)))
    global resp
    if random_choice.upper() in no_bank:
        while True:
            try:
                resp = int(input('Starting question:  '.rjust(int(int(columns)/2 -11))))
                if resp < 1:
                    raise ValueError('value too low')
                elif resp > int(file_len):
                    raise ValueError('value too high')
                else:
                    break
            except KeyboardInterrupt:
                raise
            except:
                print('INVALID'.rjust(int(int(columns)/2 -24)))
    else:
        resp = random.randint(1,int(file_len))
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
    clear()    
    return question_num


###prints out question and defines answers
def pr_ques(num):
    global ans_bank
    global resp
    global question_num
    ###print the questions
##    print(str(num) + 'num')
##    print(str(resp) + ' resp')
    is_it_there = 0
    while is_it_there != 1:
        lookup = ("QUESTION " + str(resp) + '\n')
        with open(txt, encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if lookup in line:
##                    print(line + 'line')
##                    print(str(i) + ' i')
                    question_num = (i + 2)
                    num = question_num
                    is_it_there = 1
        resp = int(resp) + 1

    print('\n')
    while True:
        line = (linecache.getline(txt,int(num)))
        if line == '\n':
            num += 1
            break
        else:
            print(line, end="")
            num += 1
    print('\n')
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
                my_ans = input("incorrect answer length\n    try again: ")
                my_ans = list(my_ans.upper())
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
        print("\nCorrect Answers:")
        for i in correct:
            print('  '+i, end = '')
        print('\n')
        WANS += 1
        sleep(1)
    else:
        sleep(.5)
        print('CORRECT!!')
        RANS += 1



### print explination
def explain(num):
    exp = linecache.getline(txt,int(num - 3))
    if len(exp) > 13:
        print(exp)






################
## here we go ##
################

try:
    yes_bank = ['YES', 'Y']
    no_bank = ['NO', 'N']
    yesno_bank = ['Y', 'N', 'YES', 'NO']
    rows = 0
    columns = 0

    txt = ''
    random_choice = ''
    file_len = ''
    quizes = []
    quizes_long = []
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

    while True:
        if (RANS + WANS) == 0:
            print('Right/Wrong: ' + str(RANS) + '/' + str(WANS) + '   ---   TOTAL: ' + str(RANS + WANS) + '\n\nQUESTION ' + str(resp))
        else:
            print('Right/Wrong: ' + str(RANS) + '/' + str(WANS) + '   ---   ' + str(round(((RANS/(RANS + WANS))*100),2)) + '%   ---   TOTAL: ' + str(RANS + WANS) + '\n\nQUESTION ' + str(resp))
        q_num += 1
        question_num = pr_ques(question_num)
        #print(question_num)
        sleep(1)
        my_ans = input("\nENTER to submit answer\n    : ")
        my_ans = list(my_ans.upper())
        question_num = pr_ans(question_num)
        check_answer()
        explain(question_num)
        input("ENTER to continue...")
        if resp > int(file_len):
            resp = 1
        if random_choice.upper() in yes_bank:
            resp = random.randint(1,int(file_len))
        clear()
        ans_bank = []
    print('\n\n\nALL DONE')
    clear()



except KeyboardInterrupt:
    print("\n\nexiting......")
    sleep(1.5)
#    clear()


except UnboundLocalError:
    print("\n\nInvalid Number\n    Exiting......")
    sleep(1.5)
    clear()
