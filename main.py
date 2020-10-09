from lxml.html import parse
from lxml import etree as et
from os import listdir
import matplotlib.pyplot as plt

from Person import *

chars_to_monitor = ')(.!?'
month = {'янв' : '01', 'фев' : '02', 'мар' : '03', 'апр' : '04', 'мая' : '05',
         'июн' : '06', 'июл' : '07', 'авг' : '08', 'сен' : '09', 'окт' : '10',
         'ноя' : '11', 'дек' : '12'}

me      = Person('Я   ', chars_to_monitor)
not_me  = Person('Не я', chars_to_monitor)

def is_msg_mine(msg):
    return True if msg[0:2] == 'Вы' else False

def get_date(s):
    i = s.find(',')
    date = s[i + 2 : i + 13].split()
    if len(date[0]) == 1:
        date[0] = '0' + date[0]
    return date[2] + '-' + month[date[1]] + '-' + date[0]
    

def parse_file(filename):
    doc = parse(filename).getroot()

    messages = doc.xpath('/html/body/div/div[2]/div/div')

    for item in messages:
        if item.get('class') != 'item':
            continue
        
        msg = item[0][0]
        header = msg[0].text_content()
        date = get_date(msg[0].text_content())
        #print(msg[0].text_content()) # отправитель, время
        #print(msg[1].text_content()) # содержимое

        if is_msg_mine(header):
            me.update(date, msg[1].text_content())
        else:
            not_me.update(date, msg[1].text_content())


def process_all_files(main_dir):
    for f in listdir(main_dir):
        parse_file(main_dir + '/' + str(f))
        #print('parsed ' + f)


def print_results():
    print()
    me.output()
    print()
    not_me.output()


def graph(my_counter, not_my_counter):
    total = my_counter + not_me.msgs
    labels, values = zip(*sorted(total.items()))
    melabels, mevalues = zip(*sorted(my_counter.items()))
    nmelabels, nmevalues = zip(*sorted(not_my_counter.items())) #.most_common(10)))#
    
    # Create figure and plot space
    fig, ax = plt.subplots(figsize=(10, 10))

    # Add x-axis and y-axis
    ax.plot(labels,
            values,
            color='white')
    
    ax.plot(melabels,
            mevalues,
            color='red')
    
    ax.plot(nmelabels,
            nmevalues,
            color='purple')

    plt.show()

    
main_directory = 'C:\\Users\\me\\Downloads\\Archive\\messages\\anon'

process_all_files(main_directory)

print_results()
graph(me.msgs, not_me.msgs)
#graph(me.total_len, not_me.total_len)
