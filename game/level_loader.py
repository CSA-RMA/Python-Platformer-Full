import csv
import pygame

import constants
import platforms
import collectables

with open('level_01_Tile Layer 1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
