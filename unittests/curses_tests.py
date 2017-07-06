import curses
from templates.template_text import Templates

class CursesTest(object):
    temp =Templates()

    myscreen = curses.initscr()
    win = curses.newwin(25, 50, 30, 100)

    myscreen.border(0)
    myscreen.addstr(10, 10, temp.BANNER_THEWELL)
    myscreen.refresh()
    myscreen.getch()

    curses.endwin()
