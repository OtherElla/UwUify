import re

original_text = input(r'Insert text to uwuify: ')
patterns = [r'(?i)[rl]', r'(?i)\bi\b', r'(?i)\bthe\b', r'(?i)\byou\b']
count = 0
original_text = re.sub(patterns[0], r'w', original_text)
original_text = re.sub(patterns[1], r'me', original_text)
original_text = re.sub(patterns[2], r'da', original_text)
original_text = re.sub(patterns[3], r'u', original_text)
print(original_text)
