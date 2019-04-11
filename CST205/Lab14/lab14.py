#magic
def standardize(string):
    return ''.join(e for e in string if e.isalnum()).lower()

def uniqueWordCount():
    file = open(pickAFile(), "r")
    words = file.read().split()
    uniqueWords = []
    for word in words:
        word = standardize(word)
        if not word in uniqueWords:
            uniqueWords.append(word)
    print("Unique Words: " + str(len(uniqueWords)))

text = ""
def pullHeadlines():
    file = open(pickAFile(), "r")
    global text
    text = file.read()
    startStr = 'uscb-margin-TB-02 uscb-title-3'
    endStr = "</p>"
    headlines = []
    start = 0
    start = text.find(startStr, start)
    end = text.find(endStr, start)
    print(start)
    while not start == -1:
        headlines.append(text[start+len(startStr):end])
        start = end
        start = text.find(startStr, start)
        end = text.find(endStr, start)
        print(start)
    print("**** U.S. Census Bureau News! ****")
    for line in headlines:
        print(line)
