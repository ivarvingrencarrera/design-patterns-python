from unittest import TestCase

from .subject import Subject


class TestSubject(TestCase):
    def create_subject(self, **kwargs: object) -> Subject:
        subject = {
            'subject_id': 54572,
            'subject_name': 'Empreendedorismo e Negócios',
            'subject_is_hybrid': False,
            'shift_id': 5,
            'shift_name': 'Virtual',
            'offer_id': 4510104,
            'offer_year': 2023,
            'offer_semester': 2,
            'offer_term': 1,
            'offer_status': 'active',
            'offer_group': 1,
            'offer_team': 4,
            'course_id': 2412,
            'lms_course_id': 'SGA_53255_2412_2023_2_4510104',
            'synced_at_lms': True,
        } | kwargs
        return Subject(**subject)

    def test_semipresencial(self) -> None:
        subject = self.create_subject(subject_is_hybrid=True)
        self.assertEqual(subject.subject_type, 'Disciplina Semipresencial')

    def test_assincrona(self) -> None:
        subject = self.create_subject(course_id=128)
        self.assertEqual(subject.subject_type, 'Disciplina Assíncrona da Graduação Presencial')

    def test_microfundamento(self) -> None:
        subject = self.create_subject(subject_name='Microfundamento: Empreendedorismo e Negócios')
        self.assertEqual(subject.subject_type, 'Microfundamento')

    def test_projeto(self) -> None:
        subject = self.create_subject(subject_name='Projeto: Empreendedorismo e Negócios')
        self.assertEqual(subject.subject_type, 'Projeto')

    def test_grupos_de_estudos(self) -> None:
        subject = self.create_subject(subject_name='Grupos de Estudos: Empreendedorismo e Negócios')
        self.assertEqual(subject.subject_type, 'Grupos de Estudos')

    def test_competencias_comportamentais(self) -> None:
        subject = self.create_subject(
            subject_name='Competências Comportamentais: Empreendedorismo e Negócios'
        )
        self.assertEqual(subject.subject_type, 'Competências Comportamentais')

    def test_desafios_contemporaneos(self) -> None:
        subject = self.create_subject(
            subject_name='Desafios Contemporâneos: Empreendedorismo e Negócios'
        )
        self.assertEqual(subject.subject_type, 'Desafios Contemporâneos')

    def test_bacharelado_licenciatura(self) -> None:
        subject = self.create_subject()
        self.assertEqual(subject.subject_type, 'Bacharelado | Licenciatura')
