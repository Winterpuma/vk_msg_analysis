from collections import Counter

class CharStat:
    def __init__(self, name):
        self.name = name
        self.cnt = Counter()

    def update(self, date, msg):
        self.cnt[date] += msg.count(self.name)
