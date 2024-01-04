import re
from typing import Iterable

def process_text_selection(text) -> Iterable[str]:
  return to_paragraphs(text)


def to_paragraphs(text) -> Iterable[str]:
  return [substr for substr in re.split(r'\n{1,}', text) if substr]
