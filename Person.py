from CharStat import CharStat
from collections import Counter

class Person:
    def __init__(self, name, chars_to_monitor):
        self.name = name
        self.n_msg = 0
        self.msgs = Counter()
        self.total_len = Counter()
        self.counters = []
        for c in chars_to_monitor:
            self.counters.append(CharStat(c))

    def update(self, date, msg):
        self.n_msg += 1
        self.msgs[date] += 1
        self.total_len[date] += len(msg) # а вложения???
        for i in self.counters:
            i.update(date, msg)

    def output(self):
        print(self.name + '\n' +
              'Число сообщений\t:' + str(self.n_msg) + '\n' +
              'Число символов\t: ' + str(sum(self.total_len.values())))
        for i in self.counters:
            print(i.name + ' ' + str(sum(i.cnt.values())))


