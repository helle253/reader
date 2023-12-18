import re
from typing import Iterable

from nltk.tokenize import sent_tokenize

def to_sentences(text) -> Iterable[str]:
  return sent_tokenize(text)

def to_paragraphs(text) -> Iterable[str]:
  return [substr for substr in re.split(r'\n{1,}', text) if substr]

def chunk_paragraph(text) -> Iterable[str]:
  max_length = 2000
  if len(text) < max_length:
    yield text
    return

  sentences = to_sentences(text)

  chunk = ''
  for sentence in sentences:
    if len(chunk) + len(sentence) > max_length:
      yield chunk
      chunk = ''
    chunk += f' {sentence}'

def chunk_text_selection(text) -> Iterable[str]:
  paragraphs = to_paragraphs(text)
  for paragraph in paragraphs:
    for chunk in chunk_paragraph(paragraph):
      yield chunk
