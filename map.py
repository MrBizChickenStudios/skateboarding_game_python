from constants import *
import pygame
import block
import rail
import ramp



class Map(object):

    def __init__(self):
        self.lines = []
        self.blocks = pygame.sprite.Group()
        self.player_location = (0, 0)

    def load(self, map_file):
        with open(map_file, "r") as map:
            self.lines = map.readlines()


        # remove comments from map map_file

        self.lines = [line for line in self.lines if "#" not in line]


        r = 0
        for r in range(len(self.lines)):
            c = 0
            for c in range(len(self.lines[r])):
                # print(f"R:{r * BLOCK_SIZE}   C:{c * BLOCK_SIZE}  char:{self.lines[r][c]}")  # Output will be a list of lines
                tile = self.lines[r][c]

                if tile =="R":
                    self.blocks.add(rail.Rail(c * BLOCK_SIZE, r * BLOCK_SIZE))
                if tile =="B":
                    self.blocks.add(block.Block(c * BLOCK_SIZE, r * BLOCK_SIZE))
                if tile ==">":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "left"))
                if tile =="<":
                    self.blocks.add(ramp.Ramp(c * BLOCK_SIZE, r * BLOCK_SIZE, "right"))
                if tile =="P":
                    self.player_location = (c * BLOCK_SIZE, r * BLOCK_SIZE)

        return self.blocks
