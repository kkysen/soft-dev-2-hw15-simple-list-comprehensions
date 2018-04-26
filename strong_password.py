# Khyber Sen
# SoftDev2 pd7
# K15 -- Do you even list?
# 2018-04-25

from __future__ import print_function

import random

from typing import List

import string

all_criterias = (
    "".join(map(str, xrange(10))),
    string.ascii_lowercase,
    string.ascii_uppercase,
    ".?!&#,;:-_*",
)


def password_strength(password, criterias=all_criterias):
    # type: (str) -> int
    return 10 - 10 // sum(1 for criteria in criterias if not set(password).isdisjoint(set(criteria)))


def check_password_strength(password):
    # type: (str) -> bool
    criterias = all_criterias[0:-1]
    return password_strength(password, criterias=criterias) > 10 // len(criterias)


def test(passwords):
    # type: (List[str]) -> None
    map(print, ((password, check_password_strength(password)) for password in passwords))
    return None


if __name__ == '__main__':
    test([
        "hello",  # False
        "1234",  # False
        "Hello, 5 Worlds!",  # True
        "Hello, 5 Worlds",  # True
    ])
    print()
    
    # Test 10000 random passwords to make sure they have the right strength
    print(all(10 - 10 // length == password_strength(
        "".join(random.choice(all_criterias[i]) for i in xrange(length))
    ) for length in (random.randrange(1, len(all_criterias)) for x in xrange(10000)))
          )
