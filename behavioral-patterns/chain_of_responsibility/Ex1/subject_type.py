from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:   # pragma: no cover
    from .subject import Subject


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, subject: Subject) -> str:
        pass


class SubjectTypeHandler(Handler):
    _next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, subject: Subject) -> str:
        if self._next_handler:
            return self._next_handler.handle(subject)
        return 'Bacharelado | Licenciatura'   # Default Subject Type


class DisciplinaSemipresencialHandler(SubjectTypeHandler):
    def handle(self, subject: Subject) -> str:
        if subject.is_disciplina_semipresencial():
            return 'Disciplina Semipresencial'
        return super().handle(subject)


class DisciplinaAssincronaDaGraduacaoPresencialHandler(SubjectTypeHandler):
    def handle(self, subject: Subject) -> str:
        if subject.is_disciplina_assincrona_da_graduacao_presencial():
            return 'Disciplina Assíncrona da Graduação Presencial'
        return super().handle(subject)


class MicrofundamentoHandler(SubjectTypeHandler):
    def handle(self, subject: Subject) -> str:
        if subject.is_microfundamento():
            return 'Microfundamento'
        return super().handle(subject)


class ProjetoHandler(SubjectTypeHandler):
    def handle(self, subject: Subject) -> str:
        if subject.is_projeto():
            return 'Projeto'
        return super().handle(subject)


class GruposDeEstudosHandler(SubjectTypeHandler):
    def handle(self, subject: Subject) -> str:
        if subject.is_grupos_de_estudos():
            return 'Grupos de Estudos'
        return super().handle(subject)


class CompetenciasComportamentaisHandler(SubjectTypeHandler):
    def handle(self, subject: Subject) -> str:
        if subject.is_competencias_comportamentais():
            return 'Competências Comportamentais'
        return super().handle(subject)


class DesafiosContemporaneosHandler(SubjectTypeHandler):
    def handle(self, subject: Subject) -> str:
        if subject.is_desafios_contemporaneos():
            return 'Desafios Contemporâneos'
        return super().handle(subject)


class SubjectType:
    @staticmethod
    def handler(subject: Subject) -> str:
        disciplina_semipresencial = DisciplinaSemipresencialHandler()
        (
            disciplina_semipresencial.set_next(DisciplinaAssincronaDaGraduacaoPresencialHandler())
            .set_next(MicrofundamentoHandler())
            .set_next(ProjetoHandler())
            .set_next(GruposDeEstudosHandler())
            .set_next(CompetenciasComportamentaisHandler())
            .set_next(DesafiosContemporaneosHandler())
        )
        return disciplina_semipresencial.handle(subject)
