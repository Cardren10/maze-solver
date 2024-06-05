from tkinter import Tk, BOTH, Canvas
from graphics.Line import Line


class Window:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack()

        self.running = False

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(canvas=self._canvas, fill_color=fill_color)
