def vigenere_cipher(input_str, key):
    alpalist = list('abcdefghijklmnopqrstuvwxyz')
    metrix = []

    for i in range(26):
        metrix.append([alpalist[_] for _ in range(i, 26)] + alpalist[:i])

    input_str = input_str.replace(" ", "")
    key = key.replace(" ", "")

    key = (key * (len(input_str)//len(key))) + \
        (key[:len(input_str) % len(key)])

    result = ''

    for i in range(len(input_str)):
        x, y = alpalist.index(input_str[i]), alpalist.index(key[i])
        result += metrix[x][y]

    return result
