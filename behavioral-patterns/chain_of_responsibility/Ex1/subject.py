from dataclasses import dataclass

from .subject_type import SubjectType


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
    def subject_type(self) -> str:
        return SubjectType.handler(self)

    def is_disciplina_assincrona_da_graduacao_presencial(self) -> bool:
        return self.course_id in (128, 2458)

    def is_disciplina_semipresencial(self) -> bool:
        return self.subject_is_hybrid

    def is_microfundamento(self) -> bool:
        return self.subject_name.startswith('Microfundamento: ')

    def is_projeto(self) -> bool:
        return self.subject_name.startswith('Projeto: ')

    def is_grupos_de_estudos(self) -> bool:
        return self.subject_name.startswith('Grupos de Estudos')

    def is_competencias_comportamentais(self) -> bool:
        return self.subject_name.startswith('Competências Comportamentais: ')

    def is_desafios_contemporaneos(self) -> bool:
        return self.subject_name.startswith('Desafios Contemporâneos: ')
