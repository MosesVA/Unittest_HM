import unittest
from classes import Teacher, DisciplineTeacher


class TestTeacher(unittest.TestCase):
    teacher = Teacher('test_name test_surname', 'test_education', 'test_experience')

    def test01_init(self):
        self.assertEqual(len(Teacher.teachers_list), 2)

    def test02_get_name(self):
        self.assertEqual(self.teacher.get_name(), 'test_name test_surname')

    def test03_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'test_education')

    def test04_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 'test_experience')

    def test05_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), 'test_name test_surname, образование test_education, '
                                                          'опыт работы test_experience лет.')

    def test06_add_mark(self):
        self.assertEqual(self.teacher.add_mark('test_student_name', 'test_value'), 'test_name '
                                                                                   'test_surname поставил оценку '
                                                                                   'test_value студенту '
                                                                                   'test_student_name.')

    def test07_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('test_student_name', 'test_value'), 'test_name '
                                                                                      'test_surname удалил оценку '
                                                                                      'test_value студенту '
                                                                                      'test_student_name.')

    def test08_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('test_student_class'), 'test_name test_surname провел '
                                                                                 'консультацию в классе '
                                                                                 'test_student_class.')

    def test09_set_experience(self):
        self.assertEqual(self.teacher.set_experience('test_new_experience'), 'test_new_experience')

    def test10_fire_teacher(self):
        self.assertEqual(Teacher.fire_teacher(self.teacher), 'Учитель уволен')
        self.assertEqual(Teacher.fire_teacher(self.teacher), 'Учитель уже был уволен')


class TestDisciplineTeacher(unittest.TestCase):
    dis_teacher = DisciplineTeacher('test_name test_surname', 'test_education', 'test_experience',
                                    'test_discipline', 'test_job_title')

    def test_get_discipline(self):
        self.assertEqual(self.dis_teacher.get_discipline(), 'test_discipline')

    def test_get_job_title(self):
        self.assertEqual(self.dis_teacher.get_job_title(), 'test_job_title')

    def test_get_teacher_data(self):
        self.assertEqual(self.dis_teacher.get_teacher_data(), 'test_name test_surname, образование test_education, '
                                                              'опыт работы test_experience лет. Предмет test_discipline'
                                                              ', Должность test_job_title.')

    def test_add_mark(self):
        self.assertEqual(self.dis_teacher.add_mark('test_student_name', 'test_value'), 'test_name '
                                                                                       'test_surname поставил оценку '
                                                                                       'test_value студенту '
                                                                                       'test_student_name. '
                                                                                       'Предмет: test_discipline.')

    def test_remove_mark(self):
        self.assertEqual(self.dis_teacher.remove_mark('test_student_name', 'test_value'),
                         'test_name test_surname удалил оценку test_value студенту test_student_name.  '
                         'Предмет: test_discipline.')

    def test_give_a_consultation(self):
        self.assertEqual(self.dis_teacher.give_a_consultation('test_student_class'), 'test_name test_surname '
                                                                                     'провел консультацию в классе '
                                                                                     'test_student_class. '
                                                                                     'По предмету test_discipline '
                                                                                     'как test_job_title.')
