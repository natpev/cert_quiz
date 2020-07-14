#!/bin/python3

################################################################
#                                                              #
#                    Created by Nathan P.                      #
#   Free for all but dont be a dick and remove the credit.     #
#                                                              #
#                         v0.9.0                               #
#                                                              #
################################################################


### Change this line to the file path to properly formated .txt file that you wish to be quized on
txt = 'Network+_questions.txt'
######################################





######must be in the following format##########
#########################################################################################################
## QUESTION 1
##
## A UTM is deployed on the external edge of the main corporate office. The office connects to the WAN port of the edge router.The edge router at the main office connects to the remote offices using GRE IPSec tunnels. A network administrator noticesthat a worm that was not detected by the UTM has spread from the remote sites into the corporate network. The UTM currentlyhas traffic rules applied that should block the port used by the worm. Which of the following steps would MOST likely correctthis issue?
##
## A.Move the UTM onto the LAN side of the network
## B.Enable TLS inspection on the UTM
## C.Enable stateful inspection on the UTM
## D.Configure the UTM to deny encrypted files from being transferred
## 
## Correct Answer: C
## 
## 
## QUESTION 2
##
## A technician has racked a new access switch and has run multimode fiber to a new location. After installing an extended-range10Gb SFP in the core switch, the technician installed a 10Gb SFP in the access switch and connected the port to the newextension with a fiber jumper. However, the link does not display, and the technician cannot see light emitting from the coreswitch. Which of the following solutions is MOST likely to resolve the problem?
##
## A.Swap the fiber pairs in one of the SFPs 
## B.Replace the jumpers with single-mode fiber
## C.Set the correct MTU on the new interface
## D.Install an optic that matches the fiber type 
##
## Correct Answer: B
##
##
#########################################################################################################
##
## Can have up to 26 answers one for each letter. answers must be A. B. C. ect.



import linecache
from time import sleep
from os import system, name
import os



def credits():
    print('################################################################')
    sleep(.1)
    print('#                                                              #')
    sleep(.1)
    print('#                    Created by Nathan P.                      #')
    sleep(.1)
    print('#   Free for all but dont be a dick and remove the credit.     #')
    sleep(.1)
    print('#                                                              #')
    sleep(.1)
    print('#                         v0.9.0                               #')
    sleep(.1)
    print('#                                                              #')
    sleep(.1)
    print('################################################################\n')
    sleep(.5)





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


###function to select the starting question
def start_q():
    resp = input('Starting question:  ')
    global q_num
    q_num = int(resp)
    #resp = '450'
    lookup = ("QUESTION " + resp)
    with open(txt) as f:
        for num, line in enumerate(f, 1):
            if lookup in line:
                question_num = (num + 2)
                break
    clear()    
    return question_num

###prints out question and defines answers
def pr_ques(num):
    global ans_bank
    ###print the questions
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
    correct = []
    q_num = 0
    my_ans = ''

    RANS = 0
    WANS = 0
    clear()
    ans_bank = []

    question_num = ''
    credits()
    question_num = start_q()

    while linecache.getline(txt,int(question_num)) != 'END\n':
        if (RANS + WANS) == 0:
            print('Right/Wrong: ' + str(RANS) + '/' + str(WANS) + '   ---   TOTAL: ' + str(RANS + WANS) + '\n\nQUESTION ' + str(q_num))
        else:
            print('Right/Wrong: ' + str(RANS) + '/' + str(WANS) + '   ---   ' + str((RANS/(RANS + WANS))*100) + '%   ---   TOTAL: ' + str(RANS + WANS) + '\n\nQUESTION ' + str(q_num))
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
    print('\n\n\nALL DONE')
    clear()



except KeyboardInterrupt:
    print("\n\nexiting......")
    sleep(1.5)

except UnboundLocalError:
    print("\n\nInvalid Number\n    Exiting......")
    sleep(1.5)
