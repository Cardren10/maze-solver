from graphics.Window import Window
from graphics.Line import Line
from graphics.Point import Point
from graphics.Cell import Cell
from graphics.Maze import Maze


def main():
    win = Window(1200, 800)

    maze = Maze(10, 10, 12, 8, 30, 30, win)

    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
