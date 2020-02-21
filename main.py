import utils

from copy import deepcopy
from collections import defaultdict


# {'book_scores':book_scores, days:'days', 'libraries':libraries}
def solver(inputs):
    books_so_far = set()
    book_scores = inputs["book_scores"]
    libraries = inputs["libraries"]
    result = []

    while  len(libraries)>0:
        libraries = sorted(libraries, key=lambda x: x.score(books_so_far))
        result.append(libraries[-1])
        for book in libraries[-1].books.keys():
            books_so_far.add(book)
        libraries.pop(-1)

    return result


if __name__ == "__main__":
    utils.solve_files('data', solver)
