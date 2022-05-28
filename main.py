from gol import GOL
from processor import InputProcessor
import time
import sys


def pprint(data):
    print(f'Generation {data["generation"]}:')
    print(f'{data["row"]} {data["col"]}')

    for i in range(data['row']):
        for j in range(data['col']):
            print('*' if GOL.get_key(i, j) in data['cells'] else '.', end='')
        print()
    print()


if __name__ == '__main__':
    assert len(sys.argv) == 2

    input_data = InputProcessor.process_input(sys.argv[1])
    gol = GOL(
        rows=input_data['rows'],
        cols=input_data['cols'],
        cells=input_data['cells'],
        generation=input_data['generation'],
    )
    while True:
        gol.round()
        data = gol.serialize()
        pprint(data)
        time.sleep(2)
