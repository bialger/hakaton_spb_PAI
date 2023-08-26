import yake
import spacy


user_prompt = input()

language = "ru"
max_ngram_size = 1
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 5
ignore_list = ["PUNCT", "ADP", "PRON", "CCONJ", "SPACE", "SCONJ"]

extractor = yake.KeywordExtractor(lan=language,
                                     n=max_ngram_size,
                                     dedupLim=deduplication_thresold,
                                     dedupFunc=deduplication_algo,
                                     windowsSize=windowSize,
                                     top=numOfKeywords)

nlp = spacy.load("ru_core_news_sm")
doc = nlp(user_prompt)
raw_keywords = extractor.extract_keywords(" ".join([token.lemma_ for token in doc if token.pos_ not in ignore_list]))
extracted_keywords_list = [i[0] for i in raw_keywords]

print(extracted_keywords_list)