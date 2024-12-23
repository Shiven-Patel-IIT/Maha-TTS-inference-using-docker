import subprocess

#List of packages to install
packages = [
    "annotated-types==0.6.0",
    "audioread==3.0.1",
    "certifi==2023.11.17",
    "cffi==1.16.0",
    "charset-normalizer==3.3.2",
    "decorator==5.1.1",
    "einops==0.7.0",
    "filelock==3.13.1",
    "fsspec==2023.10.0",
    "huggingface-hub==0.19.4",
    "idna==3.4",
    "inflect==7.0.0",
    "Jinja2==3.1.2",
    "joblib==1.3.2",
    "lazy_loader==0.3",
    "librosa==0.10.1",
    "llvmlite==0.41.1",
    "MarkupSafe==2.1.3",
    "mpmath==1.3.0",
    "msgpack==1.0.7",
    "networkx==3.2.1",
    "numba==0.58.1",
    "numpy==1.26.2",
    "packaging==23.2",
    "platformdirs==4.0.0",
    "pooch==1.8.0",
    "pycparser==2.21",
    "pydantic==2.5.1",
    "pydantic_core==2.14.3",
    "PyYAML==6.0.1",
    "regex==2023.10.3",
    "requests==2.31.0",
    "safetensors==0.4.0",
    "scikit-learn==1.3.2",
    "scipy==1.11.3",
    "soundfile==0.12.1",
    "soxr==0.3.7",
    "sympy==1.12",
    "threadpoolctl==3.2.0",
    "tokenizers==0.15.0",
    "tqdm==4.66.1",
    "transformers==4.35.2",
    "typing_extensions==4.8.0",
    "Unidecode==1.3.7",
    "urllib3==2.1.0"
]

# Install each package using pip
for package in packages:
    subprocess.run(["pip", "install", package])

# # Install maha-tts from PyPI or GitHub (uncomment depending on the source)
# subprocess.run(["pip", "install", "maha-tts"])  # If available on PyPI

# # Install torch with CUDA support

subprocess.run(["pip", "install", "torch==2.0.1+cu118", "torchvision==0.15.2+cu118", "-f", "https://download.pytorch.org/whl/torch_stable.html"])

subprocess.run(["pip", "install", "IPython"])
