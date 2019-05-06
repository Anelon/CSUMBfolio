#magic
def standardize(string):
    return ''.join(e for e in string if e.isalnum()).lower()

def uniqueWordCount():
    path = pickAFile()
    file = open(path, "r")
    if '.' in path:
        path = path[:path.rfind('.')] + '.'
        path = path[:-1]
    writeFile = open(path + ".html", "w+")
    words = file.read().split()
    uniqueWords = {}
    for word in words:
        word = standardize(word)
        if not word in uniqueWords:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] += 1
    print("Unique Words: " + str(len(uniqueWords)))
    for key,val in uniqueWords.items():
        if val == 1:
            size = 5
        elif val < 4:
            size = 10
        elif val < 7:
            size = 20
        elif val < 10:
            size = 25
        elif val < 20:
            size = 30
        elif val < 30:
            size = 40
        elif val < 40:
            size = 60
        else:
            size = 50
        writeFile.write('<p style="color:#339900; font-size:' + str(size) + 'px; font-weight:bold">' + key + '</p>')
    writeFile.close()

