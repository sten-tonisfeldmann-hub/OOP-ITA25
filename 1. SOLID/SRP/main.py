from Diary import Diary
from DiaryPersistence import DiaryPersistence
from DiaryStatistics import DiaryStatistics

if __name__ == "__main__":

    # Loome Diary objekti (ainult andmed + äriloogika)

    diary = Diary()

    diary.add_entry("Täna oli ilus ilm.")

    diary.add_entry("Õppisin programmeerimist.")

    diary.add_entry("SRP on tegelikult väga loogiline.")

    print("---- DIARY SISU ----")

    print(diary)

    print()

    # Statistika (kasutame staticmethod'e)

    print("---- STATISTIKA ----")

    DiaryStatistics.print_statistics(diary)

    print()

    # Salvestame faili (EI loo Persistence objekti)

    filename = "diary.txt"

    DiaryPersistence.save_to_file(diary, filename)

    print(f"Salvestatud faili: {filename}")

    print()

    # Laeme uuesti failist

    loaded_diary = DiaryPersistence.load_from_file(filename)

    print("---- FAILIST LAETUD ----")

    print(loaded_diary)

    print()

    # Kontrollime, kas loendur töötab edasi

    loaded_diary.add_entry("See lisati pärast laadimist.")

    print("---- PÄRAST UUT LISAMIST ----")

    print(loaded_diary)