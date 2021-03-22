# -*- coding: utf-8 -*-

import math
import random
import numpy as np

class Spin:
    def __init__(self, spin_type='primitive'):
        self.spin_type = spin_type


class Reel:
    def __init__(
            self,
            symbols,
            spin_type='primitive',
            min_num_full_turns=0,
            max_num_full_turns=200
    ):
        """

        :param symbols - list contains reel symbols:
        :param spin_type - primitive - only stop index, math_sim - and num of full turns, phys_sim
        use mass momentum, impulse momentum, friction force for realistic simulation (and in each case
        frontend play big role in realistic simulation:
        :param min_num_full_turns:
        :param max_num_full_turns:
        """
        self.symbols = symbols
        self.symbols_len = len(symbols)
        self.symbols_index = range(symbols)
        self.curr_state_index = 0
        self.curr_stop_index = None
        self.spin_type = spin_type
        self.spin_types = {
            'prmitive': self._spin_primitive,
            'math_sim': self._spin_math_simulation,
            'phys_sim': self._phys_simulation
        }
        self.curr_num_full_turns = 0
        self.min_num_full_turns = min_num_full_turns
        self.max_num_full_turns = max_num_full_turns

    def spin(self):
        self.curr_stop_index = self.spin_types[self.spin_type]
        self.curr_state_index = self.curr_stop_index
        return self.curr_stop_index

    def set_curr_state_index(self, state_index):
        self.curr_state_index = state_index

    def _spin_primitive(self):
        return random.randint(0, self.symbols_len - 1)

    def _spin_math_simulation(self):
        self.curr_num_full_turns = random.randint(
            self.min_num_full_turns,
            self.max_num_full_turns
        )
        return self._spin_primitive()

    def _spin_phys_simulation(self):
        pass


class SlotMachine:

    def __init__(
            self,
            reels=[[Reel(), Reel(), Reel()]],
            paylines=[[{(0, 0): '7'}, {(0, 1): '7'}, {(0, 2): '7'}]]
    ):
        """

        :param reels list of lists (rows) of reels (columns). Frame rows x columns. Complex shapes are
        not considered:
        :param paylines, list of lists of dicts. Dict key - (row, column) typle, value - symbol:
        """
        self.reels= reels
        self.max_reels_row_index = len(reels) + 1
        self.max_reels_column_index = len(reels[0]) + 1
        self.paylines = paylines



if __name__ == '__main__':
    slot_machine = SlotMachine()

