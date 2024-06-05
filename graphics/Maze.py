from graphics.Cell import Cell
from graphics.Window import Window
import time
import random


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed:
            self._seed = random.seed(seed)
        self._create_cells()
        self._break_enterance_and_exit()

    def _create_cells(self) -> None:
        """create a multidimensional array filled with cells."""
        for row in range(self._num_rows):
            self._cells.append([])
            for cell in range(self._num_cols):
                self._cells[row].append(None)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[row][col] = self._draw_cell(row + 1, col + 1)
                cell = self._cells[row][col]
                cell.draw()
                self._animate()

    def _draw_cell(self, i, j) -> Cell:
        """Calculate the x,y values for a given cell. i is the row value of the cell and j is the column value."""
        win_height = self.win.height
        win_width = self.win.width
        half_maze_height = self._cell_size_y * self._num_rows
        half_maze_width = self._cell_size_x * self._num_cols
        win_center = (
            (win_width - half_maze_width) // 2,
            (win_height - half_maze_height) // 2,
        )

        maze_left = win_center[0] - ((self._num_cols / 2) * (self._cell_size_x / 2))
        maze_top = win_center[1] + ((self._num_rows / 2) * (self._cell_size_y / 2))

        x1 = maze_left + ((i * self._cell_size_x) - self._cell_size_x)
        y1 = maze_top + ((j * self._cell_size_y) - self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 - self._cell_size_y
        has_left_wall = True
        has_right_wall = True
        has_top_wall = True
        has_bottom_wall = True
        win = self.win

        cell = Cell(
            x1,
            y1,
            x2,
            y2,
            has_left_wall,
            has_right_wall,
            has_top_wall,
            has_bottom_wall,
            win,
        )
        return cell

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_enterance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[0][0].draw()
        self._cells[self._num_rows - 1][self._num_cols - 1].has_right_wall = False
        self._cells[self._num_rows - 1][self._num_cols - 1].draw()
