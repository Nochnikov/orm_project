from CRUD_CREATE import add_grade, add_student
from project_school.database import get_session


session = get_session()

student = add_student(
    session=session, 
    fname='Дуйсенов',
    sname='Нурдаулет',
    age=15,
    group='11B',
    teacher_id=1
)


session.close()