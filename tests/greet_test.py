import pytest

from niclasProject.niclasProject import greet

def test_greet_returns_Hi_Niclas_given_Niclas():
    assert greet("Niclas") == "Hi, Niclas."