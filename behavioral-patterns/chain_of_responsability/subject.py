from dataclasses import dataclass

from .subject_segment import (
    CompetenciasComportamentaisHandler,
    DesafiosContemporaneosHandler,
    DisciplinaAssincronaDaGraduacaoPresencialHandler,
    DisciplinaSemipresencialHandler,
    GruposDeEstudosHandler,
    MicrofundamentoHandler,
    ProjetoHandler,
    SegmentHandler,
)


@dataclass
class Subject:
    subject_id: int
    subject_name: str
    subject_is_hybrid: bool
    shift_id: int
    shift_name: str
    offer_id: int
    offer_year: int
    offer_semester: int
    offer_term: int
    offer_status: str
    offer_group: int
    offer_team: int
    course_id: int
    lms_course_id: str
    synced_at_lms: bool

    @property
    def segment(self) -> str:
        segment_handlers: list[SegmentHandler] = [
            DisciplinaSemipresencialHandler(),
            DisciplinaAssincronaDaGraduacaoPresencialHandler(),
            MicrofundamentoHandler(),
            ProjetoHandler(),
            GruposDeEstudosHandler(),
            CompetenciasComportamentaisHandler(),
            DesafiosContemporaneosHandler(),
        ]

        for segment_handler in segment_handlers:
            segment = segment_handler.handle(self)
            if segment is not None:
                return segment

        return 'Bacharelado | Licenciatura'
