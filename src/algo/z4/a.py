<<<<<<< HEAD
"""
zadanie1:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej
 połączeń wychodzących.
"""

from gen_train_data import generate_data


def print_destinations(destinations: list[list[int]]):
    for i, dest in enumerate(destinations):
        print(i, '->', dest)


def extract_destination_info(train_data: list[tuple[int, int]]):
    max_city = max([start for start, end in train_data])
    destinations = [[] for _ in range(max_city + 1)]
    for start, end in train_data:
        destinations[start].append(end)
    return destinations


def get_city_most_connections(train_data: list[tuple[int, int]]) -> int:
    destinations = extract_destination_info(train_data)
    destination_counts = [len(dest) for dest in destinations]
    return destination_counts.index(max(destination_counts))


if __name__ == '__main__':
    data = generate_data(50)
    mxcity = get_city_most_connections(data)
    print(mxcity)
=======
# from adir.f import foo
# from f import foo
# export PYTHONPATH=~/PycharmProjects/python1-2022
# from src.algo.z4.libs.f import foo
from libs.f import foo

# foo(10)

print('ok')

print('-------------')
with open('kadabra.txt') as f:
    print(f.readlines())
print('-------------')

print('uruchamiam funkcje')
print(foo(10))
>>>>>>> t1-dev
