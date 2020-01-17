# Run this script to cycle the contents of your clipboard automatically. Perfect for... well... uh... oh no I'm running out of space to write this comment oh crap 

import keyboard, clipboard

 
strings = open("lines.txt","r").readlines()
# print(strings)

pointer = 0
run = True


def cycle():
    global pointer
    pointer += 1
    if pointer == len(strings): 
        pointer = 0

    clipboard.copy(strings[pointer])

if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+v', cycle)

    while(run):
        keyboard.wait('ctrl+v')