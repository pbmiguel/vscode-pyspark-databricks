FROM databricksruntime/python:13.3-LTS AS base

ENV PATH $PATH:/databricks/python3/bin

RUN python -m pip install poetry==1.4.2
RUN poetry config virtualenvs.create false
RUN poetry config cache-dir /tmp/poetry-cache

RUN mkdir -p /app/
WORKDIR /app


COPY pyproject.toml poetry.lock /app/
COPY entrypoint.py /app

RUN poetry install

FROM databricksruntime/python:13.3-LTS AS dev

ENV PATH $PATH:/databricks/python3/bin

COPY --from=base /app/ /app/
COPY --from=base /databricks/python3 /databricks/python3