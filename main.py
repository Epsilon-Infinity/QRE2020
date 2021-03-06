import utils

from copy import deepcopy
from collections import defaultdict


# {'book_scores':book_scores, days:'days', 'libraries':libraries}
def solver(inputs):
    books_so_far = set()
    libraries = inputs["libraries"]
    result = []

    while len(libraries)>0:
        libraries = sorted(libraries, key=lambda x: x.score(books_so_far, penalty=2))
        result.append(libraries[-1])
        books_so_far.update(libraries[-1].books.keys())
        libraries.pop(-1)

    return result


if __name__ == "__main__":
    utils.solve_files('data', solver)
