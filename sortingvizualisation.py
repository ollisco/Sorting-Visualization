import pygame as pg
import random
import Sort4viz.bubblesort4pygame as bs
import Sort4viz.mergesort as ms

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


def is_sorted(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


class SortViz(object):
    # Width correlates to number of elem. and heigt = the range of size
    def __init__(self, function, width=1000, height=800):
        pg.init()
        self.FPS = 500
        self.clock = pg.time.Clock()
        self.w = width
        self.h = height
        self.listsize = self.w
        self.screen = pg.display.set_mode((self.w, self.h))
        pg.display.set_caption('Sorting viz')
        self.lista = self.list_gen()
        self.running = True
        self.sorted = True
        self.dc = False
        self.linecolor = WHITE
        self.linecolor2 = GREEN
        self.function = function
        self.runc = False

    def list_gen(self):
        temp_list = []
        for u in range(self.listsize):
            r = random.randrange(1, self.h)
            temp_list.append(r)
        return temp_list

    def run(self):
        # Loop
        while self.running:
            # Rät FPS eller Tick/s
            self.clock.tick(self.FPS)
            # Kollar om man stänger fönstret
            self.events()

            # Kollar om sorerat
            self.sorted = is_sorted(self.lista)
            if not self.sorted:
                self.sort()
                self.draw()


            elif self.sorted and not self.dc:
                self.draw_complete()

            else:
                self.run_complete()

    def run_complete(self):
        # When complete => dont update or draw
        while self.running:
            self.events()

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.running:
                    self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.running:
                        self.running = False

    def sort(self):
        self.lista = self.function(self.lista)

    def draw_complete(self):  # Rita klart
        for i, val in enumerate(self.lista):
            pg.draw.line(self.screen, self.linecolor2, (i, self.h), (i, self.h - val), 1)
            self.dc = True
        pg.display.flip()

    def draw(self):
        # Ett steg och rita
        self.screen.fill(BLACK)

        for i, val in enumerate(self.lista):
            # print(i, val)
            pg.draw.line(self.screen, self.linecolor, (i, self.h), (i, self.h - val), 1)
        pg.display.flip()


# s = SortViz(bogo.bogosort)
#s = SortViz(bs.bubble_sort)
# s = SortViz(ins.qqq)
# s = SortViz(ins.ollesort)
s = SortViz(ms.merge_sort)

# Startar game loopen
s.run()
