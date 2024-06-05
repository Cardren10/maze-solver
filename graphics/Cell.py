from graphics.Point import Point
from graphics.Window import Window
from graphics.Line import Line


class Cell:

    def __init__(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        has_left_wall: bool,
        has_right_wall: bool,
        has_top_wall: bool,
        has_bottom_wall: bool,
        win: Window = None,
        visited: bool = False,
    ) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = visited

    def draw(self) -> None:
        """Draw the cell in the window."""
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(top_left.x, bottom_right.y)
        top_right = Point(bottom_right.x, top_left.y)

        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line, "black")

        if not self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line, "white")
        if not self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line, "white")
        if not self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line, "white")
        if not self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        """Draw a line from the center of this cell to the center of another cell."""
        # get the center of the current cell.
        self_center_x = (self._x1 + self._x2) // 2
        self_center_y = (self._y1 + self._y2) // 2
        self_center = Point(self_center_x, self_center_y)

        # get the center of the next cell
        to_center_x = (to_cell._x1 + to_cell._x2) // 2
        to_center_y = (to_cell._y1 + to_cell._y2) // 2
        to_center = Point(to_center_x, to_center_y)

        # draws the line between the two centers
        color = "red"
        if undo:
            color = "gray"
        line = Line(self_center, to_center)
        self._win.draw_line(line, color)
