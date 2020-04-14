FROM balenalib/jetson-nano-ubuntu:bionic

ENV TFLITE_RUNTIME_WHL=https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp36-cp36m-linux_aarch64.whl

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        python3-pip \
        python3-setuptools \
        python3-dev && \
    python3 -m pip install -U pip Cython wheel && \
    python3 -m pip install -U numpy==1.16.1 && \
    python3 -m pip install $TFLITE_RUNTIME_WHL

COPY . .

CMD ["python3", "benchmark.py"]
