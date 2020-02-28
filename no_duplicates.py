import utils

from copy import deepcopy
from collections import defaultdict


# {'book_scores':book_scores, days:'days', 'libraries':libraries}
def solver(inputs):
    books_so_far = set()
    libraries = inputs["libraries"]
    days_left = inputs["days"]

    # sort libraries
    libraries = sorted(libraries, key=lambda x: x.score(books_so_far))

    # remove duplicate books from library
    for library in libraries:
        library.remove_duplicates(books_so_far, days_left)
        if not library.books:
            libraries.remove(library)
        else:
            books_so_far.update(library.books.keys())
            days_left -= library.signup_days
        print(f"{days_left} days left")

    return libraries


if __name__ == "__main__":
    utils.solve_files('data', solver)
