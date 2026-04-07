class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self.status = 'LOCKED'
        self.entered_digits = []

    def enter_digit(self, digit):
        self.entered_digits.append(digit)
        current_step = len(self.entered_digits)
        correct_part = self.combination[:current_step]

        if self.entered_digits == correct_part:
            if len(self.entered_digits) == len(self.combination):
                self.status = 'OPEN'
            else:
                self.status = "".join(map(str, self.entered_digits))
        else:
            self.status = 'ERROR'

if __name__ == '__main__':
    cl = CombinationLock([1, 2, 3, 4, 5])
    print(cl.status)
    cl.enter_digit(1)
    print(cl.status)
    cl.enter_digit(2)
    cl.enter_digit(3)
    print(cl.status)
    cl.enter_digit(4)
    cl.enter_digit(5)
    print(cl.status)
    cl2 = CombinationLock([1, 2, 3])
    cl2.enter_digit(1)
    cl2.enter_digit(9)
    print(cl2.status)