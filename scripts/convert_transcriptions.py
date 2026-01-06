import json
import re

def main():
    input_file = 'scripts/audio_transcriptions.json'
    output_file = 'scripts/audio_transcriptions.json'

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Regex pattern to find the answer part
    # We look for "La respuesta correcta es" or similar variations, case insensitive
    pattern = re.compile(r"(?i)(.*?)(\.?,?\s*(?:La\s+)?(?:respuesta|opción)\s+correcta\s+es.*)", re.DOTALL)

    updated_data = []
    
    for entry in data:
        original_text = entry.get('text', '')
        if not original_text:
            updated_data.append(entry)
            continue

        match = pattern.match(original_text)
        if match:
            question_part = match.group(1).strip()
            answer_part = match.group(2).strip()
            
            # Clean up leading punctuation from answer if regex caught it
            if answer_part.startswith('.') or answer_part.startswith(','):
                answer_part = answer_part[1:].strip()

            entry['question'] = question_part
            entry['anwser'] = answer_part # User requested key "anwser"
            # keeping or removing 'text'? User example showed removal.
            if 'text' in entry:
                del entry['text']
        else:
            # If pattern doesn't match, put everything in question and empty answer?
            # Or just leave as is? The user example implies a strict format.
            # Let's put everything in question and leave answer empty to avoid data loss
            entry['question'] = original_text
            entry['anwser'] = ""
            if 'text' in entry:
                del entry['text']
        
        updated_data.append(entry)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=2, ensure_ascii=False)

    print(f"Conversion complete. Processed {len(updated_data)} items.")

if __name__ == "__main__":
    main()
