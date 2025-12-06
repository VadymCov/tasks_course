"""Given a word grid, your task is to find words in it. The word can go vertically,
horizontally, or diagonally, forwards or backwards.

Implement a class WordFinder in the file wordgrid.py with the following methods:

set_grid: the method is given the contents of the word grid as a list, which represents the rows of the grid as strings
count: counts the occurrences of the given word in the grid

If the word can be read in multiple directions from the same letters in the grid,
the method count should count such occurrences as only one occurrence.

The functionality of your class will be tested on different grids. Each grid has a maximum width and height of 20 characters.
Each character is a letter from A to Z."""



class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.derections = [
            (0, 1), (0, -1),
            (-1, 0), (1, 0),
            (+1, +1), (-1, -1),
            (-1, +1), (+1, -1)
        ]

    def count(self, word):
        cnt = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == word[0]:
                    for dr, dc in self.derections:
                        letter_cnt = 1
                        rn, cn = r, c
                        for k in range(1, len(word)):
                            rn = r + k * dr
                            cn = c + k * dc
                            if (
                                    0 <= rn < self.rows and
                                    0 <= cn < self.cols and
                                    self.grid[rn][cn] ==  word[k]
                            ):
                                continue
                            else:
                                break
                        else:
                            unique_key = tuple(sorted([(r,c),(rn, cn)]))
                            cnt.add(unique_key)
        return len(cnt)


if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0

