"""Diary."""

class Diary:
    """Diary class."""

    def __init__(self):
        """Diary constructor."""
        self.diary_inputs = []
        self.counter = 0


    def add_entry(self, text):
        """Add entry to the diary."""
        self.diary_inputs.append(f"{self.counter}: {text}")
        self.counter += 1


    def remove_entry(self,index):
        """Remove entry from the diary."""
        self.diary_inputs.pop(index)


    def __str__(self):
        return "\n".join(self.diary_inputs)