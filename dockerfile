FROM python:3.10

ENV PYTHONUNBUFFERED True

COPY src /app/src
WORKDIR /app/src

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/* \ 
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove gcc build-essential

EXPOSE 8080

#CMD ["uvicorn", "App:app", "--host", "0.0.0.0", "--port", "8080"]
CMD ["python", "PullApp.py"]