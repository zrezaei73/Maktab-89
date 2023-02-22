from typing import List

def sum_even_numbers(numbers: List[int]) -> int:
    """
    sums all even numbers in a list of integers.
    Args:
        numbers: A list of integers.

    Returns:
        The sum of all even numbers in the list.

    """
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum