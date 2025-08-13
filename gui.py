import curses

class Gui:
  def __init__(s):
    s.scr = curses.initscr()
    s.bx , s.by = 0, 0
    s.ex, s.ey  = curses.COLS - 1, curses.LINES - 1
    s.win = curses.newwin(s.ex, s.ey, s.bx, s.by)

  def initialize(s):
    pass
  def draw(s):
    #s.scr.clear() clears screen
    #s.scr.refresh() refreshes screen
    pass