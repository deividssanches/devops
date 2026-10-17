FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install flask boto3
COPY lambda_function.py app.py ./
# NÃO copie .aws-sam
EXPOSE 8080
CMD ["python", "app.py"]