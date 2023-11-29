def caesar_cipher(input_str, num=3):
    alpalist = list('abcdefghijklmnopqrstuvwxyz')
    result = ''

    for i in range(len(input_str)):
        for j in range(len(alpalist)):
            if input_str[i] == alpalist[j]:
                result += alpalist[j-3]

    return result


if __name__ == "__main__":
    input_str = 'seunggihong'
    cipher = caesar_cipher(input_str)
    print(cipher)
