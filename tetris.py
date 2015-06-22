import arena
import termcolor
from block import Block

if __name__ == '__main__':
    a = arena.Arena()
    while True:
        b = Block()
        if a.block is None:
            if not a.add_block(block=b):
                termcolor.cprint('Game Over. Block cannot be added')
                exit(0)
        termcolor.cprint(a, color='blue')
        while True:
            termcolor.cprint('[a/A] Move Left', color='yellow')
            termcolor.cprint('[d/D] Move Right', color='yellow')
            termcolor.cprint('[w/W] Rotate Counter Clockwise', color='yellow')
            termcolor.cprint('[s/S] Rotate Clockwise', color='yellow')
            termcolor.cprint('[n/N] Next', color='yellow')
            termcolor.cprint('[x/X] Exit', color='yellow')
            choice = raw_input(termcolor.colored('Enter Choice: ', color='yellow'))

            choice = choice.lower()
            if choice == 'd':
                a.move_right()
                break
            elif choice == 'a':
                a.move_left()
                break
            elif choice == 'w':
                a.rotate_cc()
                break
            elif choice == 's':
                a.rotate()
                break
            elif choice == 'n' or choice == '':
                break
            elif choice == 'x':
                exit(0)
            else:
                termcolor.cprint('Invalid Input', color='red')
                continue

        a.step()