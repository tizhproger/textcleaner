import pytest
from textcleaner import TextCleaner

@pytest.mark.parametrize("text,expected", [
    ("https://example.com", "[LINK]"),
    ("me@mail.com", "[EMAIL]"),
    ("Привет!", "Привет!"),
    ("!!!!!!", None),
    ("123456", None),
    ("   ", None),
    ("Just a link: https://example.com", "Just a link: [LINK]"),
])
def test_cleaner(text, expected):
    cleaner = TextCleaner(strict=True, min_length=5, strip_only_tokens=False)
    result = cleaner.clean(text)
    if expected is None:
        assert result is None
    else:
        assert expected == result
