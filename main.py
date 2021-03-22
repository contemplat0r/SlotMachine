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

    def __init__(self, reils=[Reel(), Reel(), Reel()], paylines=[[0, 1, 2]]):
        pass


if __name__ == '__main__':
    slot_machine = SlotMachine()

