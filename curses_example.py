import curses



def interact(screen):
    while True:
        key = screen.getch()
        screen.addstr("Got: %s\n" % key)

# curses.wrapper(interact)

screen = curses.initscr()

curses.noecho()
curses.cbreak()
screen.keypad(1)

try:
    interact(screen)
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
