from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Grade {self.subject} - {self.grade}>'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    grades = db.relationship('Grade', backref='student', lazy=True)

    def __repr__(self):
        return f'{self.id}. Student {self.name} {self.last_name}. Age: {self.age}. Group: {self.group}. Faculty ID: {self.faculty_id}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    students = db.relationship('Student', backref=db.backref('faculty'), lazy=True)

    def __repr__(self):
        return f'{self.name}'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    number_of_copies = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return (f'<Book "{self.title}" (author id: {self.author_id}). '
                f'Year of publishing: {self.year}. Number of copies: {self.number_of_copies}.')


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.name} {self.last_name}>'
