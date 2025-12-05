"""Annettuna on sanaruudukko ja tehtäväsi on etsiä sieltä sanoja. Sana voi kulkea pysty-,
vaaka- tai vinosuunnassa etuperin tai takaperin.

Toteuta tiedostoon wordgrid.py luokka WordFinder, jossa on seuraavat metodit:

    set_grid: metodille annetaan sanaruudukon sisältö listana, joka esittää ruudukon rivit merkkijonoina
    count: laskee annetun sanan esiintymiskerrat ruudukossa

Jos sana voidaan lukea useaan suuntaan samoista ruudukon kirjaimista,
metodin count tulee laskea tällaiset esiintymät vain yhtenä esiintymiskertana.

Luokkasi toimintaa testataan erilaisilla ruudukoilla. Jokaisessa ruudukossa leveys ja korkeus on enintään 20 merkkiä.
Jokainen merkki on kirjain välillä A–Z."""



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

