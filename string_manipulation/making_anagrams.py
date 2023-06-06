#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings


def make_anagrams(a, b):
    my_dict = {}
    my_dict2 = {}
    for char in a:
        my_dict[char] = my_dict.get(char, 0) + 1
    for char in b:
        if char in my_dict.keys():
            if my_dict[char] == 1:
                del my_dict[char]
            else:
                my_dict[char] = my_dict[char] - 1
        else:
            my_dict2[char] = my_dict2.get(char, 0) + 1

    count = 0
    for value in my_dict.values():
        count += value

    for value in my_dict2.values():
        count += value

    return count


make_anagrams('cde', 'abc')

