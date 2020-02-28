import utils

from copy import deepcopy
from collections import defaultdict


# {'book_scores':book_scores, days:'days', 'libraries':libraries}
def solver(inputs):
    books_so_far = set()
    libraries = inputs["libraries"]

    # sort libraries
    libraries = sorted(libraries, key=lambda x: x.score(books_so_far))

    return libraries


if __name__ == "__main__":
    utils.solve_files('data', solver)
