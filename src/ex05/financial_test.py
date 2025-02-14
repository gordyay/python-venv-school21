import pytest
from financial.py import get_fin_data


def test_total_revenue():
    result = get_fin_data("MSFT", "Total Revenue")
    assert isinstance(result, tuple)
    assert len(result) > 0
    assert result[0] == "Total Revenue"


def test_return_type():
    result = get_fin_data("AAPL", "Basic Average Shares")
    assert isinstance(result, tuple)


def test_invalid_ticker():
    with pytest.raises(Exception):
        get_fin_data("INVALID_TICKER", "Total Revenue")


def test_invalid_row_name():
    with pytest.raises(Exception):
        get_fin_data("MSFT", "Invalid Row Name")