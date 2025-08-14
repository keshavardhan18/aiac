import string

def clean_text(text, stop_words):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    text = text.lower()
    # Remove stop words
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Example usage
stop_words = {'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'in', 'to', 'of'}
text = "The quick brown fox jumps over the lazy dog, and runs away!"
result = clean_text(text, stop_words)
print(result)