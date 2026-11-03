"""Tests for is_valid_username, count_words, truncate  (function-style tests)."""
import pytest

from qe_utils import count_words, is_valid_username, truncate


# ---- WORKED EXAMPLE (already done for you; read it, then copy the pattern) ----
@pytest.mark.smoke
def test_username_valid_simple_name():
    # Arrange
    name = "qe_trainee"
    # Act
    result = is_valid_username(name)
    # Assert
    assert result is True


# ---- TODO tests: replace each `pytest.fail(...)` line with real test code ----
@pytest.mark.boundary
@pytest.mark.regression
def test_username_too_short_is_rejected():

    name = "ab"

    result = is_valid_username(name)

    assert result is False

@pytest.mark.boundary
@pytest.mark.regression
def test_username_exactly_3_chars_is_accepted():

    name = "abc"

    result = is_valid_username(name)

    assert result is True

@pytest.mark.boundary
@pytest.mark.regression
def test_username_16_chars_is_rejected():

    name = "abcabcabcabcabca"

    result = is_valid_username(name)

    assert result is False

@pytest.mark.regression
def test_username_starting_with_digit_is_rejected():

    name = "1abc"

    result = is_valid_username(name)

    assert result is False

@pytest.mark.regression
def test_username_with_space_or_symbol_is_rejected():

    name1 = "bad name"
    name2 = "bad-name"

    result1 = is_valid_username(name1)
    result2 = is_valid_username(name2)

    assert result1 is False
    assert result2 is False


def test_username_non_string_raises_type_error():

    name = 12345

    with pytest.raises(TypeError, match="username must be a string"):
        result = is_valid_username(name)

@pytest.mark.smoke
def test_count_words_simple_sentence():

    words = "quality is everyone's job"

    result = count_words(words)

    assert result == 4

@pytest.mark.boundary
@pytest.mark.regression
def test_count_words_empty_string_is_zero():

    words = ""

    result = count_words(words)

    assert result == 0


def test_count_words_non_string_raises_type_error():

    words = None

    with pytest.raises(TypeError):
        result = count_words(words)

@pytest.mark.smoke
def test_truncate_short_text_is_unchanged():

    word = "hello"
    length = 10

    result = truncate(word, length)

    assert result == word


def test_truncate_long_text_ends_with_ellipsis_and_has_max_len():

    word = "abcdefghij"
    length = 8

    result = truncate(word, length)

    assert result == "abcde..."

@pytest.mark.xfail(reason="Known bug", strict=True)
@pytest.mark.boundary
@pytest.mark.regression
def test_truncate_text_exactly_max_len_is_unchanged():
    # TODO (Task 6): by the docstring, text that fits exactly must NOT be cut.
    # Write the test according to the docstring. It will FAIL - why?
    # Then mark it as a known bug:  @pytest.mark.xfail(reason="...", strict=True)
    # Markers: boundary, regression
    word = "Bonjour"
    length = 7

    result = truncate(word, length)

    assert result == "Bonjour"

def test_truncate_max_len_below_3_raises_value_error():
    # TODO (Task 4): max_len=2 -> ValueError, check the message with match=
    word = "Blabber"
    length = 2

    with pytest.raises(ValueError, match="max_len must be at least 3"):
        result = truncate(word, length)