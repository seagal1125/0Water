import re
import os
import glob

def clean_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove timestamps and indices
    # Pattern: Digit(s) newline Time --> Time newline
    pattern = r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n'
    content = re.sub(pattern, '', content)
    # Remove extra newlines
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    return '\n'.join(lines)

transcript_dir = '/Users/david/Library/Mobile Documents/com~apple~CloudDocs/0漏水/Transcript'
output_file = '/Users/david/Library/Mobile Documents/com~apple~CloudDocs/0漏水/cleaned_transcripts.txt'

srt_files = sorted(glob.glob(os.path.join(transcript_dir, '*.srt')))

with open(output_file, 'w', encoding='utf-8') as outfile:
    for srt_file in srt_files:
        filename = os.path.basename(srt_file)
        cleaned_text = clean_srt(srt_file)
        outfile.write(f"### File: {filename}\n\n")
        outfile.write(cleaned_text + "\n\n")

print(f"Processed {len(srt_files)} files. Output saved to {output_file}")
