import base64
import requests
import io
import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

import requests
import base64

def inference_chat_new(chat, API_TOKEN):
    api_url = 'https://apix.ai-gaochao.cn/v1/chat/completions'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    # Extracting messages from chat history
    messages = []
    for role, content_list in chat:
        for content in content_list:
            if content["type"] == "text":
                messages.append({"role": role, "content": content["text"]})
            elif content["type"] == "image_url":
                messages.append({"role": role, "content": content["image_url"]["url"]})

    payload = {
        "model": "gpt-4o",
        "messages": messages,
        "max_tokens": 300
    }

    while True:
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            res = response.json()
            break
        except requests.exceptions.RequestException as e:
            print(f"Network Error: {e}")
            print("c")
            print(response.text)
    
    print(res)
    return res

def inference_chat(chat, API_TOKEN):    
    api_url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    data = {
        "model": "gpt-4o",
        "messages": [],
        "max_tokens": 4096,
    }

    for role, content in chat:
        data["messages"].append({"role": role, "content": content})
        print(data)
    for i in range(5):
        try:
            res = requests.post(api_url, headers=headers, json=data, timeout=180)
            res = res.json()['choices'][0]['message']['content']
        except Exception as e:
            print(e)
        #    print(res.text)
            # print("Network Error:")
        else:
            break
    
    return res


"""def inference_chat(chat, API_TOKEN):    
    api_url = 'https://apix.ai-gaochao.cn/v1/chat/completions'
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    data = {
        "model": "gpt-4",
        "messages": [],
        "max_tokens": 4096,
        "stream": True
    }

    for role, content in chat:
        data["messages"].append({"role": role, "content": content})

    try:
        with requests.post(api_url, headers=headers, json=data, stream=True, timeout=180) as res:
            res.raise_for_status()
            response_text = ''
            for line in res.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith("data: "):
                        line = line[len("data: "):]
                    if line == "[DONE]":
                        break
                    try:
                        token_data = json.loads(line)
                        response_text += token_data['choices'][0]['delta'].get('content', '')
                        print(token_data['choices'][0]['delta'].get('content', ''), end='', flush=True)
                    except json.JSONDecodeError:
                        pass
    except Exception as e:
        print(f"An error occurred: {e}")
        response_text = "Error occurred during the request."

    return response_text"""