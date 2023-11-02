from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:   # pragma: no cover
    from .subject import Subject


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, subject: Subject) -> Optional[str]:
        pass


class SegmentHandler(Handler):
    _next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, subject: Subject) -> Optional[str]:
        return self._next_handler.handle(subject) if self._next_handler else None


class DisciplinaSemipresencialHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        return 'Disciplina Semipresencial' if subject.subject_is_hybrid else super().handle(subject)


class DisciplinaAssincronaDaGraduacaoPresencialHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.course_id in (128, 2458):
            return 'Disciplina Assíncrona da Graduação Presencial'
        return super().handle(subject)


class MicrofundamentoHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Microfundamento: '):
            return 'Microfundamento'
        return super().handle(subject)


class ProjetoHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Projeto: '):
            return 'Projeto'
        return super().handle(subject)


class GruposDeEstudosHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Grupos de Estudos'):
            return 'Grupos de Estudos'
        return super().handle(subject)


class CompetenciasComportamentaisHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Competências Comportamentais: '):
            return 'Competências Comportamentais'
        return super().handle(subject)


class DesafiosContemporaneosHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Desafios Contemporâneos: '):
            return 'Desafios Contemporâneos'
        return super().handle(subject)


class Segmenter:
    def __init__(self) -> None:
        self.chain = self.build_chain_of_responsibility()

    def handle(self, subject: Subject) -> str:
        return self.chain.handle(subject) or 'Bacharelado | Licenciatura'

    def build_chain_of_responsibility(self) -> SegmentHandler:
        chain_of_responsibility = DisciplinaSemipresencialHandler()
        chain_of_responsibility.set_next(
            DisciplinaAssincronaDaGraduacaoPresencialHandler()
        ).set_next(MicrofundamentoHandler()).set_next(ProjetoHandler()).set_next(
            GruposDeEstudosHandler()
        ).set_next(
            CompetenciasComportamentaisHandler()
        ).set_next(
            DesafiosContemporaneosHandler()
        )
        return chain_of_responsibility
