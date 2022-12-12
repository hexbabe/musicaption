"""
Base code credit:
https://towardsdatascience.com/speech-recognition-with-timestamps-934ede4234b2
"""

import wave
import json

from vosk import Model, KaldiRecognizer

model_path = "vosk-model-en-us-0.22"
model = Model(model_path)

def transcribe_to_subs(wav_path):
    wav = wave.open(wav_path, "rb")
    rec = KaldiRecognizer(model, wav.getframerate())
    rec.SetWords(True)
    results = []
    # recognize speech and get raw transcription using vosk model
    while True:
        data = wav.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    # convert JSON dictionaries list into subtitle tuples list
    subs = []
    for sentence in results:
        if len(sentence) == 1:
            # sometimes there are bugs in recognition & it returns an empty dict
            # e.g. {'text': ''}
            continue
        for obj in sentence['result']:
            sub = ((obj['start'], obj['end']), obj['word'])
            subs.append(sub)  # and add it to list

    wav.close()
    with open('./subs.json', 'w') as f:
        json.dump(subs, f)
    return subs

if __name__ == '__main__':
    use_existing = input('Use existing subs.json file (y/n)? ')
    if use_existing == 'n':
        audio_file_name = input('Audio file name (exclude ext): ')
        transcribe_to_subs(f'inputs/audios/{audio_file_name}.wav')
    else:
        print('Using current subs.json')