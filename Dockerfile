FROM python:3.7

COPY src/ /src/

ENTRYPOINT ["/src/entrypoint.py"]