# Dependency Pre-stage
FROM python:3.10-slim-bullseye AS requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev ; else poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev ; fi"
# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Main App Setup
FROM python:3.10-slim-bullseye

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./tests /code/tests

# COPY ./alembic.ini /code/

COPY ./scripts/prestart.sh /code/

COPY ./scripts/start.sh /code/

EXPOSE 8000

ENV PYTHONPATH=/code

CMD ["./start.sh"]
