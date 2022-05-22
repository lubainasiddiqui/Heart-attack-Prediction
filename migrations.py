from models import db, Doctor,Patient
from faker import Factory

fake = Factory.create()

#fake = Factory.create('es_ES')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake doctors
for num in range(100):
    fullname = fake.name().split()
    name = fullname[0]
    surname = ' '.join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    # Save in database
    mi_doctoro = Doctor(name=name, surname=surname, email=email, phone=phone)
    db.session.add(mi_doctoro)

db.session.commit()

# Make 100 fake patients
for num in range(100):
    P_fullname = fake.name().split()
    P_name = P_fullname[0]
    P_surname = ' '.join(P_fullname[1:])
    P_email = fake.email()
    P_phone = fake.phone_number()
    # Save in database
    mi_patiento = Patient(P_name=P_name, P_surname=P_surname, P_email=P_email, P_phone=P_phone)
    db.session.add(mi_patiento)

db.session.commit()
