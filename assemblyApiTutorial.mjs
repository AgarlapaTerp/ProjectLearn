// Start by making sure the `assemblyai` package is installed.
// If not, you can install it by running the following command:
// npm install assemblyai

import { AssemblyAI } from 'assemblyai';

const client = new AssemblyAI({
  apiKey: '4239ecd4544249b7a7a99a477ed6521a',
});

const FILE_URL = "https://youtu.be/wZAjVQWbMlE?si=Nf5BSwMIWcjkPszk";

// You can also transcribe a local file by passing in a file path
// const FILE_URL = './path/to/file.mp3';

// Request parameters 
const data = {
  audio_url: FILE_URL
}

const run = async () => {
  console.log("waiting");
  const transcript = await client.transcripts.create(data);
  console.log(transcript.text);
};

run();
