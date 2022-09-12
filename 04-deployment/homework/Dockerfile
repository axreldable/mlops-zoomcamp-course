FROM agrigorev/zoomcamp-model:mlops-3.9.7-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "starter.py", "starter.py" ]
COPY [ "./data/fhv_tripdata_2021-04.parquet", "./data/fhv_tripdata_2021-04.parquet" ]
RUN mkdir output

ENTRYPOINT [ "python", "starter.py", "--month", "4" ]
