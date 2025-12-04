class WordFinder:
    def set_grid(self, grid):
        self.g = grid

    def count(self, word):
        cnt = 0
        cols = len(self.g[0])
        rows = len(self.g)
        L = len(word)
        first = word[0]
        for r in range(rows):
            for c in range(cols):
                if first == self.g[r][c]:
                    if c + L <= cols and word == self.g[r][c:c+L]:
                        cnt += 1
        return cnt

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7
    # print(finder.count("TA")) # 13
    # print(finder.count("RITARI")) # 3
    # print(finder.count("A")) # 8
    # print(finder.count("AA")) # 6
    # print(finder.count("RAITA")) # 0

"""
Реалізуйте клас WordFinder у файлі wordgrid.py за допомогою таких методів:

    set_grid: метод отримує вміст слова grid у вигляді списку, який представляє рядки сітки як рядки.
    count: підраховує кількість входжень заданого слова в сітці

Якщо слово можна прочитати в кількох напрямках з тих самих літер у сітці, метод count повинен вважати такі входження лише одним.

Ваш клас буде протестовано на різних сітках. Кожна сітка має максимальну ширину та висоту 20 символів. Кожен символ – це літера від A до Z."""