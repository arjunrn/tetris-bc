from copy import deepcopy
import random


class Arena:
    def __init__(self):
        self.block = None
        self.area = [[0 for _ in range(20)] for _ in range(20)]

    def __str__(self):
        printable = []
        if self.block:
            _, mask = self.block.mask()
            merged = self.merge(mask)
        else:
            merged = self.area
        for row in merged:
            printable.append(''.join(['*', ''.join(['*' if e == 1 else ' ' for e in row]), '*']))
        printable.append('*' * 22)
        return '\n'.join(printable)

    def add_block(self, block):
        """
        The block to be added to the arena is passed here.
        :param block: The `block.Block` type object.
        :return: True if the block can be added. False otherwise
        """
        if self.block is not None:
            raise RuntimeError('Existing block in arena')
        block.position = block.position[0], random.randint(0, 20 - block.width)
        _, mask = block.mask()
        for i in range(20):
            for j in range(20):
                if self.area[i][j] == 1 and mask[i][j] == 1:
                    return False
        self.block = block
        return True

    def move_right(self):
        """

        :return:
        """
        dummy = deepcopy(self.block)
        dummy.move_right(True)
        if self.conflict(dummy.mask()[1]):
            return False
        result, _ = self.block.move_right(True)
        return result

    def move_left(self):
        dummy = deepcopy(self.block)
        dummy.move_left(True)
        if self.conflict(dummy.mask()[1]):
            return False
        result, _ = self.block.move_left(True)
        return result

    def rotate_cc(self):
        dummy = deepcopy(self.block)
        dummy.rotate_counter()
        if self.conflict(dummy.mask()[1]):
            return False
        return self.block.rotate_counter()

    def rotate(self):
        dummy = deepcopy(self.block)
        dummy.rotate_clockwise()
        if self.conflict(dummy.mask()[1]):
            return False
        return self.block.rotate_clockwise()

    def step(self):
        dummy_block = deepcopy(self.block)
        dummy_block.down()
        _, mask = dummy_block.mask()
        if self.conflict(mask):
            self.area = self.merge(self.block.mask()[1])
            self.block = None
            return

        self.block.down()
        if self.reached_bottom():
            self.area = self.merge(self.block.mask()[1])
            self.block = None

    def conflict(self, mask):
        for i in range(20):
            for j in range(20):
                if self.area[i][j] == 1 and mask[i][j] == 1:
                    return True
        return False

    def merge(self, mask):
        merged = [[0 for _ in range(20)] for _ in range(20)]
        for i in range(20):
            for j in range(20):
                merged[i][j] = mask[i][j] + self.area[i][j]
        return merged

    def reached_bottom(self):
        if self.block.height + self.block.position[0] >= 20:
            return True
        else:
            return False