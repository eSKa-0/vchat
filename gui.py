import curses

class Gui:
  def __init__(s):
    s.scr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    s.scr.keypad(True)
    s.bx = 0
    s.by = 0
    s.ex = curses.COLS - 1
    s.ey = curses.LINES - 1
    #s.win = curses.newwin(s.ex, s.ey, s.bx, s.by)

  def initialize(s):
    pass
  def draw(s):
    #s.scr.clear() clears screen
    #s.scr.refresh() refreshes screen
    # Clear screen
    s.scr.clear()
    s.scr.addstr(5, 5, "Key: (Press Key)")
    # This raises ZeroDivisionError when i == 10.
    while True:
      key= s.scr.getkey()
      s.scr.clear()
      try:
        s.scr.addstr(5, 5, f"Key: {ord(key)}")
      except:
        s.scr.addstr(5, 5, f"Key: {key}")