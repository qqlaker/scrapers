import pandas as pd

list = []
list1 = []
end1 = []
name_and_ip = [[], []]
end = [[],[],[],[]]
end2 = []
lines = 0
h = 0

f = open('file.log')
for line in f:

    if line != '\n':
        list.append(line.split(' '))
        lines += 1

for _ in range(len(list)):

    for i in range(len(list[_])):
        list[_][i] = list[_][i].strip('\n')

f.close()

lines = 0
for i in range(len(list)):

    if list[i][0] == 'name=' or list[i][0] == 'ip=':
        list1.append(list[i])
        lines += 1

del list
list = list1
del list1

while 'name=' in list[h]:

    try:
        if 'ip=' in list[h+2]:
            while 'ip=' in list[h+2]:
                list[h+1][1] += ' ' + list[h+2][1]
                list[h + 1][2] += ' ' + list[h + 2][2]
                del list[h+2]
                lines -= 1

    except IndexError:

        break

    h += 2

for _ in range(lines):

    if list[_][0] == 'name=':
        name_and_ip[0].append(list[_])
    if list[_][0] == 'ip=':
        name_and_ip[1].append(list[_])


for i in range(len(name_and_ip[0])):
    name_and_ip[0][i].pop(0)
    name_and_ip[1][i].pop(0)

for _ in range(len(name_and_ip[0])):

    st = ''
    if '#' in name_and_ip[0][_][-1]:
        last = name_and_ip[0][_].pop(-1)
    else:
        last = ''
    end[1].append(last)

    for l in range(len(name_and_ip[0][_])):
        if l != (len(name_and_ip[0][_])-1):
            st += name_and_ip[0][_][l] + ' '
        else:
            st += name_and_ip[0][_][l]
    end[0].append(st)

    for l in range(len(name_and_ip[1][_])):
        if l == 0:
            end[2].append(name_and_ip[1][_][l])
        elif l == 1:
            end[3].append(name_and_ip[1][_][l])

for _ in range(len(end[2])):

    end[1][_] = end[1][_].replace(',', '')
    end[2][_] = end[2][_].replace(',', '')
    end[3][_] = end[3][_].replace(',', '')

for i in range(len(end[0])):
    end1.append([end[0][i], end[1][i], end[2][i], end[3][i]])

for i in range(len(end1)):

    curr_name = end1[i][0]
    curr_id = end1[i][1]

    if (len(end1[i][2].split())) > 1:
        string1 = end1[i][2].split(' ')
        string2 = end1[i][3].split(' ')
        for k in range(len(string1)):
            mas = [curr_name, curr_id, string1[k], string2[k]]
            end2.append(mas)
    else:
        mas = [curr_name, curr_id, end1[i][2], end1[i][3]]
        end2.append(mas)

try:
    df = pd.DataFrame(end2)
    df.to_excel(r'file.xlsx', index=False, startcol=0)
except PermissionError:
    print('Закройте file.xlsx')
    inp = input('Нажмите Enter...')
