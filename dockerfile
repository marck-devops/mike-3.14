
FROM 339712843199.dkr.ecr.us-east-1.amazonaws.com/marck-python-slim:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

