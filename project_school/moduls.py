from database import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(10))
    last_name = Column(String(10))
    age = Column(Integer, nullable=False, onupdate=True)

    subjects = relationship('Subject', cascade='all,delete', back_populates='teachers')
    rooms = relationship('Group', cascade='all,delete', back_populates='teachers')
    students = relationship('Student', cascade='all,delete', back_populates='teachers')
    grades = relationship('Grade', cascade='all,delete', back_populates='teachers')


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, nullable=False)
    Subject_name = Column(String(15), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))

    teachers = relationship('Teacher', back_populates='subjects', cascade='all,delete')
    rooms = relationship('Group', cascade='all,delete', back_populates='subjects')
    grades = relationship('Grade', cascade='all,delete', back_populates='subjects')


class Group(Base):
    __tablename__ = 'classes'
    name = Column(String(5), primary_key=True)
    lead_teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    room_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'), nullable=True, onupdate=True)

    __table_agrs__ = (UniqueConstraint("room_id", name='related_subject_room'))

    teachers = relationship('Teacher', cascade='all,delete', back_populates='rooms')
    subjects = relationship('Subject', cascade='all,delete', back_populates='rooms')
    students = relationship('Student', cascade='all,delete', back_populates='rooms')


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(10))
    last_name = Column(String(10))
    age = Column(Integer, nullable=False, onupdate=True)
    group = Column(String(5), ForeignKey('classes.name'), nullable=False, onupdate=True)
    lead_teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False, onupdate=True)

    teachers = relationship('Teacher', cascade='all,delete', back_populates='students')
    rooms = relationship('Group', cascade='all,delete', back_populates='students')
    grades = relationship('Grade', cascade='all,delete', back_populates='students')


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, nullable=False)
    grade = Column(Integer, nullable=False, onupdate=False, )
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE'))
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'), onupdate=True)

    teachers = relationship('Teacher', cascade='all,delete', back_populates='grades')
    subjects = relationship('Subject', cascade='all,delete', back_populates='grades')
    students = relationship('Student', cascade='all,delete', back_populates='grades')


Base.metadata.create_all(engine)
