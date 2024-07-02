import base64
import requests
import os
from openai import OpenAI
from PIL import Image
import io
import json
import argparse
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filePath", type=str)
    parser.add_argument("--startingNum", type=int)
    parser.add_argument("--api", type=str)
    parser.add_argument("--description", type=str)
    args = parser.parse_args()
    return args
def concatenate_images(image_paths, direction='horizontal'):
    """
    Concatenate multiple images into one.
    :param image_paths: List of file paths of images to be concatenated
    :param direction: 'horizontal' or 'vertical'
    :return: Concatenated image
    """
    images = [Image.open(path) for path in image_paths]
    
    # Determine the size of the output image
    if direction == 'horizontal':
        width = sum(img.width for img in images)
        height = max(img.height for img in images)
    else:  # vertical
        width = max(img.width for img in images)
        height = sum(img.height for img in images)
    
    # Create a new image with the appropriate size
    concatenated = Image.new('RGB', (width, height))
    
    offset = 0
    for img in images:
        if direction == 'horizontal':
            concatenated.paste(img, (offset, 0))
            offset += img.width
        else:  # vertical
            concatenated.paste(img, (0, offset))
            offset += img.height
    
    return concatenated

def resize_image(img, max_size=(500, 500), quality=75):
    # Convert image to RGB if it's not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Resize the image
    img.thumbnail(max_size)
    
    # Save the image to a bytes buffer
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG", quality=quality, optimize=True)
    return buffered.getvalue()

def encode_image(image_data):
    return base64.b64encode(image_data).decode('utf-8')

def analyze_images(apiKey, description, images, resize=True, max_size=(500, 500)):
    api_url = 'https://api.openai.com/v1'
    client = OpenAI(
        api_key = apiKey,
        base_url=api_url
    )

    # Encode all images
    encoded_images = []
    for img in images:
        if resize:
            image_data = resize_image(img, max_size)
        else:
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            image_data = buffered.getvalue()
        encoded_images.append(encode_image(image_data))

    # Prepare the messages for the API call
    messages = [
        {
            "role": "user",
            "content": [        
                {"type": "text", "text": "Please act like the description provided: " + description + " (end of description) Please take in and go over all 350 images and in the end assess the potential negative (the negative effects can only come from what is inside each photo of the content) effect it could have on you (remember you are acting like the description). Address the negative effects from the images (the impacts should only come from the images you received, it shouldn't be things such as shortened attention span or mixed content, which have nothing to do with the content, its just related to short videos in general) you received as well and please reference where you got it from specifically. Give a predicted negative impact considering only the negatives (ex negligible, minimal, moderate, significant, large impact) from taking in those photos (only use the photos provided and do not make anything up or say that an effect may be possible because something can possibly show up. only base the effect on the things you saw). GET ALL YOUR INFO FROM THE PHOTOS PROVIDED. DO NOT BRING IN OUTSIDE INFO. ONLY USE THE PHOTOS YOU GOT. ONLY ASSESS THE EFFECT. Finally, at the end be sure to put the net impact you think it had."}
                ] + [ 
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}}
                for img in encoded_images
            ]
        }
    ]

    # Make the API call with streaming
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=4096,
        stream=True,
        timeout=1000
    )
    # Process the streaming response
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            print(content, end='', flush=True)  # Print each chunk as it arrives

    return full_response
def fileImageGatherer(args):
    image_paths = []
    for i in range(70):
        file_path = args.filePath + "\\test" + str(args.startingNum+i) + "\\data.json"
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for x in range(5):
                    key = str(x+1)
                    key1 = str(x)
                    if key in data and key1 in data and "Path" in data[key] and (x+1)%2==0:
                        img_paths = [str(data[key]["Path"]),str(data[key1]["Path"])]
                        image = concatenate_images(img_paths)
                        image_paths.append(image)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Invalid JSON in file: {file_path}")
    return image_paths

if __name__ == "__main__":
    args = get_args()
    paths = fileImageGatherer(args)
    result = analyze_images(args.api,args.description,paths)
    print(result)

