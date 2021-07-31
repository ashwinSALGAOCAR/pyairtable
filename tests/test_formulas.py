import pytest
from airtable.formulas import (
    AND,
    EQUAL,
    FIELD,
    STR_VALUE,
    match,
)


def test_equal():
    assert EQUAL("A", "B") == "A=B"


def test_field():
    assert FIELD("Name") == "{Name}"


def test_and():
    assert AND("A", "B", "C") == "AND(A,B,C)"


def test_string_value():
    assert STR_VALUE("A") == "'A'"


def test_combination():
    formula = AND(
        EQUAL(FIELD("First Name"), STR_VALUE("A")),
        EQUAL(FIELD("Last Name"), STR_VALUE("B")),
        EQUAL(FIELD("Age"), STR_VALUE(15)),
    )
    assert formula == ("AND({First Name}='A',{Last Name}='B',{Age}='15')")


@pytest.mark.parametrize(
    "dict,exprected_formula",
    [
        ({"First Name": "John"}, "{First Name}='John'"),
        ({"A": "1", "B": "2"}, "AND({A}='1',{B}='2')"),
        ({}, ""),
    ],
)
def test_match(dict, exprected_formula):
    rv = match(dict)
    assert rv == exprected_formula
