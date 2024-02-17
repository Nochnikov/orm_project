from project_school.moduls import Teacher, Subject, Group, Student, Grade
from project_school.database import get_session
from sqlalchemy import func, desc

session = get_session()


def get_average_student_in_school():
    student_count = session.query(func.count(Student.id)).one()
    group_count = session.query(func.count(Group.name)).one()
    aver_stud = student_count[0] / group_count[0]
    return aver_stud


def top_three_students(subject_id: int):
    students = session.query(Student.first_name, Student.last_name).filter(
        Student.id == Grade.student_id and subject_id == Grade.subject_id).order_by(desc(Grade.grade)).limit(3).all()

    return students


def top_three_group():
    subquery = session.query(Subject).join(Grade).join(Group).subquery('subq')

    classes = session.query(Grade.grade, subquery.c.name).join(
        subquery,
        Grade.id == subquery.c.id
    ).order_by(desc(Grade.grade)).limit(3).all()
    return classes



