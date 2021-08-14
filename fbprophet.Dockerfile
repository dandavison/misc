FROM ubuntu:20.04

ENV PYTHON_VERSION=3.6.9

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    curl \
    git\
    libbz2-dev \
    libncurses5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    llvm \
    make \
    zlib1g-dev

ENV PATH="/root/.pyenv/bin:$PATH"

RUN curl https://pyenv.run | bash && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    eval "$(pyenv init -)" && \
    pyenv update && \
    pyenv install $PYTHON_VERSION && \
    pyenv global $PYTHON_VERSION

RUN /root/.pyenv/shims/python3.6 -m venv /tmp/venv

RUN /tmp/venv/bin/pip install --upgrade pip

RUN /tmp/venv/bin/pip install fbprophet
