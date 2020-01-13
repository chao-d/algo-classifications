# Any number will be called a happy number if, after repeatedly replacing it
# with a number equal to the sum of the square of all of its digits, leads us
# to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead,
# they will be stuck in a cycle of numbers which does not include ‘1’.


def find_happy_number(n):
    if n == 1:
        return True
    slow, fast = n, get_next(n)
    while slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        if fast == 1 or slow == 1:
            return True
    return False


def get_next(n):
    res = 0
    while n:
        digit = n % 10
        res += digit * digit
        n //= 10
    return res
