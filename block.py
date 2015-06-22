import random

shapes = [
    [
        (1, 1, 1, 1)
    ],
    [
        (1, 0), (1, 0), (1, 1)
    ],
    [
        (0, 1), (0, 1), (1, 1)
    ],
    [
        (0, 1), (1, 1), (1, 0)
    ],
    [
        (1, 1), (1, 1)
    ]
]


class Block:
    def __init__(self):
        self.shape = random.choice(shapes)
        self.position = (0, 0)

    @property
    def width(self):
        """
        Convenience for width of block
        :return: the height of the block
        """
        return len(self.shape[0])

    @property
    def height(self):
        return len(self.shape)

    def mask(self):
        """
        A matrix like mask is created which is used to interpolate with exisiting blocks.
        :return: a 2 dimensional matrix with the blocks positions as 1's and empty as 0's
        """
        m = [[0 for _ in range(20)] for _ in range(20)]
        for i, row in enumerate(self.shape):
            for j, element in enumerate(row):
                x = self.position[0] + i
                y = self.position[1] + j
                if x >= 20 or y >= 20:
                    return False, None
                m[x][y] = element
        return True, m

    def move_left(self, set_pos=False):
        """
        Moves the block left.
        :param set_pos: simulate only
        :return: result of operation
        """
        new_p = (self.position[0], self.position[1] - 1)

        if not (0 <= new_p[0] < 20 and 0 <= new_p[1] < 20):
            return False, None
        if set_pos:
            self.position = new_p
        return True, new_p

    def move_right(self, set_pos=False):
        """
        Move the block right
        :param set_pos: Simulate only.
        :return: The result of the operation.
        """
        new_p = (self.position[0], self.position[1] + 1)
        if not (0 <= (new_p[0] + self.height) < 20 and 0 <= (new_p[1] + self.width - 1) < 20):
            return False, None
        if set_pos:
            self.position = new_p
        return True, new_p

    def rotate_clockwise(self):
        """
        Rotate the block clockwise.
        :return: The result of the operation
        """
        new_shape = zip(*self.shape[::-1])
        if (self.position[1] + len(new_shape[0])) > 20 or (self.position[0] + len(new_shape)) > 20:
            return False
        self.shape = new_shape
        return True

    def rotate_counter(self):
        """
        Rotate the block counter clockwise.
        :return: The result of the opeartion.
        """
        new_shape = zip(*self.shape)[::-1]
        if (self.position[1] + len(new_shape[0])) > 20 or (self.position[0] + len(new_shape)) > 20:
            return False
        self.shape = new_shape
        return True

    def print_mask(self):
        """
        Convenience method to print the current mask.
        """
        _, m = self.mask()
        for row in m:
            p = []
            for e in row:
                p.append('-' if e == 0 else '*')
            print(''.join(p))

    def down(self):
        """
        Move the block down one position.
        """
        new_y = self.position[0] + 1
        if new_y > 20:
            raise RuntimeError('Moved outside. Should be detected')
        self.position = new_y, self.position[1]