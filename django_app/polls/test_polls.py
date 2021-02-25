"""using pytest rather than Django tests
   See https://pytest-django.readthedocs.io/en/latest/tutorial.html for how we set this up.
"""

from datetime import datetime, timedelta
from polls.models import Question


def test_pytest_configuration():
    assert True


def test_published_recently_false_for_future_question():
    time = datetime.now() + timedelta(days=30)
    future_question = Question(pub_date=time)
    assert not future_question.was_published_recently()
