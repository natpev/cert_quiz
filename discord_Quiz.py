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
from asyncio import sleep
import asyncio
from os import system, name
import os
import random
import shutil
import discord
from dotenv import load_dotenv


load_dotenv(verbose=True)
client = discord.Client()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
    text_channel_list = []
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)
    for channel in text_channel_list:
        await channel.send('BOT in da house!!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )   

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.content == '$credits':
        await message.channel.send(
                "#######################################\n"
                "#                                                                                                          #\n"
                "#                                 Created by Nathan P.                                  #\n"
                "#     Free for all but don't be a dick and remove the credit.     #\n"
                "#                                                                                                          #\n"
                "#                                            v0.0.1                                                   #\n"
                "#                                        DISCORD                                                #\n"
                "#######################################")



##quiz_select
async def quiz_select():
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
async def start_q():
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
async def pr_ques(num):
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
async def pr_ans(num):
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
async def check_answer():
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
'''
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
            print('Right/Wrong: ' + str(RANS) + '/' + str(WANS) + '   ---   ' + str((RANS/(RANS + WANS))*100) + '%   ---   TOTAL: ' + str(RANS + WANS) + '\n\nQUESTION ' + str(resp))
        q_num += 1
        question_num = pr_ques(question_num)
        #print(question_num)
        sleep(1)
        my_ans = input("\nENTER to submit answer\n    : ")
        my_ans = list(my_ans.upper())
        question_num = pr_ans(question_num)
        check_answer()
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
'''













client.run(TOKEN)
