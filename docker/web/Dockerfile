FROM python:3.12-slim

ARG USER_ID=1000
ARG GROUP_ID=1000

# No .pyc files in the bind mount; logs reach `docker compose logs` immediately.
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PIP_NO_CACHE_DIR=1 \
	PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN groupadd -g ${GROUP_ID} appuser \
	&& useradd -u ${USER_ID} -g appuser -m -s /bin/sh appuser

USER appuser

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
