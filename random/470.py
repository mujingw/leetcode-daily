# The rand7() API is already defined for you.
from random import randint


def rand7():
    return randint(1, 7)
    # @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        def get_rand():
            r1 = rand7()
            r2 = rand7()

            return r1 + (r2 - 1) * 7

        res = get_rand()

        while res > 40:
            res = get_rand()

        return 10 if res % 10 == 0 else res % 10
