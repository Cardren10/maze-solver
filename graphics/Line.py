from tkinter import Canvas
from graphics.Point import Point


class Line:
    def __init__(self, A: Point, B: Point) -> None:
        self.A = A
        self.B = B

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.A.x, self.A.y, self.B.x, self.B.y, fill=fill_color, width=2
        )
