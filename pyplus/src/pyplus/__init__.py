import math, random, pyfiglet, time, signal
from os import system

def reprint(oldmsg:str,newmsg:str,delay:float=2):
    if len(oldmsg) == len(newmsg):
        print(oldmsg, end="\r")
        time.sleep(delay)
        print(newmsg)
    elif len(oldmsg) > len(newmsg):
        adder = len(oldmsg)-len(newmsg)
        updatedmsg = newmsg
        for i in range(adder):
            updatedmsg = updatedmsg+" "
            
        print(oldmsg, end="\r")
        time.sleep(delay)
        print(updatedmsg)
    else:
        print(oldmsg, end="\r")
        time.sleep(delay)
        print(newmsg)

        


def forloop(msg:str,count:int,i:int,step:int=1,delay:float=0):
    for i in range(0,count,step):
        print(msg,i)
        time.sleep(delay)

class Ascii:
    def __init__(self,msg:str):
        self.msg = msg

    def print(self):
        print(pyfiglet.figlet_format(self.msg))


inf = lambda: 999999999999999999999999999999999999**999999999999999999999999999999999999**999999999999999999999999999999999**99999999999999999**9999999999999 

def pause(pause_length=2):
    if pause_length == "tiny":
        time.sleep(0.5)
    elif pause_length == "short":
        time.sleep(1)
    elif pause_length == "medium":
        time.sleep(2)
    elif pause_length == "long":
        time.sleep(3)
    elif pause_length == int:
        time.sleep(pause_length)

def bat_cmd(cmd:str):
    system(cmd)


def clear():
    system("cls")

def batpause():
    system("pause")

def marker(name:str):
    system(":"+name)

def goto(marker:str):
    try:
        system("goto "+marker)
    except:
        print("Marker not found. make sure to make a marker using the `marker()` function.")

def ping(host:str,nul:bool):
    if nul == True:
        system("ping -n 1 "+host+" > nul")
    else:
        system("ping -n 1 "+host)

def color(color):
    try:
        system("color "+color)
    except:
        print("Color not found. Try one of the following:")
        print("""0 = black 8 = gray.
1 = navy 9 = blue.
2 = green A = lime.
3 = teal B = aqua.
4 = maroon C = red.
5 = purple D = fuchsia.
6 = olive E = yellow.
7 = silver F = white.""")

def echooff():
    system("@echo off")

def echo(msg:str):
    system("echo "+msg)






        