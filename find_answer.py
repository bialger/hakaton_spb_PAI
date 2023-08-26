import pandas as pd


def func1(a):
    keywords_answer = pd.read_csv('keywords_answer.csv', delimiter=';')
    maxi = 0
    max_counter = 0
    counter = 0
    for x in keywords_answer["Keywords"]:
        len1 = 0
        for t in x:
            if t in a:
                len1 += 1
        if len1 > maxi:
            maxi = len1
            max_counter = counter
        counter += 1
    return keywords_answer["Answer"][max_counter]

