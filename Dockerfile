FROM python:3.8
RUN mkdir /code
RUN mkdir /config
COPY ./ /code/
WORKDIR /code
COPY ./requirements.txt /config/
EXPOSE 8080
RUN pip install --upgrade pip
RUN pip install -r /config/requirements.txt
