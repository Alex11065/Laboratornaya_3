# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first, participants_second, separator=','):
    group1 = participants_first.split(separator)
    group2 = participants_second.split(separator)
    common_participants = list(set(group1).intersection(group2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
list_ = find_common_participants(participants_first_group, participants_second_group)
print('Список общих участников:', list_)

# TODO Провеьте работу функции с разделителем отличным от запятой
