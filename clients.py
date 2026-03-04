"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        day_earnings = self.current_amount - self.starting_amount
        return day_earnings / self.account_age


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")

                name = parts[0]
                bank = parts[1]
                account_age = int(parts[2])
                starting_amount = int(parts[3])
                current_amount = int(parts[4])

                new_client = Client(name, bank, account_age, starting_amount, current_amount)

                clients.append(new_client)
    except FileNotFoundError:
        return []

    return clients


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    bank_people = read_from_file_into_list(filename)
    filtered_people = list(filter(lambda client: client.bank == bank, bank_people))
    return filtered_people


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with the largest earnings.
    """
    clients = read_from_file_into_list(filename)
    best_earner = None

    for client in clients:
        earnings = client.earnings_per_day()

        if earnings > 0:
            if best_earner is None:
                best_earner = client
            else:
                current_best_earnings = best_earner.earnings_per_day()
                if (earnings > current_best_earnings or (earnings == current_best_earnings and client.account_age < best_earner.account_age)):
                    best_earner = client

    return best_earner


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with the largest earnings.
    """
    clients = read_from_file_into_list(filename)
    worst_client = None

    for client in clients:
        earnings = client.earnings_per_day()

        if earnings < 0:
            if worst_client is None:
                worst_client = client
            else:
                current_worst_earnings = worst_client.earnings_per_day()

                if earnings < current_worst_earnings:
                    worst_client = client

                elif earnings == current_worst_earnings:
                    if client.account_age < worst_client.account_age:
                        worst_client = client

    return worst_client


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
