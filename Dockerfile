FROM python:3.11-alpine AS requirements-stage
WORKDIR /tmp
RUN pip install poetry poetry-plugin-export
COPY ./poetry.lock* ./pyproject.toml /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --only=main

FROM python:3.11-alpine AS base
WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apk del gcc musl-dev libffi-dev python3-dev

COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
