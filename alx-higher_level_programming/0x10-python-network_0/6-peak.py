#!/usr/bin/python3
"""This module contains a program to find peaks from a list_of_integers"""


def find_peak(seq=[]):
    """Funnction to find the first peak in fastest time"""
    n = len(seq)

    if n == 0:
        return None

    if n == 1:
        return seq[0]

    if seq[0] > seq[1]:
        return seq[0]

    if seq[-1] > seq[-2]:
        return seq[-1]

    for i in range(1, n - 1):
        if seq[i] > seq[i - 1] and seq[i] > seq[i + 1]:
            return seq[i]


if __name__ == "__main__":
    find_peak()
