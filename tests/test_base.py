"""
Unit tests for shared base model utilities.
"""

from datetime import datetime, timezone

from database.models._base import Base, utcnow


def test_utcnow_returns_datetime():
    result = utcnow()

    assert isinstance(result, datetime)


def test_utcnow_returns_timezone_aware_datetime():
    result = utcnow()

    assert result.tzinfo is not None
    assert result.utcoffset() is not None


def test_utcnow_returns_utc_datetime():
    result = utcnow()

    assert result.tzinfo == timezone.utc


def test_utcnow_returns_current_time():
    before = datetime.now(timezone.utc)
    result = utcnow()
    after = datetime.now(timezone.utc)

    assert before <= result <= after


def test_base_is_available():
    assert Base is not None
