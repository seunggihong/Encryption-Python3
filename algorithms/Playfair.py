key = list(dict.fromkeys('assassinator'))
alpalist = 'abcdefghijklmnopqrstuvwxyz'
input_str = 'seunggihong'

table = list(dict.fromkeys(list(key + list(alpalist))))
table.remove('z')
table[table.index('q')] = 'qz'

table_metrix = [["" for _ in range(5)] for x in range(5)]

for i in range(5):
    for j in range(5):
        table_metrix[i][j] += table[i*5+j]

pair = []
cnt = 0
while (cnt < len(input_str)-1):
    if input_str[cnt] == input_str[cnt+1]:
        pair.append([input_str[cnt], 'x'])
        cnt += 2
    else:
        pair.append([input_str[cnt], input_str[cnt+1]])
        cnt += 2

if len(input_str) % 2 != 0:
    pair.append([input_str[cnt], 'x'])

sub_result = [["", ""] for _ in range(len(pair))]

for i in range(len(pair)):
    for j in range(5):
        if pair[i][0] in table_metrix[j]:
            sub_result[i][0] = [j, table_metrix[j].index(pair[i][0])]
        if pair[i][1] in table_metrix[j]:
            sub_result[i][1] = [j, table_metrix[j].index(pair[i][1])]

print(sub_result[0][0][1])
