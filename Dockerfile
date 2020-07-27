FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY src/ ./src
COPY assets/ ./assets

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "src/main.py" ]