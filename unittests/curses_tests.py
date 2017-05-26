import curses
from templates.template_text import Templates

class CursesTest(object):
    temp =Templates()

    myscreen = curses.initscr()
    # self.win = curses.newwin(25, 50, 20, 20)

    myscreen.border(0)
    myscreen.addstr(25, 50, temp.INTRO)
    myscreen.refresh()
    myscreen.getch()

    curses.endwin()
