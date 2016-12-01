#!/usr/bin/python
input = open('test')
array = input.readline().split(', ')
direction = 0
position = [0, 0]
for command in array:
    if(command[0] == 'R'):
        direction += 1
    if(command[0] == 'L'):
        direction -= 1
    if(direction % 4 == 0):
        position[1] += int(command[1])
    if(direction % 4 == 1):
        position[0] += int(command[1])
    if(direction % 4 == 2):
        position[1] -= int(command[1])
    if(direction % 4 == 3):
        position[0] += int(command[1])
print(position)
print(abs(position[0]) + abs(position[1]))
