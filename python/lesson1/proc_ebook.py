def proccess_ebook(filename):

    file = open(filename, encoding='utf-8')

    content = file.read()

    lines = content.split("\n")

    words_map = {}

    for line in lines:
        if len(line) > 0:
            words = []

            for word in line.split(' '):
                if len(word) > 0:
                    words.append(word)

            for word in words:
                if word.lower() in words_map.keys():
                    words_map[word.lower()] +=1
                else:
                    words_map[word.lower()]= 1

    value = ''
    count = 0

    for word in words_map.keys():
        if words_map[word] > count:
            count = words_map[word]
            value = word

    result = {k: v for k, v in sorted(words_map.items(), key=lambda item: item[1])}

    return list(result.items())[-1]
if __name__ == '__main__':
    print(proccess_ebook('pg36099.txt'))