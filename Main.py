from itertools import count
from platform import python_branch
from turtle import pu
import pyautogui
import time

time.sleep(4)
count=0
while count <= 5 :
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")
    count=count+1
