# Need to create JSON object for the text 
import re
sentence_arr = []

# call to OpenAI, reference api_key
from openai import OpenAI
import openai
openai.api_key = "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"
audio_file= open("jrewhole.wav", "rb") #Read audio file and store in binary
#Call to Speech to Text API, pass in model and audio in binary
transcript_class = openai.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)


# Split the paragraph into sentences
transcript = transcript_class.text
pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
sentences = pattern.split(transcript)

for sentence in sentences:
    sentence_arr.append(sentence.strip())
print(sentence_arr)



