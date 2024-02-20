import json
from openai import OpenAI

client = OpenAI()

default_prompt = """
Assuming you are a store assistant please analyze the item in the picture.
 Only return the data in a json with the keys shape, dominant_colors, style, description, material, suggested_title, theme. 
 Please restrict the product description to 100 words. 
 For theme please return any special characteristics like nature, geometric, abstract etc. 
"""


def get_openai_opinion(url: str, image_capture_prompt=default_prompt) -> dict:
    print(f'Sending request for {url}')
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": image_capture_prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": url,
                        },
                    },
                ],
            }
        ],
        max_tokens=400,
    )
    print('Received response')
    json_resp = response.choices[0].message.content
    tokens_used = response
    try:
        print(f'Processing content {json_resp}')
        json_resp = json_resp.replace('```json', '').replace('```', '')
        data = json.loads(json_resp)
        print(f'Response obtained: {data}')
        return data
    except Exception as e:
        print('Error calling openai', e)
        return dict()
