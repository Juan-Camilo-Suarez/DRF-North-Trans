FROM python:3.10.9

RUN pip install poetry==1.3.2 && poetry config virtualenvs.create false

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

COPY . .


EXPOSE 8000

CMD python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000