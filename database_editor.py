import pandas as pd
import yake
import spacy


# This file configures databases and processes significant amount of information using NLP and keyword extractor library
# This script merges two given datasets into one, then handle them, extracting keywords from questions and other data.
# Normally it should be edited and launched only if you want to reconfigure dataset, e.g. increase amount of keywords.

first_database = pd.read_csv('train_dataset.csv', delimiter=';')
first_database = first_database.dropna()
second_database = pd.read_csv('database.csv', delimiter=';')
second_database = second_database.dropna()

columns_list = ["QUESTION", "ANSWER"]
intersections = pd.DataFrame(columns=columns_list)

for line in first_database.iterrows():
    question = line[1]["QUESTION"]
    answer = line[1]["ANSWER"]
    mask = (second_database["Ответ"] == answer)
    try:
        full_name = second_database["Полное наименование услуги"][mask][0]
        short_name = second_database["Сокращенное наименование услуги"][mask][0]
        tag = second_database["Теги по услуге"][mask][0]
    except KeyError:
        full_name = ""
        short_name = ""
        tag = ""
    new_question = " ".join([question, full_name, short_name, tag])
    summarized_dataframe = pd.DataFrame([[new_question, answer]], columns=columns_list)
    intersections = pd.concat([intersections, summarized_dataframe], ignore_index=True)

intersections.to_csv("full-question-answer-base.csv", sep=';', index=False)


language = "ru"
max_ngram_size = 1
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 5
ignore_list = ["PUNCT", "ADP", "PRON", "CCONJ", "SPACE", "SCONJ"]
nlp = spacy.load("ru_core_news_sm")

extractor = yake.KeywordExtractor(lan=language,
                                  n=max_ngram_size,
                                  dedupLim=deduplication_thresold,
                                  dedupFunc=deduplication_algo,
                                  windowsSize=windowSize,
                                  top=numOfKeywords)


columns_list = ['Keywords', 'Answer']
first_dataframe = pd.DataFrame(columns=columns_list)

for line in second_database.iterrows():
    question = " ".join([line[1]["Теги по услуге"], line[1]["Сокращенное наименование услуги"], line[1]["Вопрос"]])
    nlp_question = nlp(question)
    normalized_question = " ".join([token.lemma_ for token in nlp_question if token.pos_ not in ignore_list])
    keywords_question = " ".join([i[0].lower() for i in extractor.extract_keywords(normalized_question)])
    line_dataframe = pd.DataFrame([[keywords_question, line[1]["Ответ"]]], columns=columns_list, dtype="object")
    first_dataframe = pd.concat([first_dataframe, line_dataframe], ignore_index=True)

first_dataframe.to_csv("keywords_answer.csv", sep=";", index=False)

numOfKeywords_question = 3
numOfKeywords_answer = 2

extractor_question = yake.KeywordExtractor(lan=language,
                                  n=max_ngram_size,
                                  dedupLim=deduplication_thresold,
                                  dedupFunc=deduplication_algo,
                                  windowsSize=windowSize,
                                  top=numOfKeywords_question)

extractor_answer = yake.KeywordExtractor(lan=language,
                                  n=max_ngram_size,
                                  dedupLim=deduplication_thresold,
                                  dedupFunc=deduplication_algo,
                                  windowsSize=windowSize,
                                  top=numOfKeywords_answer)

columns_list = ['Keywords', 'Answer']
second_dataframe = pd.DataFrame(columns=columns_list)

for line in first_database.iterrows():
    question = line[1]["QUESTION"]
    answer = line[1]["ANSWER"]
    nlp_question = nlp(question)
    nlp_answer = nlp(answer)
    normalized_question = " ".join([token.lemma_ for token in nlp_question if token.pos_ not in ignore_list])
    normalized_answer = " ".join([token.lemma_ for token in nlp_answer if token.pos_ not in ignore_list])
    keywords_question_list = [i[0].lower() for i in extractor_question.extract_keywords(normalized_question)]
    keywords_answer_list = [i[0].lower() for i in extractor_answer.extract_keywords(normalized_answer)]
    keywords = " ".join(set(keywords_question_list + keywords_answer_list))
    line_dataframe = pd.DataFrame([[keywords, line[1]["ANSWER"]]], columns=columns_list, dtype="object")
    second_dataframe = pd.concat([second_dataframe, line_dataframe], ignore_index=True)

second_dataframe.to_csv("res_key_ans.csv", sep=";", index=False)

full_keywords_answer_dataframe = pd.concat([first_dataframe, second_dataframe], ignore_index=True)
full_keywords_answer_dataframe.to_csv("full_dataset.csv", sep=";", index=False)
