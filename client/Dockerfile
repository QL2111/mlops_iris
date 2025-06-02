FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app 
RUN pip install -r requirements.txt

COPY app.py app.py
COPY pokemon_meme.jpeg pokemon_meme.jpeg


CMD ["streamlit", "run", "app.py"]