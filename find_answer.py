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
        c = 0
        while len(answers) < 2:
            if biggest_len_of_keys[c][1] not in answers:
                answers.append(biggest_len_of_keys[c][1])
            c += 1
    elif 5 > len(a) > 1:
        c = 0
        while len(answers) < 7-len(a):
            if biggest_len_of_keys[c][1] not in answers:
                answers.append(biggest_len_of_keys[c][1])
            c += 1
    else:
        answers = ['Пожалуйста, уточните Ваш запрос.']
    return answers
