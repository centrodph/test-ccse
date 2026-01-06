import os
import json
import argparse
from faster_whisper import WhisperModel
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser(description='Transcribe audio files to JSON.')
    parser.add_argument('--limit', type=int, help='Limit the number of files to process (for testing)')
    args = parser.parse_args()

    audio_dir = 'web-app/public/audios'
    output_file = 'scripts/audio_transcriptions.json'
    model_size = "base"

    print(f"Loading model: {model_size}...")
    # Run on CPU with INT8 quantization by default regarding macs
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    files = []
    for f in os.listdir(audio_dir):
        if f.endswith('.mp3'):
            files.append(f)
    
    # Sort files by numerical ID
    files.sort(key=lambda x: int(os.path.splitext(x)[0]))

    if args.limit:
        files = files[:args.limit]
        print(f"Limiting to first {args.limit} files.")

    results = []

    print(f"Starting transcription of {len(files)} files...")
    for filename in tqdm(files):
        file_path = os.path.join(audio_dir, filename)
        file_id = os.path.splitext(filename)[0]
        
        try:
            segments, info = model.transcribe(file_path, beam_size=5)
            
            # segments is a generator so we iterate over it
            text = " ".join([segment.text for segment in segments]).strip()
            
            results.append({
                "id": file_id,
                "filename": filename,
                "text": text
            })
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            results.append({
                "id": file_id,
                "filename": filename,
                "text": "",
                "error": str(e)
            })

    # Regex pattern to find the answer part
    # We look for "La respuesta correcta es" or similar variations, case insensitive
    import re
    pattern = re.compile(r"(?i)(.*?)(\.?,?\s*(?:La\s+)?(?:respuesta|opción)\s+correcta\s+es.*)", re.DOTALL)

    final_results = []
    for entry in results:
        text = entry.get('text', '')
        if not text:
             # handle error case or empty text
            entry['question'] = ""
            entry['anwser'] = ""
            if 'text' in entry:
                del entry['text']
            final_results.append(entry)
            continue
            
        match = pattern.match(text)
        if match:
            question_part = match.group(1).strip()
            answer_part = match.group(2).strip()
            if answer_part.startswith('.') or answer_part.startswith(','):
                answer_part = answer_part[1:].strip()
            entry['question'] = question_part
            entry['anwser'] = answer_part
            del entry['text']
        else:
            entry['question'] = text
            entry['anwser'] = ""
            del entry['text']
        final_results.append(entry)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_results, f, indent=2, ensure_ascii=False)

    print(f"Transcription complete. Saved to {output_file}")

if __name__ == "__main__":
    main()
