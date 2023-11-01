from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:   # pragma: no cover
    from .subject import Subject


class SegmentHandler(ABC):
    @abstractmethod
    def handle(self, subject: Subject) -> Optional[str]:
        pass


class DisciplinaSemipresencialHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        return 'Disciplina Semipresencial' if subject.subject_is_hybrid else None


class DisciplinaAssincronaDaGraduacaoPresencialHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.course_id in (128, 2458):
            return 'Disciplina Assíncrona da Graduação Presencial'
        return None


class MicrofundamentoHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Microfundamento: '):
            return 'Microfundamento'
        return None


class ProjetoHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        return 'Projeto' if subject.subject_name.startswith('Projeto: ') else None


class GruposDeEstudosHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Grupos de Estudos'):
            return 'Grupos de Estudos'
        return None


class CompetenciasComportamentaisHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Competências Comportamentais: '):
            return 'Competências Comportamentais'
        return None


class DesafiosContemporaneosHandler(SegmentHandler):
    def handle(self, subject: Subject) -> Optional[str]:
        if subject.subject_name.startswith('Desafios Contemporâneos: '):
            return 'Desafios Contemporâneos'
        return None
