import pandas as pd

b1 = pd.read_csv('train_dataset.csv', delimiter=';')
b1 = b1.dropna()
b2 = pd.read_csv('database.csv', delimiter=';')
b2 = b2.dropna()

columns_list = ["QUESTION", "ANSWER"]
intersections = pd.DataFrame(columns=columns_list)

for str1 in b1.iterrows():
    question = str1[1]["QUESTION"]
    answer = str1[1]["ANSWER"]
    mask = (b2["Ответ"] == answer)
    try:
        full_name = b2["Полное наименование услуги"][mask][0]
        short_name = b2["Сокращенное наименование услуги"][mask][0]
        tags = b2["Теги по услуге"][mask][0]
    except Exception:
        full_name = ""
        short_name = ""
        tags = ""
    
    loc_df = pd.DataFrame([[" ".join([question, full_name, short_name, tags]), answer]], columns=columns_list)
    intersections = pd.concat([intersections, loc_df], ignore_index=True)

intersections.to_csv("full-question-answer-base.csv", sep=';', index=False)

import yake

language = "ru"
max_ngram_size = 1
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 5

kw_extractor = yake.KeywordExtractor(lan=language, 
                                     n=max_ngram_size, 
                                     dedupLim=deduplication_thresold, 
                                     dedupFunc=deduplication_algo, 
                                     windowsSize=windowSize, 
                                     top=numOfKeywords)

columns_list = ['Keywords', 'Answer']
keywords_answer = pd.DataFrame(columns=columns_list)
for str1 in b2.iterrows():
    loc = pd.DataFrame([[[i[0] for i in kw_extractor.extract_keywords(" ".join([str1[1]["Теги по услуге"], str1[1]["Сокращенное наименование услуги"], str1[1]["Вопрос"]]))], str1[1]["Ответ"]]],columns=columns_list)
    keywords_answer = pd.concat([keywords_answer, loc], ignore_index=True)

keywords_answer.to_csv("keywords_answer.csv", sep=";", index=False)

language = "ru"
max_ngram_size = 1
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 3

kw_extractor = yake.KeywordExtractor(lan=language, 
                                     n=max_ngram_size, 
                                     dedupLim=deduplication_thresold, 
                                     dedupFunc=deduplication_algo, 
                                     windowsSize=windowSize, 
                                     top=numOfKeywords)

columns_list = ['Keywords', 'Answer']
res_key_ans = pd.DataFrame(columns=columns_list)
for str1 in b1.iterrows():
    loc = pd.DataFrame([[[i[0] for i in kw_extractor.extract_keywords(str1[1]["QUESTION"])], str1[1]["ANSWER"]]],columns=columns_list)
    res_key_ans = pd.concat([res_key_ans, loc], ignore_index=True)

res_key_ans.to_csv("res_key_ans.csv", sep=";", index=False)