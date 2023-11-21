from pickle import dump
from abc import ABC, abstractmethod


class Mixin(object):

    @staticmethod
    def display_data(sort_list: list):
        print(f'Sort list:\n>  {sort_list}')

    @staticmethod
    def save_data(sort_list: list) -> None:
        name_list = input('Write name of document, please: ')
        with open(f'{name_list}.dat', 'wb') as file:
            dump(sort_list, file)
        print(f'Data was saved!')


# ===================================================


class SortManager(ABC):

    def __init__(self, sort_name: str):
        self._sort_name = sort_name

    @staticmethod
    @abstractmethod
    def sort(unsorted_list) -> list:
        pass


class BubbleSortManager(SortManager, Mixin):

    def __init__(self):
        super().__init__("Sort by bubble method:")

    @staticmethod
    def sort(unsorted_list):
        for i in range(0, len(unsorted_list) - 1):
            for j in range(len(unsorted_list) - 1):
                if unsorted_list[j] > unsorted_list[j + 1]:
                    temp = unsorted_list[j]
                    unsorted_list[j] = unsorted_list[j + 1]
                    unsorted_list[j + 1] = temp
        return unsorted_list


class SelectionSortManager(SortManager, Mixin):

    def __init__(self):
        super().__init__("Sort by selection method:")

    @staticmethod
    def sort(unsorted_list) -> list:
        for i in range(0, len(unsorted_list) - 1):
            smallest = i
            for j in range(i + 1, len(unsorted_list)):
                if unsorted_list[j] < unsorted_list[smallest]:
                    smallest = j
            unsorted_list[i], unsorted_list[smallest] = unsorted_list[smallest], unsorted_list[i]
        return unsorted_list


class InsertionSortManager(SortManager, Mixin):

    def __init__(self):
        super().__init__("Sort by insertion method:")

    @staticmethod
    def sort(unsorted_list) -> list:
        for i in range(1, len(unsorted_list)):
            temp = unsorted_list[i]
            j = i - 1
            while j >= 0 and temp < unsorted_list[j]:
                unsorted_list[j + 1] = unsorted_list[j]
                j = j - 1
            unsorted_list[j + 1] = temp
        return unsorted_list
