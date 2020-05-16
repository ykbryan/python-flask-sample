FROM python:3.7
RUN mkdir /code
RUN mkdir /config
COPY ./ /code/
WORKDIR /code
COPY ./requirements.txt /config/
RUN pip install -r /config/requirements.txt
