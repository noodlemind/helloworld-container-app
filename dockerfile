FROM python:2.7-slim
WORKDIR /app
ADD . /app

# Install any necessary dependencies
RUN pip install -r dependencies.txt

# Open Port 80 for serving the Application Page
EXPOSE 80

# Run app.py whn ee container is launched / spin
CMD ["python", "app.py"]