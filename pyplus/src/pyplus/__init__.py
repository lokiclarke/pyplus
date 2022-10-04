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


INFINITY = 999999999999999999999999999999999999**999999999999999999999999999999999999**999999999999999999999999999999999**99999999999999999**9999999999999**9999999**99999999

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

def batpause(nul:bool):
    if nul == True:
        system("pause >nul")
    else:
        system("pause")

def marker(msg:str,name:str):
    system("echo "+msg)
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

def color(text:str,bg:str):
    if text == "black":
        text = "0"
    elif text == "navy":
        text = "1"
    elif text == "green":
        text = "2"
    elif text == "teal":
        text = "3"
    elif text == "maroon":
        text = "4"
    elif text == "purple":
        text = "5"
    elif text == "olive":
        text = "6"
    elif text == "silver":
        text = "7"
    elif text == "gray":
        text = "8"
    elif text == "grey":
        text = "8"
    elif text == "blue":
        text = "9"
    elif text == "lime":
        text = "a"
    elif text == "aqua":
        text = "b"
    elif text == "red":
        text = "c"
    elif text == "fuchisa":
        text = "d"
    elif text == "yellow":
        text = "e"
    elif text == "white":
        text = "f"
    elif bg == "black":
        bg = "0"
    elif bg == "navy":
        bg = "1"
    elif bg == "green":
        bg = "2"
    elif bg == "teal":
        bg = "3"
    elif bg == "maroon":
        bg = "4"
    elif bg == "purple":
        bg = "5"
    elif bg == "olive":
        bg = "6"
    elif bg == "silver":
        bg = "7"
    elif bg == "gray":
        bg = "8"
    elif bg == "grey":
        bg = "8"
    elif bg == "blue":
        bg = "9"
    elif bg == "lime":
        bg = "a"
    elif bg == "aqua":
        bg = "b"
    elif bg == "red":
        bg = "c"
    elif bg == "fuchisa":
        bg = "d"
    elif bg == "yellow":
        bg = "e"
    elif bg == "white":
        bg = "f"
    try:
        system("color "+text+bg)
    except SystemError:
        print("That color is not supported.")
        

def echooff():
    system("@echo off")

def echo(msg:str):
    system("echo "+msg)
