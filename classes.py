class Teacher:
    teachers_list = []

    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience
        self.teachers_list.append(self)

    def get_name(self):
        return self._name

    def get_education(self):
        return self._education

    def get_experience(self):
        return self._experience

    def set_experience(self, new_experience):
        self._experience = new_experience
        return self._experience

    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт работы {self._experience} лет."

    def add_mark(self, student_name, value):
        return f"{self._name} поставил оценку {value} студенту {student_name}."

    def remove_mark(self, student_name, value):
        return f"{self._name} удалил оценку {value} студенту {student_name}."

    def give_a_consultation(self, student_class):
        return f"{self._name} провел консультацию в классе {student_class}."

    @staticmethod
    def fire_teacher(self):
        if self in self.teachers_list:
            self.teachers_list.remove(self)
            return 'Учитель уволен'
        else:
            return 'Учитель уже был уволен'


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self._job_title = job_title

    def get_discipline(self):
        return self._discipline

    def get_job_title(self):
        return self._job_title

    def get_teacher_data(self):
        return (f"{self._name}, образование {self._education}, опыт работы {self._experience} лет. "
                f"Предмет {self._discipline}, Должность {self._job_title}.")

    def add_mark(self, student_name, value):
        return f"{self._name} поставил оценку {value} студенту {student_name}. Предмет: {self._discipline}."

    def remove_mark(self, student_name, value):
        return f"{self._name} удалил оценку {value} студенту {student_name}.  Предмет: {self._discipline}."

    def give_a_consultation(self, student_class):
        return (f"{self._name} провел консультацию в классе {student_class}. "
                f"По предмету {self._discipline} как {self._job_title}.")
