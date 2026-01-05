"""At a lemonade stand, each lemonade costs $5.
Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays,
return true if you can provide every customer with the correct change, or false otherwise."""

from collections import defaultdict


def lemonade_change(bills: list[int]) -> bool:
    purse = defaultdict(int)

    for bill in bills:
        if bill == 5:
            purse[5] += 1

        elif bill == 10:
            if purse[5] >= 1:
                purse[5] -= 1
                purse[10] += 1
            else:
                return False

        elif bill == 20:
            # always better to pay with 10+5 instead of 3*5 if possible...
            if purse[10] >= 1 and purse[5] >= 1:
                purse[5] -= 1
                purse[10] -= 1
            elif purse[5] >= 3:
                purse[5] -= 3
            else:
                return False
            purse[20] += 1
    return True


assert lemonade_change(bills=[5, 10, 5, 5, 20])
assert not lemonade_change(bills=[5, 5, 10, 10, 20])
