from flask import Flask, redirect, url_for, render_template, request, flash
from models import db, Doctor, Patient
from forms import ContactForm,P_ContactForm

# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'
app.config['DEBUG'] = False

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    '''
    Home page
    '''
    return redirect(url_for('doctors'))


@app.route("/new_doctor", methods=('GET', 'POST'))
def new_doctor():
    '''
    Create new doctor
    '''
    form = ContactForm()
    if form.validate_on_submit():
        my_doctor = Doctor()
        form.populate_obj(my_doctor)
        db.session.add(my_doctor)
        try:
            db.session.commit()
            # User info
            flash('Doctor created correctly', 'success')
            return redirect(url_for('doctors'))
        except:
            db.session.rollback()
            flash('Error generating Doctor.', 'danger')

    return render_template('web/new_doctor.html', form=form)


@app.route("/edit_doctor/<id>", methods=('GET', 'POST'))
def edit_doctor(id):
    '''
    Edit doctor

    :param id: Id from doctor
    '''
    my_doctor = Doctor.query.filter_by(id=id).first()
    form = ContactForm(obj=my_doctor)
    if form.validate_on_submit():
        try:
            # Update Doctor
            form.populate_obj(my_doctor)
            db.session.add(my_doctor)
            db.session.commit()
            # User info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update doctor.', 'danger')
    return render_template('web/edit_doctor.html',form=form)


@app.route("/doctors")
def doctors():
    '''
    Show alls doctors
    '''
    doctors = Doctor.query.order_by(Doctor.name).all()
    return render_template('web/doctors.html', doctors=doctors)


@app.route("/search")
def search():
    '''
    Search
    '''
    name_search = request.args.get('name')
    all_doctors = Doctor.query.filter(
        Doctor.name.contains(name_search)
        ).order_by(Doctor.name).all()
    return render_template('web/doctors.html', doctors=all_doctors)


@app.route("/doctors/delete", methods=('POST',))
def doctors_delete():
    '''
    Delete doctor
    '''
    try:
        mi_doctoro = Doctor.query.filter_by(id=request.form['id']).first()
        db.session.delete(mi_doctoro)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  Doctor.', 'danger')

    return redirect(url_for('doctors'))
'''
PATIENT MODULE
'''


@app.route("/new_patient", methods=('GET', 'POST'))
def new_patient():
    '''
    Create new patient
    '''
    form = P_ContactForm()
    if form.validate_on_submit():
        my_patient = Patient()
        form.populate_obj(my_patient)
        db.session.add(my_patient)
        try:
            db.session.commit()
            # User info
            flash('Patient created correctly', 'success')
            return redirect(url_for('patients'))
        except:
            db.session.rollback()
            flash('Error generating Patient.', 'danger')

    return render_template('web/new_patient.html', form=form)


@app.route("/edit_patient/<P_id>", methods=('GET', 'POST'))
def edit_patient(P_id):
    '''
    Edit patient

    :param P_id: P_id from patient
    '''
    my_patient = Patient.query.filter_by(P_id=P_id).first()
    form = P_ContactForm(obj=my_patient)
    if form.validate_on_submit():
        try:
            # Update Patient
            form.populate_obj(my_patient)
            db.session.add(my_patient)
            db.session.commit()
            # Patient info
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update patient.', 'danger')
    return render_template('web/edit_patient.html',form=form)


@app.route("/patients")
def patients():
    '''
    Show alls patients
    '''
    patients = Patient.query.order_by(Patient.P_name).all()
    return render_template('web/patients.html', patients=patients)


@app.route("/P_search")
def P_search():
    '''
    Search
    '''
    P_name_search = request.args.get('P_name')
    all_patients = Patient.query.filter(
        Patient.P_name.contains(P_name_search)
        ).order_by(Patient.P_name).all()
    return render_template('web/patients.html', patients=all_patients)


@app.route("/patients/delete", methods=('POST',))
def patients_delete():
    '''
    Delete patient
    '''
    try:
        mi_patiento = Patient.query.filter_by(P_id=request.form['P_id']).first()
        db.session.delete(mi_patiento)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  Patient.', 'danger')

    return redirect(url_for('patients'))


if __name__ == "__main__":
    app.run(debug=True)
