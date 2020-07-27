#!/bin/python3

from os import system, name
from time import sleep
import linecache
import os
from termcolor import colored, cprint
quizes = []
quizes_files = []
direct = {}


directory = (os.getcwd() + '/quiz_files')
file_list = (os.listdir(directory))



for i in file_list:
    quizes_files = (directory + '/' +  i)
    titleline = (linecache.getline(quizes_files,int(1))[5:-1])
    quizes.append(titleline)
    direct[titleline] = quizes_files





while True:
    for i in quizes:
        print(i)
    ans = input('\nWhich quiz would you like to take? ')
    if ans in quizes:
        break
    else:
        print(colored('INVALID', 'red'))
        sleep(1)
