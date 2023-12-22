import re
from typing import Iterable

from nltk.tokenize import sent_tokenize, word_tokenize, TreebankWordDetokenizer

def to_sentences(text) -> Iterable[str]:
  for sentence in sent_tokenize(text):
    yield from chunk_sentence(sentence)

def chunk_sentence(sentence) -> Iterable[str]:
  max_length = 500
  if len(sentence) < max_length:
    yield sentence
    return

  yield from __chunkify(word_tokenize(sentence), max_length)

def to_paragraphs(text) -> Iterable[str]:
  return [substr for substr in re.split(r'\n{1,}', text) if substr]

def chunk_paragraph(text) -> Iterable[str]:
  max_length = 2000
  if len(text) < max_length:
    yield TreebankWordDetokenizer().detokenize(list(to_sentences(text)))
    return

  yield from __chunkify(to_sentences(text), max_length)

def chunk_text_selection(text) -> Iterable[str]:
  for paragraph in to_paragraphs(text):
    for chunk in chunk_paragraph(paragraph):
      yield chunk

def __chunkify(text_tokens, max_length):
    """
    Binary search to split a list of tokens into chunks,
    where the combined length of each chunk is less than max_length.
    """
    def split_and_chunkify(tokens):
        if not tokens:
            return
        combined = TreebankWordDetokenizer().detokenize(tokens)
        if len(combined) <= max_length:
            yield combined
            return

        # Split the list in half and apply the same process to each half
        middle = len(tokens) // 2
        left_half = tokens[:middle]
        right_half = tokens[middle:]

        yield from split_and_chunkify(left_half)
        yield from split_and_chunkify(right_half)

    return split_and_chunkify(text_tokens)
