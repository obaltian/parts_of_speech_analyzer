import typing as tp

from django.utils.translation import gettext_lazy as _

from .errors import LanguageValidationError
from .utils import detect_language, get_language_by_code, LanguageMeta


def get_language_validator(allowed_langs: tp.Iterable[str],
                           ) -> tp.Callable[..., None]:
    def language_validator(value: str,
                           *,
                           lang: tp.Optional[LanguageMeta] = None,
                           ) -> None:
        if lang is None:
            lang = detect_language(value)
            if lang is None:
                raise LanguageValidationError(
                    _("Could not detect language from text")
                )
        if lang.code not in allowed_langs:
            raise LanguageValidationError(
                _("Expected text in one of the following languages: "
                  "%(allowed_langs)s. Got %(got_lang)s."
                  ),
                params={
                    "allowed_langs":
                        ", ".join(map(get_language_by_code, allowed_langs)),
                    "got_lang": lang.name,
                },
            )
    return language_validator
