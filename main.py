import asyncio
import time
import curses


TIC_TIMEOUT = 0.1

async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(10):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(10):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


def draw(canvas):
    row, column = (10, 25)
    curses.curs_set(False)
    canvas.border()
    coroutines = [blink(canvas, row, column, ' *'*step) for step in range(6)]
    while True:
        for coroutine in coroutines.copy():
            coroutine.send(None)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
