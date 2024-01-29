import openai
openai.api_key = "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"

openai.fine_tuning.jobs.create(
  training_file="file-abc123", 
  model="gpt-3.5-turbo"
)

def fine_tune():
    response = openai.chat.completions.create(
        model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
        messages=[{"role": "system", "content": "You are a helpful assistant."}]
        )
    return response.choices[0].message.content.strip()
