import pygame as pg
import random
import time
import assets.bubblesort as bs
import assets.mergesort as ms
import assets.quicksort as q
import assets.bogosort as bogo

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def is_sorted(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


class SortViz(object):
    # Width correlates to number of elem. and heigt = the range of size
    def __init__(self, function, width=1920, height=1080, linesize=2, nested=False):
        """

        :param function: the sorting function returning
        :param width: Int representing window width
        :param height: Int representing window height
        :param linesize: Int
        :param nested: Bool representing if the step list has sublist(s), e.g step[0][[1,2] , 4, 5, 3]
        """
        pg.init()

        # Pygame settings
        self.FPS = 50
        self.clock = pg.time.Clock()
        self.w = width
        self.h = height


        self.running = True
        self.updating = False
        self.sorted = True

        # Line settings
        self.linesize = linesize
        self.linecolor = WHITE
        self.linecolor2 = GREEN
        self.linehiglight = RED

        # List settings
        self.listsize = int(self.w / self.linesize)
        self.list = self.list_gen()
        self.function = function
        self.steps, self.colorsteps = self.function(self.list)
        self.stepindex = 0
        self.nested = nested
        self.step = [j for i in self.steps[self.stepindex] for j in i] if self.nested else self.steps[self.stepindex]

        # Draw complete
        self.dc = False  # Draw complete
        self.completeindex = 0

        # Setup pygame window
        self.screen = pg.display.set_mode((self.w, self.h))
        pg.display.set_caption(f'Sorting Visualization: Sorting a list containing {self.listsize} elements using '
                               f'function "{self.function.__name__}" '
                               'PRESS SPACE TO START')
        pg.display.set_icon(pg.image.load('assets/icon.png'))

    def list_gen(self):
        temp_list = []
        for u in range(self.listsize):
            r = random.randrange(1, self.h)
            temp_list.append(r)
        return temp_list

    def start(self):
        self.draw()
        time.sleep(1)
        self.run()

    def run(self):
        # The run loop
        import time

        while self.running:
            # Tickrate / FPS rate
            self.clock.tick(self.FPS)
            self.events()
            print(self.updating)
            if self.updating:

                self.sorted = is_sorted(self.step)
                if not self.sorted:
                    self.sort()
                    self.draw()


                elif self.sorted and not self.dc:
                    self.draw_complete()

                else:
                    self.updating = False
                    self.run_complete()

    def run_complete(self):
        # When complete => do not update or draw
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
                if event.key == pg.K_SPACE:
                    if self.running:
                        self.updating = True if not self.updating else False

    def sort(self):

        if self.nested:
            self.step = [j for i in self.steps[self.stepindex] for j in i]

        else:
            self.step = self.steps[self.stepindex]
        self.stepindex += 1

    def draw_complete(self):  # Rita klart

        for i in range(len(self.step)):
            pg.draw.line(self.screen, self.linecolor2, (i * self.linesize, self.h),
                         (i * self.linesize, self.h - self.step[i]), self.linesize)
            self.dc = True

        pg.draw.line(self.screen, self.linecolor2, (self.completeindex * self.linesize, self.h),
                     (self.completeindex * self.linesize, self.h - self.step[self.completeindex]), self.linesize)
        pg.display.flip()

    def draw(self):
        # Ett steg och rita
        self.screen.fill(BLACK)

        for i in range(len(self.step)):
            # print(i, val)
            pg.draw.line(self.screen, self.linecolor, (i * self.linesize, self.h),
                         (i * self.linesize, self.h - self.step[i]), self.linesize)

        pg.display.flip()


s = SortViz(bs.bubble_sort)
s.start()

s2 = SortViz(ms.merge_sort, nested=True)
s2.start()

s3 = SortViz(q.quicksort)
s3.start()
