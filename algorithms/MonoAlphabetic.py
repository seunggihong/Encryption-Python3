def mono_alphabetic_cipher(input_str, keyword):
    alpalist = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    keyword = list(dict.fromkeys(keyword))

    for i in range(len(alpalist)):
        if alpalist[i] == keyword[-1]:
            index = i

    result = keyword
    for i in alpalist[index:]:
        if i in keyword:
            pass
        else:
            result.append(i)

    for i in alpalist:
        if i not in result:
            result.append(i)

    result_crip = ''
    for i in input_str:
        for j in range(26):
            if alpalist[j] == i:
                result_crip += result[j]

    return result_crip
