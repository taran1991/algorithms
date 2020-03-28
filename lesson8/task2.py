
# -*- coding: utf-8 -*-


"""
Закодируйте любую строку по алгоритму Хаффмана
"""


from collections import Counter


class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leave(self):
        if self.right is None and self.left is None:
            return True
        else:
            return False

    def get_leaves_pathes(self, leaves_pathes={}, path=''):
        if self.is_leave():
            leaves_pathes[self.value] = path
            return leaves_pathes
        else:
            left_path = path + '0'
            right_path = path + '1'
            leaves_pathes = self.left.get_leaves_pathes(leaves_pathes, left_path)
            leaves_pathes = self.right.get_leaves_pathes(leaves_pathes, right_path)
        return leaves_pathes


def hafman_encode(user_str):
    if len(user_str) == 0:
        return ''
    symbols = Counter(user_str).most_common()
    if len(symbols) == 1:
        code_table = {symbols[0][0]: '0'}
    else:
        while len(symbols) != 1:
            left = symbols[-1][0] if isinstance(symbols[-1][0], Node) else Node(value=symbols[-1][0], left=None, right=None)
            right = symbols[-2][0] if isinstance(symbols[-2][0], Node) else Node(value=symbols[-2][0], left=None, right=None)
            new_node = Node(value=None, left=left, right=right)
            symbols = sorted(symbols[:-2] + [(new_node, symbols[-1][1] + symbols[-2][1])], key=lambda x: x[1], reverse=True)
        code_table = symbols[0][0].get_leaves_pathes()
    byte_str = ''
    for el in user_str:
        byte_str += code_table[el]
    return byte_str


user_str = 'beep boop beer!'
print(hafman_encode(user_str))