FROM python:3.10

RUN mkdir /application
WORKDIR "/application"

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

ADD requirements.txt /application/
ADD src/main.py /application/
ADD src/database_editor.py /application/
ADD src/find_answer.py /application/
ADD src/database.csv /application/
ADD src/full-question-answer-base.csv /application/
ADD src/full_dataset.csv /application/
ADD src/keywords_answer.csv /application/
ADD src/res_key_ans.csv /application/
ADD src/train_dataset.csv /application/

RUN pip install -r /application/requirements.txt
RUN python -m spacy download ru_core_news_sm

CMD [ "python", "main.py" ]