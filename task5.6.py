"""���������� ������� (�� ����������) ��������� ����, ��� ������ ������ ��������� ������� ������� � ������� ����������,
������������ � ������������ ������� �� ����� �������� � �� ����������. �����, ����� ��� ������� �������� �� �����������
���� ��� ���� �������. ������������ �������, ���������� �������� �������� � ����� ���������� ������� �� ����.
������� ������� �� �����.
"""

journal = {}
with open('journal.txt') as text:
    lines = text.readlines()
    for line in lines:
        string = line.split()
        subject = string[0]
        sum_lessons = sum([int(x[:x.find('(')]) for x in string[1:] if '(' in x])    # ����� �������� ������ ��������� ���������, ���� �� ������ ��� ������, ��� ��� if ��� ������������.
        journal[subject[:-1]] = sum_lessons
print(journal)
