import os
def summarize(filename):
    vocabulary= {}
    lines = []
    with open(filename, "r") as file:
        for line in file.readlines():
            currline = []
            line = line.rstrip('\n')
            currline.append(line)
            lines.append(currline)

    artist = lines[0]
    title = lines[2]
    del lines[0:4]

    song = []
    verse = []
    for i in range(len(lines)):
        if lines[i] == ['']:
            song.append(verse)
            verse = []
        else:
            verse.append(lines[i][0].split(' '))

    total_num_words= 0
    for verse in song:
        for line in verse:
            for word in line:
                total_num_words += 1
                if word in vocabulary:
                    vocabulary[word] += 1
                else:
                    vocabulary[word] = 1

    weights = {}
    for word in vocabulary:
        weights[word] = float(vocabulary[word])/total_num_words

    summaryIndexes = []
    for v in range(len(song)):
        scores = []
        for l in range(len(song[v])):
            lineSum = 0
            count = 0
            for word in song[v][l]:
                lineSum += weights[word]
                count += 1
            scores.append(lineSum/count)
        maxScore = 0
        maxIndex = 0
        for i in range(len(scores)): 
            if scores[i] > maxScore:
                maxScore = scores[i]
                maxIndex = i
        summaryIndexes.append(maxIndex)

    summary = "{} by {}: ".format(title[0], artist[0])

    for v in range(len(summaryIndexes)):
        index = summaryIndexes[v]
        line = ""
        for word in song[v][index]:
            line += " "
            line += word
        line += "."
        summary += line

    return summary 
        
if __name__ == '__main__':

    directory = "songs"
    for song in os.listdir(directory):
        print(summarize("songs/"+song))
        print
