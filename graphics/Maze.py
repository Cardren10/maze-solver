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
        self._break_walls(0, 0)
        self._reset_visited_cells()

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
        self._animate()
        self._cells[self._num_rows - 1][self._num_cols - 1].has_right_wall = False
        self._cells[self._num_rows - 1][self._num_cols - 1].draw()
        self._animate()

    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if self._cells[i - 1][j]:
                if self._cells[i - 1][j].visited == False:
                    to_visit.append("w")
            if self._cells[i][j + 1]:
                if self._cells[i][j + 1].visited == False:
                    to_visit.append("n")
            if self._cells[i + 1][j]:
                if self._cells[i + 1][j].visited == False:
                    to_visit.append("e")
            if self._cells[i][j - 1]:
                if self._cells[i][j - 1].visited == False:
                    to_visit.append("s")
            if len(to_visit) == 0:
                return
            else:
                if 0 <= i <= self._num_rows and 0 <= j <= self._num_cols:
                    direction = self._rand_direction(to_visit)
                    if direction == "w":
                        self._cells[i][j].has_left_wall = False
                        self._cells[i - 1][j].has_right_wall = False
                        self._cells[i][j].draw()
                        self._animate()
                        self._cells[i - 1][j].draw()
                        self._animate()
                        self._break_walls(i - 1, j)
                    if direction == "n":
                        self._cells[i][j].has_top_wall = False
                        self._cells[i][j + 1].has_bottom_wall = False
                        self._cells[i][j].draw()
                        self._animate()
                        self._cells[i][j + 1].draw()
                        self._animate()
                        self._break_walls(i, j + 1)
                    if direction == "e":
                        self._cells[i][j].has_right_wall = False
                        self._cells[i + 1][j].has_left_wall = False
                        self._cells[i][j].draw()
                        self._animate()
                        self._cells[i + 1][j].draw()
                        self._animate()
                        self._break_walls(i + 1, j)
                    if direction == "s":
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[i][j - 1].has_top_wall = False
                        self._cells[i][j].draw()
                        self._animate()
                        self._cells[i][j - 1].draw()
                        self._animate()
                        self._break_walls(i, j - 1)
                else:
                    continue

    def _rand_direction(self, list: list):
        length = len(list)
        rand = random.randrange(0, length)
        return list[rand]

    def _reset_visited_cells(self):
        for row in self._cells:
            for col in row:
                self._cells[row][col].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self._num_rows][self._num_cols]:
            return True
        if (
            self._cells[i - 1][j] is not None
            and self._cells[i - 1][j].visited == False
            and self._cells[i - 1][j].has_right_wall == False
        ):
            # west
            self._cells[i][j].draw_move([i - 1][j])
            self._animate()
            if self._solve_r(i - 1, j) == True:
                return True
            else:
                self._cells[i - 1][j].draw_move(self._cells[i][j], True)
                self._animate()
        if (
            self._cells[i][j + 1] is not None
            and self._cells[i][j + 1].visited == False
            and self._cells[i][j + 1].has_bottom_wall == False
        ):
            # north
            self._cells[i][j].draw_move([i][j + 1])
            self._animate()
            if self._solve_r(i, j + 1) == True:
                return True
            else:
                self._cells[i][j + 1].draw_move(self._cells[i][j], True)
                self._animate()
        if (
            self._cells[i + 1][j] is not None
            and self._cells[i + 1][j].visited == False
            and self._cells[i + 1][j].has_left_wall == False
        ):
            # east
            self._cells[i][j].draw_move([i + 1][j])
            self._animate()
            if self._solve_r(i + 1, j) == True:
                return True
            else:
                self._cells[i + 1][j].draw_move(self._cells[i][j], True)
                self._animate()
        if (
            self._cells[i][j - 1] is not None
            and self._cells[i][j - 1].visited == False
            and self._cells[i][j - 1].has_top_wall == False
        ):
            # south
            self._cells[i][j].draw_move([i][j - 1])
            self._animate()
            if self._solve_r(i, j - 1) == True:
                return True
            else:
                self._cells[i][j - 1].draw_move(self._cells[i][j], True)
                self._animate()
