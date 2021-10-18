def proccess_ebook(filename):

    file = open(filename, 'r', encoding='utf-8')

    content = file.read()

    lines = content.split("\n")

    words_map = {}

    for line in lines:
        if len(line) > 0:
            words = []
            for word in line.split(' '):
                if word.isnumeric() or word.islower():
                    words.append(word)

            for word in words:
                if word in words_map.keys():
                    words_map[word] +=1
                else:
                    words_map[word]= 1

    value = ''
    count = 0

    for word in words_map.keys():
        if words_map[word] > count:
            count = words_map[word]
            value = word

    result = {k: v for k, v in sorted(words_map.items(), key=lambda item: item[1])}

    return list(result.items())
if __name__ == '__main__':
    print(proccess_ebook('pg66474.txt'))