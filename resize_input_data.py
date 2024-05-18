import os
import cv2
import argparse

from pathlib import Path


def resize_image(image, size):
    resized_image = cv2.resize(image, (size, size), interpolation=cv2.INTER_AREA)
    return resized_image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--size', type=int, default=1024)
    parser.add_argument('--ext', type=str, default='png')
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    # Get full path
    input_path = input_path.resolve()
    output_path = output_path.resolve()

    # Create output directory if not exists
    if not output_path.exists():
        output_path.mkdir(parents=True)

    for idx, image_path in enumerate(input_path.glob(f'*.{args.ext}')):
        # Ignore if starts with .
        if image_path.name.startswith('.'):
            continue
        # Ignore if directory
        if image_path.is_dir():
            continue

        image = cv2.imread(str(image_path))
        resized_image = resize_image(image, args.size)
        output_image_path = os.path.join(output_path, image_path.name)

        if not cv2.imwrite(output_image_path, resized_image):
            print(f'Failed to write {output_image_path}')
        else:
            print(f'{idx + 1}/{len(list(input_path.glob(f"*.{args.ext}")))}: {image_path} -> {output_image_path}')
