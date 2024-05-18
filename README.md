# stable-diffusion-lora-training

# Steps
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Resize images
```bash
python resize_input_data.py --input data/real_person --output data/real_person_resized --size 1024
```
3. Download submodules
```bash
git submodule update --init --recursive
```
4. Run `GPT4V-Image-Captioner`
    1. `cd GPT4V-Image-Captioner`
    2. `chmod +x install_linux_mac.sh; chmod +x start_linux_mac.sh`
    3. `./install_linux_mac.sh`
    4. `./start_linux_mac.sh`
5. Download models using website
6. Start captioning, parameters:
```
API URL = https://api.openai.com/v1/chat/completions

API Model = gpt-4o

Image Quality = auto

Prompt = Make description to recreate image in Stable Diffusion. Describe model face, pose and background, describe precisely also textures, please be as thorough as possible, use only comma separated adjectives and sentence equivalents, here is an example of such description: """photo of a young adult male, distinct style, slicked back undercut hairstyle, numerous tattoos visible on face, numerous tattoos visible on face, numerous tattoos visible on arms, medium skin tone, sharp facial features, pronounced cheekbones, well-defined jawline, prominent chin, eyes focused towards the camera, neutral expression, straight eyebrow tattooed above his right eyebrow, other facial tattoos that add to his edgy appearance, seated at a wooden table, wearing a casual, short-sleeved white button-down shirt, partially unbuttoned, revealing part of his chest and more tattoos, relaxed posture, body slightly angled towards the camera, left hand placed on an open book on the table, showing his tattooed arms, outdoors during a sunset, soft and warm lighting that creates a tranquil atmosphere, serene field with blooming flowers (possibly cotton or another soft-textured plant) in the background (stretching out towards the horizon), clear partly cloudy sky with sun setting and emanating golden hues is in the distance, casting glow over the scenery"""

Model = moondream

API = GPT4V
```