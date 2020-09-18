#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

import timeit
import functools
import pstats
import cProfile


__author__ = "sondos got help from Joseph , gabby, and Daniel"
__refrences__ = "https://docs.python.org/2/library/profile.html"


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # raise NotImplementedError("Complete this decorator function")

    def wrapper(*args, **kwargs):

        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sort_by = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sort_by)

        ps.print_stats()

        return result
    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    if title in movies:
        return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


# find_duplicate_movies()


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    nums_repeat = 5
    nums_per_repeat = 3

    t = timeit.Timer(stmt="print(type(d))", setup="d = []")
    result = t.repeat(repeat=nums_repeat, number=nums_per_repeat)
    time_cost = min(result) / nums_per_repeat
    print(
        f"Best time across {nums_repeat} repeats of {nums_per_repeat} runs per repeat:{time_cost}")
    # return time_cost


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    timeit_helper()
