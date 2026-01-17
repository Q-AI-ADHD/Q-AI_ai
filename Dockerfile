FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CMAKE_ARGS="" \
    FORCE_CMAKE=0

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev \
    build-essential cmake ninja-build git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --prefer-binary \
    llama-cpp-python \
    --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124

COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
