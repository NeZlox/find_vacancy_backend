FROM python:3.12-slim

WORKDIR /vacancy

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


# Make entrypoint.sh executable
RUN chmod +x entrypoint.sh

# Use the entrypoint.sh script as the entrypoint for the container
#ENTRYPOINT ["./entrypoint.sh"]



