# Textcleaner

A lightweight multilingual (currently EN and RU languages supported) text cleaning utility for NLP tasks. Supports tagging, normalization, emoji and noise removal.

## Features

- Emoji & symbol removal
- Special character normalization
- Language-specific date detection (ru/en)
- Replacement of URLs, emails, phones, etc. with `[TAG]`
- Replacement of noise characters (unprintables, leftover spaces etc.)

## Usage

```python
from textcleaner import TextCleaner

cleaner = TextCleaner(language='multi', preserve_tokens=True)
cleaned = cleaner.clean("Text with link: https://example.com and email: me@gmail.com")
print(cleaned)
# Output: 'Text with link: [LINK] and email: [EMAIL]'
```


## Configuration

You can initialize `TextCleaner` with custom parameters:

```python
from textcleaner import TextCleaner

cleaner = TextCleaner(strict=True, min_length=8)
text = cleaner.clean("Some raw input message with a link: https://test.com")
print(text)
# Output: Some raw input message with a link: [LINK]
```
