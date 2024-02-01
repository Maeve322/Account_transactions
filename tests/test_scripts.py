import pytest
from src.scripts.insert import load_json, get_data, get_from, five_transactions, date_correct, sort_data, get_to, get_amount


@pytest.fixture
def transactions():
    """"Для проверки фейковых транзакций"""
    return load_json('test_json.json')

def test_load_json(transactions):
    assert len(transactions) == 2
    assert transactions[0]['id'] == 1
    assert transactions[1]['state'] == 'CANCELED'

def test_get_data(transactions):
    assert len(get_data(transactions)) == 1
def test_sort_data():
    pass

def test_five_transactions():
    assert five_transactions(["a","b","c","d","e","x"]) == ["a","b","c","d","e"]

def test_date_correct():
    assert date_correct("2020-01-24T10:50:58.294041") == '24-01-2020'

def test_get_from(transactions):
   item = transactions[0]
   assert get_from(item) == 'Maestro 1116 83** **** 5199'

   item = transactions[1]
   assert get_from(item) == 'Maestro 1116 83** **** 2222'

def test_get_to(transactions):
    item = transactions[1]
    assert get_to(item) == '-> Счет **5111'

def test_get_amount(transactions):
    item = transactions[0]
    assert get_amount(item) == '100 руб.'
