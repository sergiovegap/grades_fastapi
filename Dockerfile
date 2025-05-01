FROM python:alpine

WORKDIR /calificaciones_fastapi

RUN python3 -m venv venv

COPY /requirements.txt /calificaciones_fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade ./venv/bin/pip -r /calificaciones_fastapi/requirements.txt

COPY /calificaciones_fastapi /calificaciones_fastapi/server

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
