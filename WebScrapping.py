from urllib.request import urlopen

def func():
    with urlopen('http://textfiles.com/programming/freeware.txt') as story :
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    print(' '.join(story_words))


func()

  
