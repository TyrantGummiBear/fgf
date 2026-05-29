FROM python:3.12-slim

RUN pip install --no-cache-dir deep-translator==1.11.4

WORKDIR /docs

# Source + output live on the mounted volume (/docs = fgf/)
ENTRYPOINT ["python", "/docs/scripts/translate_docs.py"]
CMD ["--help"]
