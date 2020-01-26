"""
Python BubbleSort Visualizer by Luca Zani
"""

import random

import pygame

pygame.init()
pygame.display.init()


class Visualizer:

    def __init__(self):

        self.width = 600
        self.height = 400
        self.fps = 30
        self.values = [random.randrange(1, self.height) for values in range(self.width // 10)]
        self.sorted = False
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Bubble Sort")

    def bubbleSort(self):
        """
        Game Loop
        :return: None
        """
        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if not self.sorted:
                for i in range(len(self.values)):
                    for j in range(len(self.values) - 1):
                        if self.values[j] > self.values[j + 1]:
                            self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]
                        self.update(j+1)
                        #pygame.time.wait(100)  # uncomment to slow down
                self.sorted = True
                self.update(0)
        pygame.quit()

    def update(self, current_line):
        """
        Updates the window and draw the lines
        :param current_line: index, line examinated
        :return: None
        """
        self.screen.fill((0, 0, 0))
        line_width = self.width // len(self.values)

        for line in range(len(self.values)):
            if line == current_line:
                pygame.draw.line(self.screen, (255, 0, 0), (current_line * line_width, self.height - self.values[current_line]), (current_line * line_width, self.height), line_width - 1)
            else:
                pygame.draw.line(self.screen, (255, 255, 255), (line * line_width, self.height - self.values[line]), (line * line_width, self.height), line_width - 1)

        pygame.display.flip()


v = Visualizer()
v.bubbleSort()
# Ho aggiunto un commento di prova
