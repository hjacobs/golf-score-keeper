#!/usr/bin/env python3

import sys


def calculate_playing_handicap(handicap, par, cr, slope):
    "EGA handicap system"
    # http://www.golf.de/dgv/rules4you/handicap/vorgaben_detail.cfm?nr=3-9
    course_handicap = handicap * (slope/113) - cr + par
    return course_handicap


# par stroke-index
course = '''
4 3
4 11
4 15
4 9
3 17
3 7
5 1
4 13
5 5
5 8
3 18
4 10
5 4
4 14
4 12
4 2
4 6
3 16
'''
results = '''
10
6
5
/
7
4
8
6
7
'''

hcp = calculate_playing_handicap(-1 * float(sys.argv[1]), 72, 72.4, 129)
hcp = round(hcp * -1)

holes = {}
for idx, data in enumerate(course.strip().split('\n')):
    hole = idx + 1
    par, stroke_index = data.split()
    holes[hole] = {'par': int(par), 'stroke_index': int(stroke_index), 'handicap_strokes': 0}

remaining = hcp
while remaining > 0:
    for hole in sorted(holes.values(), key=lambda r: r['stroke_index']):
        if remaining <= 0:
            break
        hole['handicap_strokes'] += 1
        remaining -= 1
for hole, data in sorted(holes.items()):
    print(hole, data)

results = results.strip().split()
total_score = 0
for idx, result in enumerate(results):
    hole = idx + 1
    try:
        result = int(result)
    except:
        result = 99
    data = holes[hole]
    score = max(0, 2 + data['par'] + data['handicap_strokes'] - result)
    data['score'] = score
    total_score += score
    print(hole, result, score)

print(total_score)



