class Converter(object):

    def txtdict(self):
        line_n = 0
        words_l = []
        words_s = []  # split words
        words_d = []  # display words

        with open('/Users/cmesser/Development/The_Well/mf.txt', encoding='utf-8') as word_list:
            #  split lines
            for a_line in word_list:
                line_n += 1
                words_l.append(a_line.rstrip())
                #  split words
                for a_word in a_line.split(' ('):
                    words_s.append(a_word.lower())

            #  isolate words
            for w_word in words_s:
                if w_word not in words_d:
                    words_d.append(w_word)
                    word_count = words_s.count(w_word)
                else:
                    continue

if __name__ == '__main__':
    co = Converter()
    co.txtdict()
