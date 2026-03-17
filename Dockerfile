FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 7860

<<<<<<< HEAD
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT:-7860} app:app"]
=======
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
>>>>>>> d6832e31e439072de081850002c54f6902723475

