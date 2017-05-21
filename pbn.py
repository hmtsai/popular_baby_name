# http://www.regular-expressions.info/examples.html
# <TAG\b[^>]*>(.*?)</TAG> matches the opening and closing pair of a specific HTML tag. 
# Anything between the tags is captured into the first backreference. 
# The question mark in the regex makes the star lazy, to make sure it stops before the first closing tag rather than before the last, 
# like a greedy star would do. This regex will not properly match tags nested inside themselves, like in <TAG>one<TAG>two</TAG>one</TAG>.

import re

table_tag = '<table\s*[^>]*>((\s|.)*)</table>'
pat = '<td>(\d+)</td> <td>(\w+)</td> <td>(\w+)</td>'

def extract_name_rank(fn, extfn):
    f = open(fn, mode='r')
    text = f.read()
    lst = re.findall(pat, text)
    #print(lst)
    f.close()

    f = open(fn+extfn, 'w')
    for item in lst:
        f.write(item[0] + item[1].rjust(25) + item[2].rjust(25) + '\n')
    f.close()

def years_rank_give_name(name, years_dic):
    for d in years_dic:
        if name in d.keys():
            print (name + ' rank: ' + d[name])
        else:
            print (name + ' not found in rank')


def names_trend(fn, name):

    lines_files = []

    for item in fn:

        f = open(item, 'r')
        lines = f.readlines()
        #print(lines) # list of line string
        lines_files.append(lines)
        f.close()
    #print(lines_files) 

    all_mr_d = []
    all_fr_d = []

    for lines in lines_files:
        mr_d = {}
        fr_d = {}
        for line in lines:
            row = line.split()
            mr_d[row[1]] = row[0]
            fr_d[row[2]] = row[0]
        #print(fr_d)
        all_mr_d.append(mr_d)
        all_fr_d.append(fr_d)
    #print(all_mr_d)

    print('checking male name...')
    years_rank_give_name(name, all_mr_d)
    print('checking female name...')
    years_rank_give_name(name, all_fr_d)

 
def main():
    src_fn = ['2012.html', '2013.html', '2014.html', '2015.html', '2016.html']
    rank_ext_fn = '.rank.txt'

    for fn in src_fn:
        extract_name_rank(fn, rank_ext_fn)
    
    rank_fn = []
    for item in src_fn:
        rank_fn.append( item + rank_ext_fn )
    #print(rank_fn)

    names_trend(rank_fn, 'Sophia')


if __name__ == '__main__':
    main()
