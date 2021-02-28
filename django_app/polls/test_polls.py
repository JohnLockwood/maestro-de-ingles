"""using pytest rather than Django tests
   See https://pytest-django.readthedocs.io/en/latest/tutorial.html for how we set this up.
"""
from datetime import datetime, timedelta, timezone

import pytest
from django.urls import reverse
from django.test import Client

from polls.models import Question


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = datetime.now(timezone.utc) + timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

@pytest.mark.django_db
class TestPollsView:


    # See https://pytest-django.readthedocs.io/en/latest/database.html
    # At one point I thought --create-db was needed, but it's not.
    @pytest.mark.django_db
    def test_we_start_with_no_questions(self):
        client = Client()
        response = client.get(reverse('polls:index'))
        assert response.status_code == 200
        assert "No polls are available." in str(response.content)
        assert len(response.context['latest_question_list']) == 0

    def test_past_question_on_page(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        client = Client()
        create_question(question_text="Past question.", days=-30)
        response = client.get(reverse('polls:index'))
        questions = [q.question_text for q in response.context['latest_question_list']]
        assert "Past question." in questions


    def test_future_question_not_on_page(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        client = Client()
        create_question(question_text="Future question.", days=30)
        response = client.get(reverse('polls:index'))
        questions = [q.question_text for q in response.context['latest_question_list']]
        assert "Future question." not in questions


class TestPollModel:

    def test_published_recently_false_for_future_question(self):
        time = datetime.utcnow() + timedelta(days=30)
        future_question = Question(pub_date=time)
        assert not future_question.was_published_recently()

    def test_published_recently_false_for_old_question(self):
        time = datetime.utcnow() - timedelta(hours=-25)
        old = Question(pub_date=time)
        assert not old.was_published_recently()

    def test_published_recently_true_for_recent_questions(self):
        time = datetime.utcnow() + timedelta(hours=-23)
        recent = Question(pub_date=time)
        assert recent.was_published_recently()

    def test_question_has_default_pub_date(self):
        now = datetime.utcnow()
        question = Question()
        abs(now - question.pub_date
            ) < timedelta(seconds=1)