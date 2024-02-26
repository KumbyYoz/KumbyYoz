{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMil4UJqLXvqH1SWjiQbv4M",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KumbyYoz/KumbyYoz/blob/main/Chatbot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QE4eBEqZaD_m",
        "outputId": "d990f9d3-1e80-4a2f-9d10-eb8075f11ae0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: google-cloud-aiplatform in /usr/local/lib/python3.10/dist-packages (1.39.0)\n",
            "Requirement already satisfied: google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0 in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (2.11.1)\n",
            "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.0 in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (1.23.0)\n",
            "Requirement already satisfied: protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5 in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (3.20.3)\n",
            "Requirement already satisfied: packaging>=14.3 in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (23.2)\n",
            "Requirement already satisfied: google-cloud-storage<3.0.0dev,>=1.32.0 in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (2.8.0)\n",
            "Requirement already satisfied: google-cloud-bigquery<4.0.0dev,>=1.15.0 in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (3.12.0)\n",
            "Requirement already satisfied: google-cloud-resource-manager<3.0.0dev,>=1.3.3 in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (1.12.1)\n",
            "Requirement already satisfied: shapely<3.0.0dev in /usr/local/lib/python3.10/dist-packages (from google-cloud-aiplatform) (2.0.0)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in /usr/local/lib/python3.10/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (1.62.0)\n",
            "Requirement already satisfied: google-auth<3.0.dev0,>=2.14.1 in /usr/local/lib/python3.10/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (2.27.0)\n",
            "Requirement already satisfied: requests<3.0.0.dev0,>=2.18.0 in /usr/local/lib/python3.10/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (2.31.0)\n",
            "Requirement already satisfied: grpcio<2.0dev,>=1.33.2 in /usr/local/lib/python3.10/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (1.60.1)\n",
            "Requirement already satisfied: grpcio-status<2.0.dev0,>=1.33.2 in /usr/local/lib/python3.10/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (1.48.2)\n",
            "Requirement already satisfied: google-cloud-core<3.0.0dev,>=1.6.0 in /usr/local/lib/python3.10/dist-packages (from google-cloud-bigquery<4.0.0dev,>=1.15.0->google-cloud-aiplatform) (2.3.3)\n",
            "Requirement already satisfied: google-resumable-media<3.0dev,>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from google-cloud-bigquery<4.0.0dev,>=1.15.0->google-cloud-aiplatform) (2.7.0)\n",
            "Requirement already satisfied: python-dateutil<3.0dev,>=2.7.2 in /usr/local/lib/python3.10/dist-packages (from google-cloud-bigquery<4.0.0dev,>=1.15.0->google-cloud-aiplatform) (2.8.2)\n",
            "Requirement already satisfied: grpc-google-iam-v1<1.0.0dev,>=0.12.4 in /usr/local/lib/python3.10/dist-packages (from google-cloud-resource-manager<3.0.0dev,>=1.3.3->google-cloud-aiplatform) (0.13.0)\n",
            "Requirement already satisfied: numpy>=1.14 in /usr/local/lib/python3.10/dist-packages (from shapely<3.0.0dev->google-cloud-aiplatform) (1.25.2)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth<3.0.dev0,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (5.3.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth<3.0.dev0,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (0.3.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth<3.0.dev0,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (4.9)\n",
            "Requirement already satisfied: google-crc32c<2.0dev,>=1.0 in /usr/local/lib/python3.10/dist-packages (from google-resumable-media<3.0dev,>=0.6.0->google-cloud-bigquery<4.0.0dev,>=1.15.0->google-cloud-aiplatform) (1.5.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil<3.0dev,>=2.7.2->google-cloud-bigquery<4.0.0dev,>=1.15.0->google-cloud-aiplatform) (1.16.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (2024.2.2)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.dev0,>=2.14.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0dev,>=1.32.0->google-cloud-aiplatform) (0.5.1)\n",
            "Requirement already satisfied: pypdf in /usr/local/lib/python3.10/dist-packages (4.0.2)\n",
            "Requirement already satisfied: langchain in /usr/local/lib/python3.10/dist-packages (0.1.8)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (6.0.1)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.0.27)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (3.9.3)\n",
            "Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (4.0.3)\n",
            "Requirement already satisfied: dataclasses-json<0.7,>=0.5.7 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.6.4)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain) (1.33)\n",
            "Requirement already satisfied: langchain-community<0.1,>=0.0.21 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.0.21)\n",
            "Requirement already satisfied: langchain-core<0.2,>=0.1.24 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.1.24)\n",
            "Requirement already satisfied: langsmith<0.2.0,>=0.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (0.1.3)\n",
            "Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (1.25.2)\n",
            "Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.6.1)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.31.0)\n",
            "Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (8.2.3)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.3.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (23.2.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.4.1)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.0.5)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.9.4)\n",
            "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain) (3.20.2)\n",
            "Requirement already satisfied: typing-inspect<1,>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from dataclasses-json<0.7,>=0.5.7->langchain) (0.9.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain) (2.4)\n",
            "Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.24->langchain) (3.7.1)\n",
            "Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2,>=0.1.24->langchain) (23.2)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain) (0.6.0)\n",
            "Requirement already satisfied: pydantic-core==2.16.2 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain) (2.16.2)\n",
            "Requirement already satisfied: typing-extensions>=4.6.1 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain) (4.9.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (2024.2.2)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (3.0.3)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.24->langchain) (1.3.0)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2,>=0.1.24->langchain) (1.2.0)\n",
            "Requirement already satisfied: mypy-extensions>=0.3.0 in /usr/local/lib/python3.10/dist-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain) (1.0.0)\n",
            "Requirement already satisfied: shapely==2.0.0 in /usr/local/lib/python3.10/dist-packages (2.0.0)\n",
            "Requirement already satisfied: numpy>=1.14 in /usr/local/lib/python3.10/dist-packages (from shapely==2.0.0) (1.25.2)\n",
            "Requirement already satisfied: chromadb in /usr/local/lib/python3.10/dist-packages (0.4.22)\n",
            "Requirement already satisfied: build>=1.0.3 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.0.3)\n",
            "Requirement already satisfied: requests>=2.28 in /usr/local/lib/python3.10/dist-packages (from chromadb) (2.31.0)\n",
            "Requirement already satisfied: pydantic>=1.9 in /usr/local/lib/python3.10/dist-packages (from chromadb) (2.6.1)\n",
            "Requirement already satisfied: chroma-hnswlib==0.7.3 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.7.3)\n",
            "Requirement already satisfied: fastapi>=0.95.2 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.109.2)\n",
            "Requirement already satisfied: uvicorn[standard]>=0.18.3 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.27.1)\n",
            "Requirement already satisfied: numpy>=1.22.5 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.25.2)\n",
            "Requirement already satisfied: posthog>=2.4.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (3.4.1)\n",
            "Requirement already satisfied: typing-extensions>=4.5.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (4.9.0)\n",
            "Requirement already satisfied: pulsar-client>=3.1.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (3.4.0)\n",
            "Requirement already satisfied: onnxruntime>=1.14.1 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.17.0)\n",
            "Requirement already satisfied: opentelemetry-api>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.22.0)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.22.0)\n",
            "Requirement already satisfied: opentelemetry-instrumentation-fastapi>=0.41b0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.43b0)\n",
            "Requirement already satisfied: opentelemetry-sdk>=1.2.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.22.0)\n",
            "Requirement already satisfied: tokenizers>=0.13.2 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.15.2)\n",
            "Requirement already satisfied: pypika>=0.48.9 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.48.9)\n",
            "Requirement already satisfied: tqdm>=4.65.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (4.66.2)\n",
            "Requirement already satisfied: overrides>=7.3.1 in /usr/local/lib/python3.10/dist-packages (from chromadb) (7.7.0)\n",
            "Requirement already satisfied: importlib-resources in /usr/local/lib/python3.10/dist-packages (from chromadb) (6.1.1)\n",
            "Requirement already satisfied: grpcio>=1.58.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (1.60.1)\n",
            "Requirement already satisfied: bcrypt>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from chromadb) (4.1.2)\n",
            "Requirement already satisfied: typer>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (0.9.0)\n",
            "Requirement already satisfied: kubernetes>=28.1.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (29.0.0)\n",
            "Requirement already satisfied: tenacity>=8.2.3 in /usr/local/lib/python3.10/dist-packages (from chromadb) (8.2.3)\n",
            "Requirement already satisfied: PyYAML>=6.0.0 in /usr/local/lib/python3.10/dist-packages (from chromadb) (6.0.1)\n",
            "Requirement already satisfied: mmh3>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from chromadb) (4.1.0)\n",
            "Requirement already satisfied: packaging>=19.0 in /usr/local/lib/python3.10/dist-packages (from build>=1.0.3->chromadb) (23.2)\n",
            "Requirement already satisfied: pyproject_hooks in /usr/local/lib/python3.10/dist-packages (from build>=1.0.3->chromadb) (1.0.0)\n",
            "Requirement already satisfied: tomli>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from build>=1.0.3->chromadb) (2.0.1)\n",
            "Requirement already satisfied: starlette<0.37.0,>=0.36.3 in /usr/local/lib/python3.10/dist-packages (from fastapi>=0.95.2->chromadb) (0.36.3)\n",
            "Requirement already satisfied: certifi>=14.05.14 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2024.2.2)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (1.16.0)\n",
            "Requirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2.8.2)\n",
            "Requirement already satisfied: google-auth>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2.27.0)\n",
            "Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (1.7.0)\n",
            "Requirement already satisfied: requests-oauthlib in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (1.3.1)\n",
            "Requirement already satisfied: oauthlib>=3.2.2 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (3.2.2)\n",
            "Requirement already satisfied: urllib3>=1.24.2 in /usr/local/lib/python3.10/dist-packages (from kubernetes>=28.1.0->chromadb) (2.0.7)\n",
            "Requirement already satisfied: coloredlogs in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb) (15.0.1)\n",
            "Requirement already satisfied: flatbuffers in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb) (23.5.26)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb) (3.20.3)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from onnxruntime>=1.14.1->chromadb) (1.12)\n",
            "Requirement already satisfied: deprecated>=1.2.6 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-api>=1.2.0->chromadb) (1.2.14)\n",
            "Requirement already satisfied: importlib-metadata<7.0,>=6.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-api>=1.2.0->chromadb) (6.11.0)\n",
            "Requirement already satisfied: backoff<3.0.0,>=1.10.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (2.2.1)\n",
            "Requirement already satisfied: googleapis-common-protos~=1.52 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.62.0)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-common==1.22.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.22.0)\n",
            "Requirement already satisfied: opentelemetry-proto==1.22.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.22.0)\n",
            "Requirement already satisfied: opentelemetry-instrumentation-asgi==0.43b0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.43b0)\n",
            "Requirement already satisfied: opentelemetry-instrumentation==0.43b0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.43b0)\n",
            "Requirement already satisfied: opentelemetry-semantic-conventions==0.43b0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.43b0)\n",
            "Requirement already satisfied: opentelemetry-util-http==0.43b0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.43b0)\n",
            "Requirement already satisfied: setuptools>=16.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation==0.43b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (67.7.2)\n",
            "Requirement already satisfied: wrapt<2.0.0,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation==0.43b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (1.14.1)\n",
            "Requirement already satisfied: asgiref~=3.0 in /usr/local/lib/python3.10/dist-packages (from opentelemetry-instrumentation-asgi==0.43b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (3.7.2)\n",
            "Requirement already satisfied: monotonic>=1.5 in /usr/local/lib/python3.10/dist-packages (from posthog>=2.4.0->chromadb) (1.6)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic>=1.9->chromadb) (0.6.0)\n",
            "Requirement already satisfied: pydantic-core==2.16.2 in /usr/local/lib/python3.10/dist-packages (from pydantic>=1.9->chromadb) (2.16.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.28->chromadb) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.28->chromadb) (3.6)\n",
            "Requirement already satisfied: huggingface_hub<1.0,>=0.16.4 in /usr/local/lib/python3.10/dist-packages (from tokenizers>=0.13.2->chromadb) (0.20.3)\n",
            "Requirement already satisfied: click<9.0.0,>=7.1.1 in /usr/local/lib/python3.10/dist-packages (from typer>=0.9.0->chromadb) (8.1.7)\n",
            "Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.10/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.14.0)\n",
            "Requirement already satisfied: httptools>=0.5.0 in /usr/local/lib/python3.10/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.6.1)\n",
            "Requirement already satisfied: python-dotenv>=0.13 in /usr/local/lib/python3.10/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (1.0.1)\n",
            "Requirement already satisfied: uvloop!=0.15.0,!=0.15.1,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.19.0)\n",
            "Requirement already satisfied: watchfiles>=0.13 in /usr/local/lib/python3.10/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.21.0)\n",
            "Requirement already satisfied: websockets>=10.4 in /usr/local/lib/python3.10/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (12.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (5.3.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.3.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (4.9)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface_hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb) (3.13.1)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb) (2023.6.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata<7.0,>=6.0->opentelemetry-api>=1.2.0->chromadb) (3.17.0)\n",
            "Requirement already satisfied: anyio<5,>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from starlette<0.37.0,>=0.36.3->fastapi>=0.95.2->chromadb) (3.7.1)\n",
            "Requirement already satisfied: humanfriendly>=9.1 in /usr/local/lib/python3.10/dist-packages (from coloredlogs->onnxruntime>=1.14.1->chromadb) (10.0)\n",
            "Requirement already satisfied: mpmath>=0.19 in /usr/local/lib/python3.10/dist-packages (from sympy->onnxruntime>=1.14.1->chromadb) (1.3.0)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.37.0,>=0.36.3->fastapi>=0.95.2->chromadb) (1.3.0)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.37.0,>=0.36.3->fastapi>=0.95.2->chromadb) (1.2.0)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.5.1)\n"
          ]
        }
      ],
      "source": [
        "# Installing the dependencies\n",
        "!pip install google-cloud-aiplatform\n",
        "!pip install pypdf\n",
        "!pip install langchain\n",
        "!pip install shapely==2.0.0 # provide a natural way to compute which features contribute to a prediction or contribute to the uncertainty of a prediction.\n",
        "!pip install chromadb #open-source vector storage system (vector database) designed for the storing and retrieving vector embeddings"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import auth\n",
        "\n",
        "auth.authenticate_user()"
      ],
      "metadata": {
        "id": "G1L2C_yIlXBw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#!sudo add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null\n",
        "#!sudo apt-get update -qq 2>&1 > /dev/null\n",
        "#!sudo apt -y install -qq google-drive-ocamlfuse 2>&1 > /dev/null\n",
        "#!google-drive-ocamlfuse"
      ],
      "metadata": {
        "id": "UD1L0YrSlXQM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from langchain.document_loaders import PyPDFLoader\n",
        "\n",
        "\n",
        "def context_extractor(file_path):\n",
        "    #text_extensions = ['.txt', '.csv']  # Add more text extensions if needed\n",
        "    text_extensions = ['.csv']\n",
        "    #pdf_extensions = ['.pdf']  # Add more PDF extensions if needed\n",
        "    text = ''\n",
        "    file_extension = os.path.splitext(file_path)[1].lower()\n",
        "\n",
        "    if file_extension in text_extensions:\n",
        "        with open(file_path, 'r') as file:\n",
        "            text = file.read()\n",
        "        return text\n",
        "    elif file_extension in pdf_extensions:\n",
        "        text = ''\n",
        "        pdf_loader = PyPDFLoader(file_path)\n",
        "        pages = pdf_loader.load_and_split()\n",
        "        for i in pages:\n",
        "            text = text +\"\\n\\n\" + i.page_content\n",
        "        return text\n",
        "    else:\n",
        "        return 'Unknown file type'\n",
        "\n"
      ],
      "metadata": {
        "id": "hnTDrkW5lXMG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "\n",
        "def get_file_paths(directory):\n",
        "    file_paths = []\n",
        "    for root, _, files in os.walk(directory):\n",
        "        for file in files:\n",
        "            file_path = os.path.join(root, file)\n",
        "            file_paths.append(file_path)\n",
        "    return file_paths"
      ],
      "metadata": {
        "id": "pzZKmyDxlXT3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain.text_splitter import CharacterTextSplitter\n",
        "\n",
        "def create_context(dir_path):\n",
        "  file_paths = get_file_paths(dir_path)\n",
        "  texts_list = []\n",
        "  for file_path in file_paths:\n",
        "      print(file_path)\n",
        "      text = context_extractor(file_path)\n",
        "      text_splitter = CharacterTextSplitter(chunk_size=3000, chunk_overlap=100)\n",
        "      context = text\n",
        "      texts = text_splitter.split_text(context)\n",
        "      for i in texts:\n",
        "        texts_list.append(i)\n",
        "  for chunk_index, chunk in enumerate(texts_list):\n",
        "      # print(chunk)\n",
        "      # Create a unique file name for each chunk\n",
        "      chunk_file_name = f\"/content/chunks/chunk_{chunk_index}.txt\"\n",
        "\n",
        "      # Save the chunk as a text file\n",
        "      with open(chunk_file_name, 'w') as file:\n",
        "          file.write(chunk)\n",
        "\n",
        "      # Print the file path of the saved chunk\n",
        "      print(f\"Saved chunk {chunk_index} as {chunk_file_name}\")"
      ],
      "metadata": {
        "id": "p9fe3aFTlXYX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def read_chunks(dir_path):\n",
        "    context_paths = get_file_paths(dir_path)\n",
        "    chunks = []\n",
        "    for context_path in context_paths:\n",
        "        with open(context_path, 'r') as file:\n",
        "            chunk = file.read()\n",
        "            chunks.append(chunk)\n",
        "            print(chunk)\n",
        "    return chunks"
      ],
      "metadata": {
        "id": "3-vVH-dICJTo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dir_path = \"/content/\""
      ],
      "metadata": {
        "id": "mCJDlEAciVZv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "file_path = '/content/FMCG_data_try2.csv'"
      ],
      "metadata": {
        "id": "N9afUslJmX_X"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "directory = \"/content/\""
      ],
      "metadata": {
        "id": "wdQlafOcmi9I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#read_chunks(/content/sample_data)"
      ],
      "metadata": {
        "id": "ValEKlWMnHYP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def read_chunks(dir_path):\n",
        "    context_paths = get_file_paths(dir_path)\n",
        "    chunks = []\n",
        "    for context_path in context_paths:\n",
        "        with open(context_path, 'r') as file:\n",
        "            chunk = file.read()\n",
        "            chunks.append(chunk)\n",
        "            print(chunk)\n",
        "    return chunks"
      ],
      "metadata": {
        "id": "FbfKVHig0qv8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import vertexai\n",
        "import warnings\n",
        "from langchain.embeddings import VertexAIEmbeddings\n",
        "from langchain.llms import VertexAI\n",
        "from langchain.vectorstores import Chroma\n",
        "import os\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "\n",
        "PROJECT_ID = \"studied-triode-407210\"\n",
        "#REGION = \"southamerica-east1\"\n",
        "#REGION = \"us-central1\"\n",
        "REGION = \"northamerica-northeast1\"\n",
        "\n",
        "vertexai.init(project=PROJECT_ID, location=REGION)\n"
      ],
      "metadata": {
        "id": "4PdZwJQECUti"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#ValueError: Unsupported region for Vertex AI, select from frozenset({'europe-west8', 'us-west3', 'europe-southwest1', 'europe-west4', 'asia-southeast1', 'asia-northeast2', 'australia-southeast1', 'europe-west2', 'us-east1', 'europe-west9', 'us-west4', 'europe-west3', 'us-east4', 'us-central1', 'europe-central2', 'asia-northeast3', 'europe-west1', 'asia-southeast2', 'asia-east1', 'northamerica-northeast2', 'southamerica-east1', 'northamerica-northeast1', 'australia-southeast2', 'europe-north1', 'us-west2', 'europe-west6', 'southamerica-west1', 'asia-south1', 'me-west1', 'us-south1', 'asia-east2', 'us-west1', 'asia-northeast1'})"
      ],
      "metadata": {
        "id": "x5OSKuGV2iYb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# parameters for model\n",
        "#parameters = {\n",
        " #   \"temperature\": 0.2,\n",
        "  #  \"max_output_tokens\": 380,\n",
        "   # \"top_p\": 0.8,\n",
        "    #\"top_k\": 40\n",
        "#}"
      ],
      "metadata": {
        "id": "kE8vcsFrCUye"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# parameters for model\n",
        "parameters = {\n",
        "    \"temperature\": 0.1,\n",
        "    \"max_output_tokens\": 1000,\n",
        "    \"top_p\": 0.8,\n",
        "    \"top_k\": 40\n",
        "}"
      ],
      "metadata": {
        "id": "DvQ245536UDE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#TextGenerationModel(model_id: str, endpoint_name: Optional[str] = None)"
      ],
      "metadata": {
        "id": "zBi6pLv0yyOn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#getting the text model\n",
        "from vertexai.language_models import TextGenerationModel\n",
        "model = TextGenerationModel.from_pretrained(\"text-bison@001\")\n",
        "vertex_embeddings = VertexAIEmbeddings(model_name=\"textembedding-gecko@001\")"
      ],
      "metadata": {
        "id": "HjiyGb2suyiV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# pass the path to directory containing documents\n",
        "create_context('/content/documents')\n",
        "#create_context('/content/sample_data/')"
      ],
      "metadata": {
        "id": "ZjuKz9QPeDev",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "11953aab-5fda-4604-e5aa-7717f79f7ed9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/documents/FMCG_data_try2.csv\n",
            "Saved chunk 0 as /content/chunks/chunk_0.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# load chunks\n",
        "chunks = read_chunks('/content/chunks')\n",
        "#chunks = read_chunks('/content/sample_data/')\n",
        "#chunks = read_chunks()\n",
        "\n",
        "# create embeddings from chunks\n",
        "vector_index = Chroma.from_texts(chunks, vertex_embeddings).as_retriever()\n",
        "#vector_index = Chroma.from_texts(chunks, vertex_embeddings).as_retriever(search_kwargs={\"k\": 4})"
      ],
      "metadata": {
        "id": "HZE6RiCBGfrU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e2ade929-8f22-4e40-936b-10a87c7de4f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WarehouseID,WHManagerID,Locationtype,WHcapacitysize,zone,WHregionalzone,numrefillreql3m,transportissuel1y,Competitorinmkt,retailshopnum,whownertype,distributornum,floodimpacted,floodproof,electricsupply,distfromhub,workersnum,whestyear,storageissuereportedl3m,tempregmach,approvedwhgovtcertificate,whbreakdownl3m,govtcheckl3m,productwgton\n",
            "WH100000,EID50000,Urban,Small,West,Zone 6,3,1,2,4651,Rented,24,0,1,1,91,29,,13,0,A,5,15,17115\n",
            "WH100001,EID50001,Rural,Large,North,Zone 5,0,0,4,6217,Company Owned,47,0,0,1,210,31,,4,0,A,3,17,5074\n",
            "WH100002,EID50002,Rural,Mid,South,Zone 2,1,0,4,4306,Company Owned,64,0,0,0,161,37,,17,0,A,6,22,23137\n",
            "WH100003,EID50003,Rural,Mid,North,Zone 3,7,4,2,6000,Rented,50,0,0,0,103,21,,17,1,A,3,27,22115\n",
            "WH100004,EID50004,Rural,Large,North,Zone 5,3,1,2,4740,Company Owned,42,1,0,1,112,25,2009,18,0,C,6,24,24071\n",
            "WH100005,EID50005,Rural,Small,West,Zone 1,8,0,2,5053,Rented,37,0,0,1,152,35,2009,23,1,A,3,3,32134\n",
            "WH100006,EID50006,Rural,Large,West,Zone 6,8,0,4,4449,Company Owned,38,0,0,1,77,27,2010,24,0,B,3,6,30142\n",
            "WH100007,EID50007,Rural,Large,North,Zone 5,1,0,4,7183,Rented,45,0,0,0,241,23,,18,0,C,6,24,24093\n",
            "WH100008,EID50008,Rural,Small,South,Zone 6,8,1,4,5381,Rented,42,0,0,1,124,22,2013,13,1,A,5,2,18082\n",
            "WH100009,EID50009,Rural,Small,South,Zone 6,4,3,3,3869,Company Owned,35,0,0,0,78,43,,6,0,C,6,2,7130\n",
            "WH100010,EID50010,Rural,Large,North,Zone 6,7,1,3,4623,Company Owned,31,0,0,1,150,37,1999,17,0,B,4,6,21125\n",
            "WH100011,EID50011,Rural,Large,North,Zone 6,7,0,5,4627,Rented,40,0,0,0,225,16,2017,11,0,B,2,28,14115\n",
            "WH100012,EID50012,Urban,Mid,North,Zone 2,4,0,3,5012,Rented,48,0,0,0,95,28,2022,4,0,B,1,1,5124\n",
            "WH100013,EID50013,Rural,Mid,South,Zone 4,6,1,2,6858,Company Owned,26,0,0,1,242,36,2008,22,1,A,5,11,30063\n",
            "WH100014,EID50014,Rural,Small,West,Zone 6,8,1,4,5022,Rented,68,0,0,1,129,37,,6,0,B,3,9,7055\n",
            "WH100015,EID50015,Rural,Mid,North,Zone 2,1,1,3,5062,Company Owned,50,0,0,1,190,19,,4,0,B,3,12,5094\n",
            "WH100016,EID50016,Rural,Mid,West,Zone 4,0,0,2,5569,Company Owned,16,1,0,1,231,28,,9,0,B,5,11,12127\n",
            "WH100017,EID50017,Rural,Mid,West,Zone 2,0,1,2,5539,Company Owned,28,0,0,1,261,22,,13,0,A,4,12,17134\n",
            "WH100018,EID50018,Rural,Mid,North,Zone 3,4,1,4,4598,Rented,58,0,0,1,159,22,2001,29,1,A,5,27,38082\n",
            "WH100019,EID50019,Rural,Small,South,Zone 1,1,1,2,5679,Rented,19,0,0,1,189,24,,22,0,B,2,21,27100\n",
            "WH100020,EID50020,Rural,Mid,South,Zone 2,8,0,2,5678,Company Owned,31,0,0,1,65,41,2016,19,0,B,4,1,24062\n",
            "WH100021,EID50021,Rural,Mid,South,Zone 3,6,0,2,3980,Company Owned,49,0,0,1,156,31,2010,14,1,B,6,19,17117\n",
            "WH100022,EID50022,Rural,Small,North,Zone 6,5,0,4,3588,Company Owned,69,0,0,0,199,24,1997,28,1,C,6,8,40150\n",
            "WH100023,EID50023,Rural,Mid,South,Zone 3,8,1,2,4388,Company Owned,32,0,0,1,80,37,2003,25,0,C,5,19,32098\n",
            "WH100024,EID50024,Urban,Large,West,Zone 5,1,0,4,5670,Rented,25,0,0,1,140,31,,12,0,C,2,14,15125\n",
            "WH100025,EID50025,Rural,Mid,North,Zone 3,7,1,3,5496,Company Owned,46,0,0,0,67,31,2006,22,0,B,3,27,26066\n",
            "WH100026,EID50026,Rural,Small,West,Zone 6,5,3,4,4063,Company Owned,40,0,0,1,229,21,,8,0,C,6,9,10077\n",
            "WH100027,EID50027,Rural,Small,South,Zone 6,8,3,2,5790,Rented,31,0,0,0,98,36,,11,0,C,4,9,14150\n",
            "WH100028,EID50028,Rural,Small,North,Zone 6,3,1,1,7692,Company Owned,62,1,0,0,154,20,,0,0,NA,0,8,3123\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# main driver function\n",
        "#This is the driver code, which will query the LLM and generate the responses\n",
        "def run_query(question):\n",
        "    # get the chunks having possibility of containing answer\n",
        "    docs = vector_index.get_relevant_documents(question)\n",
        "    answers = ''\n",
        "    for i in docs:\n",
        "        # query the LLM\n",
        "        response = model.predict(\n",
        "          f\"Answer the question as precise as possible using the provided context.\\\n",
        "          Only take answers from the document provided\\\n",
        "          Do not get any answers from the internet sources\\\n",
        "           If the answer is not contained in the context, say 'answer not available \\\n",
        "           in context'. \\n\\n Context: \\n {i.page_content} \\nQuestion: \\n {question} \\n\",\n",
        "          **parameters\n",
        "        )\n",
        "        # append the answers\n",
        "        answers = answers + \"\\n\\n\" + response.text\n",
        "\n",
        "    final_response = model.predict(\n",
        "        f\"Given the extracted content and the question, create a conversational \\\n",
        "        final answer. If the answer is not contained in the context or if the context\\\n",
        "         is empty then, say 'answer not available in context'. \\n\\n Context: \\n \\\n",
        "         {answers} \\nQuestion: \\n {question} \\n\",\n",
        "        **parameters\n",
        "        )\n",
        "    return final_response.text"
      ],
      "metadata": {
        "id": "Aw0ipDo-tdJS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(\"WHregional_zone\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p10AslMRgmFO",
        "outputId": "aedb8ca9-cb8a-4ab9-fdd7-a4848275c5ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The WHregional_zone is Zone 6.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \"what are the column names in this data\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zcyl7mZhoVQn",
        "outputId": "5e7d5704-28fe-48e2-e6ca-0e12c9dfc009"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The column names are:\n",
            "\n",
            "WarehouseID\n",
            "WHManagerID\n",
            "Locationtype\n",
            "WHcapacitysize\n",
            "zone\n",
            "WHregionalzone\n",
            "numrefillreql3m\n",
            "transportissuel1y\n",
            "Competitorinmkt\n",
            "retailshopnum\n",
            "whownertype\n",
            "distributornum\n",
            "floodimpacted\n",
            "floodproof\n",
            "electricsupply\n",
            "distfromhub\n",
            "workersnum\n",
            "whestyear\n",
            "storageissuereportedl3m\n",
            "tempregmach\n",
            "approvedwhgovtcertificate\n",
            "whbreakdownl3m\n",
            "govtcheckl3m\n",
            "productwgton\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \" Which WarehouseID has the heighest Competitorinmkt\"))"
      ],
      "metadata": {
        "id": "m4qE5um3gmc_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1e5971b5-2ca9-4e2a-867b-6f6265e55161"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WH100004\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \" what is the Competitorinmkt for WarehouseID WH100011?\"))"
      ],
      "metadata": {
        "id": "qGr1cLL9noUj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1bf8b8ca-f434-4af1-be34-be63793c329c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The answer is 2.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \"How many unique zones do we have?\"))"
      ],
      "metadata": {
        "id": "7Y5mugs5noX0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f7f113f9-2994-4fcf-a22e-f467483630ed"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "There are 5 unique zones in the data.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \"what is the maximum in last column?\"))"
      ],
      "metadata": {
        "id": "yIaSLZqSnobL",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "564118e2-868c-41c0-ef64-7c8dc042e02b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The maximum value in the last column is 7692.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \"what is the maximum distributor num\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xHIVYwhPPIKX",
        "outputId": "d648fc40-d66e-4386-cb2c-d3a4e3cd5a10"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The maximum number of distributors is 28.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \"print top 5 rows of data\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vZqpj-Q6PIPO",
        "outputId": "dcfb20b1-eed3-4b52-9cae-2fc92ff075bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sure, here are the top 5 rows of data:\n",
            "\n",
            "WarehouseID,WHManagerID,Locationtype,WHcapacitysize,zone,WHregionalzone,numrefillreql3m,transportissuel1y,Competitorinmkt,retailshopnum,whownertype,distributornum,floodimpacted,floodproof,electricsupply,distfromhub,workersnum,whestyear,storageissuereportedl3m,tempregmach,approvedwhgovtcertificate,whbreakdownl3m,govtcheckl3m,productwgton\n",
            "WH100000,EID50000,Urban,Small,West,Zone 6,3,1,2,4651,Rented,24,0,1,1,91,29,,13,0,A,5,15,17115\n",
            "WH100001,EID50001,Rural,Large,North,Zone 5,0,0,4,6217,Company Owned,47,0,0,1,210,31,,4,0,A,3,17,5074\n",
            "WH100002,EID50002,Rural,Mid,South,Zone 2,1,0,4,4306,Company Owned,64,0,0,0,161,37,,17,0,A,6,22,23137\n",
            "WH100003,EID50003,Rural,Mid,North,Zone 3,7,4,2,6000,Rented,50,0,0,0,103,21,,17,1,A,3,27,22115\n",
            "WH100004,EID50004,Rural,Large,North,Zone 5,3,1,2,4740,Company Owned,42,1,0,1,112,25,2009,18,0,C,6,24,24071\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \"print a table of last 5 rows of data with headers\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MIe8WvJKPITK",
        "outputId": "9553807d-366c-4d4e-9923-a687e24c5b22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WarehouseID\tWHManagerID\tLocationtype\tWHcapacitysize\tzone\tWHregionalzone\tnumrefillreql3m\ttransportissuel1y\tCompetitorinmkt\tretailshopnum\twhownertype\tdistributornum\tfloodimpacted\tfloodproof\telectricsupply\tdistfromhub\tworkersnum\twhestyear\tstorageissuereportedl3m\ttempregmach\tapprovedwhgovtcertificate\twhbreakdownl3m\tgovtcheckl3m\tproductwgton\n",
            "WH100029\tEID50029\tRural\tMid\tSouth\tZone 3\t1\t0\t4\t5341\tCompany Owned\t41\t0\t0\t1\t125\t32\t\t16\t0\tB\t4\t14\t20115\n",
            "WH100030\tEID50030\tRural\tMid\tNorth\tZone 3\t1\t0\t2\t5015\tCompany Owned\t52\t0\t0\t1\t143\t30\t\t14\t0\tB\t4\t12\t16100\n",
            "WH100031\tEID50031\tRural\tMid\tWest\tZone 3\t1\t0\t1\t4831\tCompany Owned\t45\t0\t0\t1\t136\t28\t\t12\t0\tB\t4\t12\t15100\n",
            "WH100032\tEID50032\tRural\tMid\tSouth\tZone 3\t1\t0\t1\t4991\tCompany Owned\t48\t0\t0\t1\t139\t29\t\t13\t0\tB\t4\t12\t15600\n",
            "WH100033\tEID50033\tRural\tMid\tNorth\tZone 3\t1\t0\t1\t4871\tCompany Owned\t46\t0\t0\t1\t137\t28\t\t12\t0\tB\t4\t12\t15300\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "run_query(question = \"print third column\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "QBpk8Eb8PIXU",
        "outputId": "f471e264-bd9e-4d2a-d7f1-f7e79a8e842d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'The third column of the table is the location type. The location type can be urban, rural, or suburban.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question = \"print a table of last 10 rows of data with headers\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "926y8UodPIo1",
        "outputId": "864f48c3-7939-45bb-94b0-402803ea6db5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:chromadb.segment.impl.vector.local_hnsw:Number of requested results 4 is greater than number of elements in index 1, updating n_results = 1\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WarehouseID\tWHManagerID\tLocationtype\tWHcapacitysize\tzone\tWHregionalzone\tnumrefillreql3m\ttransportissuel1y\tCompetitorinmkt\tretailshopnum\twhownertype\tdistributornum\tfloodimpacted\tfloodproof\telectricsupply\tdistfromhub\tworkersnum\twhestyear\tstorageissuereportedl3m\ttempregmach\tapprovedwhgovtcertificate\twhbreakdownl3m\tgovtcheckl3m\tproductwgton\n",
            "WH100028\tEID50028\tRural\tSmall\tNorth\tZone 6\t3\t1\t1\t7692\tCompany Owned\t62\t1\t0\t0\t154\t20\t\t0\t0\tNA\t0\t8\t3123\n",
            "WH100029\tEID50029\tRural\tMid\tSouth\tZone 3\t1\t0\t4\t5246\tCompany Owned\t51\t0\t0\t1\t150\t30\t\t11\t0\tB\t3\t15\t19113\n",
            "WH100030\tEID50030\tRural\tMid\tSouth\tZone 3\t6\t0\t2\t5326\tCompany Owned\t43\t0\t0\t1\t164\t32\t2013\t16\t0\tB\t5\t19\t20121\n",
            "WH100031\tEID50031\tRural\tMid\tSouth\tZone 3\t5\t0\t2\t4547\tCompany Owned\t41\t0\t0\t1\t119\t34\t2010\t18\t0\tB\t4\t16\t22106\n",
            "WH100032\tEID50032\tRural\tMid\tSouth\tZone 3\t1\t0\t2\t4641\tCompany Owned\t46\t0\t0\t1\t135\t34\t2013\t18\t0\tB\t4\t19\t23112\n",
            "WH100033\tEID50033\tRural\tMid\tSouth\tZone 3\t7\t0\t2\t4891\tCompany Owned\t42\t0\t0\t1\t124\t34\t2010\t18\t0\tB\t4\t16\t24114\n",
            "WH100034\tEID50034\tRural\tMid\tSouth\tZone 3\t1\t0\t2\t4991\tCompany Owned\t44\t0\t0\t1\t140\t34\t2013\t18\t0\tB\t4\t19\t25115\n",
            "WH100035\tEID50035\tRural\tMid\tSouth\tZone 3\t6\t0\t2\t5091\tCompany Owned\t45\t0\t0\t1\t156\t34\t2010\t18\t0\tB\t4\t16\t26116\n",
            "WH100036\tEID50036\tRural\tMid\tSouth\tZone 3\t1\t0\t2\t5191\tCompany Owned\t46\t0\t0\t1\t172\t34\t2013\t18\t0\tB\t4\t19\t27117\n",
            "WH100037\tEID50037\tRural\tMid\tSouth\tZone 3\t7\t0\t2\t5291\tCompany Owned\t47\t0\t0\t1\t188\t34\t2010\t18\t0\tB\t4\t16\t28118\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "HYX6fujkPIs_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "oOLuHyCCPIw8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "aB1FRVB3PI05"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BcdBQS05PI4_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8sXCN7HFPI9G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "36HcYPrePJBJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qkfxAW7WPJFA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cysqpE9yPJI3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ogSrS5O1PJNJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "sKZ_nED5PJRI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "jK2otdDIPJUx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ZgGxmCzoPJYf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "P5tHJ7SWnoeH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "c8llgJMGnog1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "RZGcODAjnoj8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "XXF5frI7nome"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "FuptSRjonopg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "9P5EQ-fdnosI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "questions = \"how many WarehouseID?\""
      ],
      "metadata": {
        "id": "-pLT-oyL8H22"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wnVJBbMFnouw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "HBJP16RWno0J"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.predict(\"What is the meaning of life?\")"
      ],
      "metadata": {
        "id": "7MQ5YVgUdVY-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "74853fba-d909-42d7-8eac-a8f2cf2982dd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "I think the meaning of life is to find your passion and pursue it with all your heart. When you find something you love to do, it makes life so much more fulfilling. You feel like you're making a difference in the world, and you're happier and more productive."
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# The code is working above the next step is to pass a pdf or .csv and query from parsed documents."
      ],
      "metadata": {
        "id": "bR78nSPkdiDD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.api_core.client_options import ClientOptions"
      ],
      "metadata": {
        "id": "EN0hYnJ2wQxT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install google-cloud-documentai"
      ],
      "metadata": {
        "id": "c0VFn5Esw5Mc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.api_core.client_options import ClientOptions\n",
        "from google.cloud import documentai"
      ],
      "metadata": {
        "id": "HJT6lN9_xhow"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Set endpoint to EU\n",
        "options = ClientOptions(api_endpoint=\"eu-documentai.googleapis.com:443\")\n",
        "# Instantiates a client\n",
        "client = documentai.DocumentProcessorServiceClient(client_options=options)"
      ],
      "metadata": {
        "id": "blCOLiLQwj2A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#print(run_query(question=questions))"
      ],
      "metadata": {
        "id": "gOcMY2L9uuVF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "questions = 'count WHregional_zone'"
      ],
      "metadata": {
        "id": "L76Pv4sD8t3r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question=questions))"
      ],
      "metadata": {
        "id": "YY74-o-6a1Bt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "XsYyirHw-122"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(run_query(question=questions))"
      ],
      "metadata": {
        "id": "bs29FJEW-2KS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.predict(\"WarehouseID row 4\")"
      ],
      "metadata": {
        "id": "0XFvZfXrOLXN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.predict(\"zone for WarehouseID WH_100002\")"
      ],
      "metadata": {
        "id": "SaLSHZi1Ohaa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.predict(\"What is WH_regional_zone for WarehouseID WH_100002\")"
      ],
      "metadata": {
        "id": "hwtcOMx80mym"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.predict(\"What is the WHcapacity_size for WH_100019\")"
      ],
      "metadata": {
        "id": "tTZzedRA4h-0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "419RMQU24iK6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hxk1F4nS4iWP"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}