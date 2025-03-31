# Textcleaner

A lightweight multilingual (currently EN and RU languages supported) text cleaning utility for NLP tasks. Supports tagging, normalization, emoji and noise removal.

## Features

- Emoji & symbol removal
- Special character normalization
- Language-specific date detection (RU/EN)
- Replacement of URLs, emails, phones, etc. with `[TAG]`
- Replacement of noise characters (unprintables, leftover spaces etc.)
- Removing: repeated strings, strings with only digits, symbols only, tags only

## Parameters

The TextCleaner class supports flexible configuration:

```python
TextCleaner(
    preserve_tokens=True,
    strip_only_tokens=True,
    language='multi',
    strict=False,
    min_length=5
)
```

Parameter description:

- `preserve_tokens` (**bool**, default **True**)
Enables entity tagging such as `[LINK]`, `[EMAIL]`, `[DATE]`.

- `strip_only_tokens` (**bool**, default **True**)
If the cleaned message consists only of tokens (e.g., `[LINK]` `[EMAIL]`), it will be discarded.

- `language` (**str**, default **'multi'**)
Language of the text (**'ru'**, **'en'**, **'multi'**), affects date recognition.

- `strict` (**bool**, default **False**)
Enables stricter cleaning (removes texts with no letters, only numbers, repeating symbols, etc.).

- `min_length` (**int**, default **5**)
Minimum allowed length of the cleaned message.

## Usage

```python
from textcleaner import TextCleaner

cleaner = TextCleaner(language='multi', preserve_tokens=True)
cleaned = cleaner.clean("Text with link: https://example.com and email: me@gmail.com")
print(cleaned)
# Output: 'Text with link: [LINK] and email: [EMAIL]'
```

If given the text doesn't meet the required criteria of filtering, method will return `None`


## Configuration

You can initialize `TextCleaner` with custom parameters:

```python
from textcleaner import TextCleaner

cleaner = TextCleaner(strict=True, min_length=8)
text = cleaner.clean("Some raw input message with a link: https://test.com")
print(text)
# Output: Some raw input message with a link: [LINK]
```
