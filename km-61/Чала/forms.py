from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms import validators
import Workshop.application.models.db as db_models
import datetime


class SubjectForm(Form):
    Subject_name = StringField("Subject_name", [validators.DataRequired("Name is required")])

    Submit = SubmitField("Submit")

    def get_db_subject(self):
        return db_models.Subject(
            Subject_name=self.Subject_name.data
        )

    def update_db_subject(self, subject):
        subject.Subject_name = self.Subject_name.data


class AuditoriumForm(Form):
    auditorium_name = StringField("Auditorium_name", [validators.DataRequired("Name is required")])

    Submit = SubmitField("Submit")

    def get_db_auditorium(self):
        return db_models.Auditorium(
            Auditorium_name=self.Auditorium_name.data
        )

    def update_db_auditorium(self, auditorium):
        auditorium.Auditorium_name = self.Auditorium_name.data


class Auditorium_SubjectForm(Form):
    Subject = SelectField("Subject", [validators.DataRequired("Subject is required")])
    Auditorium = SelectField("Auditorium", [validators.DataRequired("Auditorium is required")])

    Submit = SubmitField("Submit")

    def get_db_auditorium_subject(self):
        return db_models.Auditorium_subject(
            SubjectId=self.Subject.data,
            AuditoriumId=self.Auditorium.data
        )

    def update_db_auditorium_subject(self, auditorium_subject):
        auditorium_subject.SubjectId = self.Subject.data
        auditorium_subject.AuditoriumId = self.Auditorium.data


class AuditoriumAdvancedSearchForm(Form):
    Auditorium_name = StringField("Auditorium_name", [validators.Optional()], default="", render_kw={"placeholder": "Auditorium_name"})
    Subject_name = SelectField("Subject", choices=[('any', "Any subject")], )

    Submit = SubmitField("Search")
