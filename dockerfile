
FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    ansible-core \
    openssh-client \
    sshpass \
    iputils-ping \
    dnsutils \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala Pytest e Testinfra
RUN pip install --no-cache-dir pytest testinfra

# Define diretório de trabalho
WORKDIR /app

CMD ["/bin/bash"]
