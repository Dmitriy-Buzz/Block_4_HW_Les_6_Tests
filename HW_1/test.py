import pytest
from main import Secretery, documents, directories
secretery = Secretery('Oleg', '11111')


class TestDocs:

    @pytest.mark.parametrize("number,result", [('2207 876234', 'Василий Гупкин'), ('11-2', 'Геннадий Покемонов'),
                                               ('10006', 'Аристарх Павлов'), ('4004 201825', None)])
    def test_number_name(self, number, result):
        assert secretery.get_number_name(number) == result


    @pytest.mark.parametrize("number,result", [('2207 876234', '1'), ('11-2', '1'),
                                              ('10006', '2'), ('4004 201825', None)])
    def test_number_dir(self, number, result):
        assert secretery.get_number_dir(number) == result


    def test_all_list(self):
        assert secretery.get__all_list() == ['passport "2207 876234" "Василий Гупкин"',
                                             'invoice "11-2" "Геннадий Покемонов"',
                                             'insurance "10006" "Аристарх Павлов"']

    def test_add_doc(self):
        assert secretery.add_doc('passport', '4021 201825', 'Павел Абрамов', '3') == {'type': 'passport', 'number': '4021 201825', 'name': 'Павел Абрамов'} == documents[-1]
        assert '4021 201825' in directories['3']
        assert secretery.add_doc('passport', '4021 201825', 'Павел Абрамов', '4') == None