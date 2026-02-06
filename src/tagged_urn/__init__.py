"""Tagged URN - Flat tag-based identifier system

This package provides the fundamental tagged URN system with flat tag-based
naming, wildcard support, and specificity comparison.
"""

from .tagged_urn import (
    TaggedUrn,
    TaggedUrnBuilder,
    TaggedUrnError,
    EmptyError,
    MissingPrefixError,
    EmptyPrefixError,
    InvalidCharacterError,
    EmptyTagComponentError,
    UnterminatedQuoteError,
    InvalidEscapeSequenceError,
    DuplicateKeyError,
    WhitespaceInInputError,
    PrefixMismatchError,
)

__version__ = "0.14.3800"

__all__ = [
    "TaggedUrn",
    "TaggedUrnBuilder",
    "TaggedUrnError",
    "EmptyError",
    "MissingPrefixError",
    "EmptyPrefixError",
    "InvalidCharacterError",
    "EmptyTagComponentError",
    "UnterminatedQuoteError",
    "InvalidEscapeSequenceError",
    "DuplicateKeyError",
    "WhitespaceInInputError",
    "PrefixMismatchError",
]
