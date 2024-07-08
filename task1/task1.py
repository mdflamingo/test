def create_array(size: int) -> list[int]:
    """Creates a list with numbers of the size 'n'."""
    array = [el for el in range(1, size + 1)]

    return array


def get_a_path(step: int, array: list[int]) -> str:
    """A function that outputs a path along which,
    moving with an interval of length m through a given array,
    the end will be the first element."""
    path = []
    i = 0
    while True:
        path.append(array[i])
        i = (i + step - 1) % len(array)
        if i == 0:
            break
    result = ''.join(map(str, path))

    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    my_list = create_array(size=n)
    print(get_a_path(step=m, array=my_list))

