FROM python:3-slim

COPY src/ /src/

ENTRYPOINT ["python3", "/src/entrypoint.py"]
