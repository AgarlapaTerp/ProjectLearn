import openai
openai.api_key = "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"
response = openai.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Can you explain what is going on in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://u-mercari-images.mercdn.net/photos/m20855214749_1.jpg?width=1024&height=1024&format=pjpg&auto=webp&fit=crop&_=1703609819",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
