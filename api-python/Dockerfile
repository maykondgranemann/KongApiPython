FROM python:3.11.2

WORKDIR /python-kong

COPY ./requirements.txt  /python-kong/requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV SERVICE_NAME "SERVICE 1"

CMD ["python", "main.py"]