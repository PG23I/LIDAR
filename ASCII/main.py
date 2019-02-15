"""This program will serve as an entry point for all other programs"""
from data_proccessor import type1_converter
from plot import plotter

mode = 0

while mode!=1 and mode!=2:
    print("Enter 1 for Dr. Wang's Lidar\nEnter 2 for April's Lidar\nChoice: ",end='')
    mode = input()
    mode = int(mode)


if mode == 2:
    type1_converter()
elif mode == 1:
    print("Under construction! :D")


print("Do you want to plot this data? (Yes=1, No=0): ",end='')
choice = input()

if int(choice) == 1:
    plotter()
else:
    print("END")