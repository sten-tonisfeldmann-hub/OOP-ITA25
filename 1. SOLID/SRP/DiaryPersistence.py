from Diary import Diary

class DiaryPersistence:
    """class DiaryPersistence:"""
    @staticmethod
    def save_to_file(diary, filename):
        """Save diary to file."""
        with open(filename, 'w') as f:
            f.write(str(diary))

    @staticmethod
    def load_from_file(filename):
        new_diary = Diary()
        with open(filename, 'r') as f:
            for line in f:
                clean_line = line.strip()
                if clean_line:
                    new_diary.add_entry(clean_line)
        return new_diary