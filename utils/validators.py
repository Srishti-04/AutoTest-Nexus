def contains_any(text, keywords):
    text = text.lower()
    return any(keyword.lower() in text for keyword in keywords)