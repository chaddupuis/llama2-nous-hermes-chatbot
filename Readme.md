

## Model Download
In local venv with pip install hugginface-hub

huggingface-cli download TheBloke/Nous-Hermes-Llama2-GGUF nous-hermes-llama2-13b.Q4_K_M.gguf --local-dir ./Nous-Hermes-Llama2-GGUF --local-dir-use-symlinks False

put in resources/....

## Python venv
python3 -m venv .env
source .env/bin/activate
pip3 install -r ./requirements.txt

## General Notes
For a single gpu low resource machine this uses ctransformers with gpu_layers=25 - that ends up using ~6GB gpu memory.  Any higher and cuda OOM errors start.
