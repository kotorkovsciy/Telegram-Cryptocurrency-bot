import re


def split_by_pattern(string, pattern):
    return list(filter(None, re.sub(pattern, r'@@\1', string).split('@@')))


if __name__ == '__main__':
    data = '''28.03.22, ПН
08:30 - 10:00 Предмет_1
10:10 - 11:40 Предмет_2
29.03.22, ВТ
08:30 - 10:00 Предмет_1
10:10 - 11:40 Предмет_2'''
    my_pattern = r'(([\d]{2}\.){2}[\d]{2})'
    print(split_by_pattern(data, my_pattern))