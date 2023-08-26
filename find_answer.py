import pandas as pd


def func1(a):
    keywords_answer = pd.read_csv('full_dataset.csv', delimiter=';')
    counter = 0
    biggest_len_of_keys = []
    for x in keywords_answer["Keywords"]:
        try:
            x1 = x.split()
        except Exception:
            pass
        len1 = 0
        for t in x1:
            if t in a:
                len1 += 1
        biggest_len_of_keys.append([len1, keywords_answer['Answer'][counter]])
        counter += 1
    biggest_len_of_keys.sort(reverse = True)
    answers = []
    if len(a) >= 5:
        answers = [answ[1] for answ in biggest_len_of_keys[0:2]]
    elif 5 > len(a) > 1:
        answers = [answ[1] for answ in biggest_len_of_keys[0:7-len(a)]]
    else:
        answers = ['Пожалуйста, уточните ваш запрос.']
    return answers
