from Diary import Diary


class DiaryStatistics:
    """Statistics class."""
    def print_statistics(self):
        """Print statistics."""
        print(f"{self.counter}")
        lengths = [len(entry) for entry in self.diary_inputs]
        print(lengths)