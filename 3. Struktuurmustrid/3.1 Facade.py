import random


class Generator:
    def generate(self, count):
        return random.sample(range(1, 10), count)

class Splitter:
    def split(self, matrix):
        size = len(matrix)
        result = []
        result.extend(matrix)
        for c in range(size):
            result.append([matrix[r][c] for r in range(size)])
        result.append([matrix[i][i] for i in range(size)])
        result.append([matrix[i][size - i - 1] for i in range(size)])
        return result

class Verifier:
    def verify(self, lists):
        if not lists:
            return False
        target_sum = sum(lists[0])
        for l in lists:
            if sum(l) != target_sum:
                return False
        return True

class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            nums = self.generator.generate(size * size)
            square = []
            for i in range(0, len(nums), size):
                square.append(nums[i:i + size])
            parts = self.splitter.split(square)
            if self.verifier.verify(parts):
                return square

if __name__ == '__main__':
    gen = MagicSquareGenerator()
    square = gen.generate(3)

    print("Leitud maagiline ruut:")
    for row in square:
        print(row)