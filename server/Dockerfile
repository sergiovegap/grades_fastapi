FROM python:3.13-alpine

COPY . /server

WORKDIR /server

RUN python3 -m venv venv

RUN source venv/bin/activate

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# CMD ["fastapi", "dev", "main.py", "--port", "8000"]
