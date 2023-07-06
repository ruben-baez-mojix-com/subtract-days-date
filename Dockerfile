FROM python:3.7

COPY src/ /src/

RUN chmod +x /src/entrypoint.py

ENTRYPOINT ["/src/entrypoint.py"]