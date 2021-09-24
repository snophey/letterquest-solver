FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "--host", "0.0.0.0", "main:app" ]
