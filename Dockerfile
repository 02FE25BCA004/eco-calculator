FROM python:3.9-slim

WORKDIR /app

COPY carbon_calculator.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "carbon_calculator.py"]