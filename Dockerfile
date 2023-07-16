FROM python:3.11

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PYTHONBUFFERED=1

WORKDIR /backend

RUN apt-get update \
&& apt-get clean autoclean \
&& apt-get autoremove --yes \
&& rm -rf /var/lib/{apt,dpkg,cache,log}/


COPY pyproject.toml pyproject.toml .env alembic.ini ./
RUN pip install poetry --no-cache-dir && \
    poetry install --no-dev --no-cache --no-root --no-interaction  # remove --no-dev if you want to install dev dependencies

COPY /app ./app

CMD poetry run alembic upgrade head && poetry run python -m uvicorn app.api.server:app --host=0.0.0.0 --reload