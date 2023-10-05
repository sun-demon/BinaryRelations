import os

import task1
import task2
import task3


def clear_screen():
    os.system('cls')
    print('\b\b', end='')


def pause_screen():
    print('Нажмите Enter для продолжения...', end='')
    input()


tasks = [task1.run, task2.run, task3.run]
key = 0
while key != '0':
    clear_screen()
    for i in range(1, len(tasks) + 1):
        print(f'{i}) Задание №{i}')
    print('0) Выход')
    key = input(' >>')
    if not key.isdigit():
        continue
    if 0 < int(key) <= len(tasks):
        clear_screen()
        tasks[int(key) - 1]()
        pause_screen()
clear_screen()
