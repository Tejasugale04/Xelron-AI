FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    curl=7.81.0-1ubuntu1.14 \
    python3=3.10.6-1~22.04 \
    python3-pip=22.0.2+dfsg-1 \
    netcat-openbsd=1.218-4ubuntu1 \
    && rm -rf /var/lib/apt/lists/*

# Install k3d
RUN curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/v1.27.3/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

WORKDIR /workspace
COPY . .
