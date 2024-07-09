import sys


def get_min_steps(nums: list[int]) -> int:
    """A function that outputs the minimum number of moves
    required to bring all elements to the same number."""

    sort_nums = sorted(nums)
    steps_count = 0
    mid = nums[len(sort_nums) // 2]

    while sort_nums.count(mid) != len(sort_nums):
        for index, el in enumerate(sort_nums):
            if el == mid:
                continue
            elif el < mid:
                sort_nums[index] = el + 1
                steps_count += 1
            elif el > mid:
                sort_nums[index] = el - 1
                steps_count += 1
    return steps_count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python task4.py <input_file>')

        sys.exit(1)

    with open(sys.argv[1], 'r') as file:
        data = [int(el) for el in file.read().split()]
        print(get_min_steps(data))
