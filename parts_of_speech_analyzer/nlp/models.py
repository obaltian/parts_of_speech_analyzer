import functools
import textwrap
import typing as tp

from django.conf import settings
from django.db import models

from .utils import detect_language, LanguageMeta
from .validators import get_language_validator


validate_text_language = get_language_validator(settings.LANGUAGE_MODELS)


# noinspection PyTypeChecker
class Text(models.Model):
    text = models.TextField(db_index=True)

    @functools.cached_property
    def language(self) -> tp.Optional[LanguageMeta]:
        return detect_language(self.text)

    def clean(self) -> None:
        validate_text_language(self.text, lang=self.language)

    def __str__(self) -> str:
        return f"Text #{self.id} ({textwrap.shorten(self.text, 15)})"


class PartOfSpeech(models.Model):
    name = models.TextField(unique=True, db_index=True)

    def __str__(self) -> models.TextField:
        return self.name


class Word(models.Model):
    word = models.TextField(db_index=True)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    part_of_speech = models.ForeignKey(PartOfSpeech, on_delete=models.CASCADE)

    class Meta:
        ordering = ["word", ]

    def __str__(self) -> models.TextField:
        return self.word
