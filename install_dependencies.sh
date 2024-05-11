pip install -e ./diffusers

pip install -r ./diffusers/examples/dreambooth/requirements.txt

accelerate config default

pip install --force-reinstall torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
