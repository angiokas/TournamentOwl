FROM python:3.12-slim-bookworm AS base

RUN apt update && apt upgrade -y

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv --version

FROM base AS final
ENV BIND=0.0.0.0:8000
CMD ["sh", "-c", "uv run gunicorn  tournament_owl.wsgi:application --bind $BIND"]

WORKDIR /owl-backend
COPY . /owl-backend

RUN \
--mount=type=cache,dst=/cache \
<<EOT
uv sync --only-group --cache-dir=/cache/ prod
uv run python manage.py makemigrations
uv run python manage.py migrate
EOT
