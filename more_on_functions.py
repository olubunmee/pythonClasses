# num = 1
#
#
# def func():
#     global num
#     num += 1
#     print(num)
#
#
# def add(a: int = 0, b: str = "white"):
#     return a, b
#
#
# print(add(b='you', a=5))
# print(add(3, '3'))
# print(add('3', 4))
# print(add())
#
# def dict_pack_unpack(*args, **kwargs):
#     print(kwargs)
#     print(args)
#
# dict_pack_unpack(4, 5, 'goal', name = 'Bunmi', age = 27, sex = 'Male')

# def rotate_list(lst, k):
#     k = k % len(lst)
#     output = []
#     list_length = len(lst)
#     for i in range(list_length - k, list_length):
#         output.append(lst[i])
#     for i in range(0, list_length - k):
#         output.append(lst[i])
#     return output
#
#
# print(rotate_list([1, 2, 3, 4, 5, 6, 7, 8], 14))
#
#
# def rotate(lst, k):
#     k = k % len(lst)
#     return lst[-k:] + lst[:-k]
#
#
# print(rotate([23, 55, 12, 86, 29], 13))
#
#
# lst = [num for num in range(1, 11)]
# even = [num for num in range(1, 11) if num % 2 == 0]
# sum_square_and_even = [num if num % 2 == 0 else num ** 2 for num in range(1, 11)]
# lst_input = [int(input("Enter your number: ")) for num in range(1, 5)]
# print(lst)
# print(even)
# print(sum_square_and_even)
# print(lst_input)
#
# list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
# print(list_nested_for)
#
# upper_names = [len(name) for name in ["dolapo", "tolani", "florence"]]
# print(upper_names)

# dict_play = {"name": "Tolani", "age": 32, "influenced": "Samson"}
# print(dict_play)
# print(dict_play.pop("name"))
# print(dict_play.update({"sex": "Male"}))
# print(dict_play)

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays a banjo"
    else:
        return name + " does not play a banjo"


print(are_you_playing_banjo(name="tola"))

# lst = []
# for i in range(65, 99):
#     lst.append(chr(i))

lst = [chr(i) for i in range(65, 91)]
print(lst)
