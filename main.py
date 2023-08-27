import yake
import spacy
import find_answer


# This is a main script of the project. Normally only this script should be launched by the user.
# This script processes prompt using NLP libraries, especially YAKE! and spaCy extracting five or fewer keywords.
# Then using find_answer.py it shows some variants of answers.


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

user_prompt = input()
nlp_user_prompt = nlp(user_prompt)
normalized_user_prompt = " ".join([token.lemma_ for token in nlp_user_prompt if token.pos_ not in ignore_list])
extracted_keywords_list = [i[0].lower for i in extractor.extract_keywords(normalized_user_prompt)]

answers = find_answer.find_answers(extracted_keywords_list)
if len(answers) == 1:
    print("Упс! К сожалению, мы не смогли найти ответ на Ваш вопрос. " + answers[0])
else:
    print("Вот, что мы нашли по Вашему вопросу: Если результат не нашелся, попробуйте переформулировать вопрос. ")
    print()
    for answer in answers:
        print(answer)
        print()
