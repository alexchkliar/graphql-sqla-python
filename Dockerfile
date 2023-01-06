FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /src /code/src

CMD ["python", "./src/app.py", "--host", "0.0.0.0", "--port", "5000"]
