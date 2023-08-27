FROM python:3.10

RUN mkdir /application
WORKDIR "/application"

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

ADD requirements.txt /application/
ADD main.py /application/
ADD database_editor.py /application/
ADD find_answer.py /application/
ADD database.csv /application/
ADD full-question-answer-base.csv /application/
ADD full_dataset.csv /application/
ADD keywords_answer.csv /application/
ADD res_key_ans.csv /application/
ADD train_dataset.csv /application/

RUN pip install -r /application/requirements.txt
RUN python -m spacy download ru_core_news_sm

CMD [ "python", "main.py" ]