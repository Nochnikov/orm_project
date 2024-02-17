from project_school.moduls import Teacher, Subject, Student, Grade, Group
from sqlalchemy.orm import Session


def add_teacher(session: Session,
                fname: str,
                sname: str,
                age: int):
    new_teacher = Teacher(
        first_name=fname,
        last_name=sname,
        age=age
    )
    session.add(new_teacher)
    session.commit()
    return new_teacher


def add_subject(session: Session,
                sub_name: str,
                teacher_id: int):
    new_subject = Subject(
        Subject_name=sub_name,
        teacher_id=teacher_id
    )
    session.add(new_subject)
    session.commit()
    return new_subject


def add_group(session: Session,
              gname: str,
              teacher_id: int,
              room_id: int):
    new_group = Group(
        name=gname,
        lead_teacher_id=teacher_id,
        room_id=room_id
    )
    session.add(new_group)
    session.commit()
    return new_group


def add_student(
        session: Session,
        fname: str,
        sname: str,
        age: int,
        group: str,
        teacher_id: int
):
    new_student = Student(
        first_name=fname,
        last_name=sname,
        age=age,
        group=group,
        lead_teacher_id=teacher_id
    )
    session.add(new_student)
    session.commit()
    return new_student


def add_grade(
        session: Session,
        grade: int,
        student_id: int,
        subject_id: int,
        teacher_id: int,
):
    new_grade = Grade(
        grade=grade,
        student_id=student_id,
        subject_id=subject_id,
        teacher_id=teacher_id
    )

    session.add(new_grade)
    session.commit()
    return new_grade