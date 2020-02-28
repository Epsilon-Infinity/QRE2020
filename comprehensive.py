import utils

from copy import deepcopy
from collections import defaultdict


# {'book_scores':book_scores, days:'days', 'libraries':libraries}
def solver(inputs):
    books_so_far = set()
    libraries = inputs["libraries"]
    result = []
    days_left = inputs["days"]

    # Sorts libraries everytime and then remove duplicates
    while len(libraries)>0:
        libraries = sorted(libraries, key=lambda x: x.score(books_so_far, penalty=4))
        libraries[-1].remove_duplicates(books_so_far, days_left)
        if libraries[-1].books:
            books_so_far.update(libraries[-1].books.keys())
            days_left -= libraries[-1].signup_days
            result.append(libraries[-1])

        libraries.pop(-1)

    return result


if __name__ == "__main__":
    utils.solve_files('data', solver)
