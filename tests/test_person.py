import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from person import Person

def test_person():
    person = Person(720, "Texas")
    assert person.state == "Texas"
    assert person.credit_score == 720

