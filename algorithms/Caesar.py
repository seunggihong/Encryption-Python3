def caesar_cipher(input_str, num=3):
    alpalist = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for i in range(len(input_str)):
        for j in range(len(alpalist)):
            if input_str[i] == alpalist[j]:
                result += alpalist[j-num]

    return result
