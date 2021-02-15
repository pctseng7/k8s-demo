FROM nvcr.io/nvidia/tritonserver:20.06-py3

RUN apt update && apt-get install -y \
    software-properties-common \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev wget \
    python3.8 \
    python3-pip

WORKDIR /root

COPY dist/pctseng-inference-app-0.0.1.tar.gz serve /root/

RUN pip3 install /root/pctseng-inference-app-*.tar.gz

CMD ["serve"]