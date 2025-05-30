FROM python:3.12-slim-bookworm

RUN apt update && apt upgrade -y

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv --version

WORKDIR /owl-backend
COPY . /owl-backend

RUN uv sync --only-group prod

RUN uv run python manage.py makemigrations
RUN uv run python manage.py migrate

ENV BIND=0.0.0.0:8000

CMD ["sh", "-c", "uv run gunicorn  tournament_owl.wsgi:application --bind $BIND"]