import pytest
from learn.models import Vocabulary, Lesson


@pytest.mark.django_db
class TestLearnModels:

    def test_can_create_legacy_lesson_and_vocabulary(self):
        lesson = Lesson(title="Some test lesson")
        lesson.save()
        v = Vocabulary(lesson=lesson, learning="Hi", native="Hola")
        v.save()
        assert v.save is not None
        assert lesson.id is not None

    # def test_can_create_new_style_unit(self):
    #     example =