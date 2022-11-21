import time
import curses


def draw(canvas):
	row, column = (10, 25)
	curses.curs_set(False)
	canvas.border()
	while True:
		canvas.addstr(row, column, '*')
		canvas.refresh()
		time.sleep(2)
		canvas.addstr(row, column, '*', curses.A_BOLD)
		canvas.refresh()
		time.sleep(2)
		canvas.addstr(row, column, '*', curses.A_DIM)
		canvas.refresh()
		time.sleep(2)


if __name__ == '__main__':
	curses.update_lines_cols()
	curses.wrapper(draw)
