import sys

eng_word = '/hp/english3.txt'
eng_word_line = eng_word.strip()
eng_words = eng_word_line.split()

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in eng_words:
            print('%s\t%s' % (word,1))