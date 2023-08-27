import pandas as pd

# This script consists of one function that is used in main.py.
# It receives keywords from user prompt, compares it with all keyword sets and returns matching answers.


def find_answers(user_keywords):
    dataset_keywords_answer = pd.read_csv('full_dataset.csv', delimiter=';')
    counter = 0
    all_matches_keywords = []
    for raw_keywords in dataset_keywords_answer["Keywords"]:
        list_keywords = []
        try:
            list_keywords = raw_keywords.split()
        except AttributeError:
            pass
        match_count = 0
        for current_keyword in list_keywords:
            if current_keyword in user_keywords:
                match_count += 1
        all_matches_keywords.append([match_count, dataset_keywords_answer['Answer'][counter]])
        counter += 1
    all_matches_keywords.sort(reverse=True)
    answers = []
    if len(user_keywords) > 1:
        target_answers_len = 3
        if len(user_keywords) < 5:
            target_answers_len += 5 - len(user_keywords)
        c = 0
        while len(answers) < target_answers_len:
            if all_matches_keywords[c][1] not in answers:
                answers.append(all_matches_keywords[c][1])
            c += 1
    else:
        answers = ['Пожалуйста, уточните Ваш запрос.']
    return answers
