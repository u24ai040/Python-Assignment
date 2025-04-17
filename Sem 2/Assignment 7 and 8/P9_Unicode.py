# QUESTION 9

import re

def gujarati_tokenizer():
    text = input("Enter Gujarati text: ")


    patterns = {
        'url': r'https?://\S+',
        'email': r'[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}',
        'date': r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2}\b',
        'number': r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+/\d+\b',
        'social_media_handle': r'@[\w_]+',
        'punctuation': r'[.,!?;:()"-]',
        'gujarati_word': r'[\u0A80-\u0AFF]+' }

    combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns.items())

    tokens = []

    for match in re.finditer(combined_pattern, text):
        for name in patterns:
            value = match.group(name)
            if value:
                tokens.append((name, value))

    print("\nExtracted Tokens:")
    for token_type, token in tokens:
        print(f"{token_type}: {token}")

gujarati_tokenizer()
#આજનું હવામાન ખૂબ જ સરસ છે. તમે https://example.com ની મુલાકાત લો! સંપર્ક: user@example.com, અથવા @gujarati_handle પર મેસેજ કરો. તારીખ: ૨૭-૦૨-૨૦૨૫ અને કિંમત: ૧,૨૩,૪૫૬ રૂપિયા.
