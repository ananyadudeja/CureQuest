from flask import Flask, render_template, request
import pandas as pd
import json
from sqlalchemy import create_engine, text, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Database setup (SQLite)
engine = create_engine('sqlite:///curequest.db')
Base = declarative_base()

class Disease(Base):
    __tablename__ = 'diseases'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    medication_cost = Column(Float)
    diagnostic_test_cost = Column(Float)
    out_of_pocket_cost = Column(Float)
    insurance_coverage = Column(Float)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

#Function to add disease to the database
def add_disease_to_db(disease_name, medication_cost, diagnostic_test_cost, out_of_pocket_cost, insurance_coverage):
  with Session() as session:
    new_disease = Disease(name=disease_name, medication_cost=medication_cost, diagnostic_test_cost=diagnostic_test_cost, out_of_pocket_cost=out_of_pocket_cost, insurance_coverage=insurance_coverage)
    session.add(new_disease)
    session.commit()


# Function to get disease data from the database
def get_disease_data_db(disease_name):
    with Session() as session:
        result = session.execute(text(f"SELECT * FROM diseases WHERE name = '{disease_name}'")).fetchone()
        if result:
            return {
                "labels": ["Medication Cost", "Diagnostic Test Cost", "Out-of-Pocket Cost", "Insurance Coverage"],
                "data": [result.medication_cost, result.diagnostic_test_cost, result.out_of_pocket_cost, result.insurance_coverage]
            }
        else:
            return {"labels": [], "data": []}



doctor_data = [
    {
        "name": "Dr. Smith",
        "specialty": "Cardiology",
        "years_experience": 15,
        "success_rate": 0.85,
        "patient_satisfaction": 4.5,
        "num_patients_seen": 500,
        "location": "New York"
    },
    {
        "name": "Dr. Jones",
        "specialty": "Oncology",
        "years_experience": 10,
        "success_rate": 0.90,
        "patient_satisfaction": 4.8,
        "num_patients_seen": 300,
        "location": "Los Angeles"
    },
    {
        "name": "Dr. Brown",
        "specialty": "Pediatrics",
        "years_experience": 5,
        "success_rate": 0.80,
        "patient_satisfaction": 4.2,
        "num_patients_seen": 200,
        "location": "Chicago"
    },
    {
        "name": "Dr. Williams",
        "specialty": "Neurology",
        "years_experience": 20,
        "success_rate": 0.88,
        "patient_satisfaction": 4.7,
        "num_patients_seen": 700,
        "location": "Houston"
    },
    {
        "name": "Dr. Taylor",
        "specialty": "Orthopedics",
        "years_experience": 12,
        "success_rate": 0.83,
        "patient_satisfaction": 4.4,
        "num_patients_seen": 450,
        "location": "Phoenix"
    },
    {
        "name": "Dr. Martinez",
        "specialty": "Endocrinology",
        "years_experience": 8,
        "success_rate": 0.87,
        "patient_satisfaction": 4.6,
        "num_patients_seen": 280,
        "location": "San Antonio"
    },
    {
        "name": "Dr. Lee",
        "specialty": "Dermatology",
        "years_experience": 6,
        "success_rate": 0.92,
        "patient_satisfaction": 4.9,
        "num_patients_seen": 320,
        "location": "San Diego"
    },
    {
        "name": "Dr. Patel",
        "specialty": "Gastroenterology",
        "years_experience": 18,
        "success_rate": 0.89,
        "patient_satisfaction": 4.5,
        "num_patients_seen": 600,
        "location": "Dallas"
    },
    {
        "name": "Dr. Kim",
        "specialty": "Pulmonology",
        "years_experience": 14,
        "success_rate": 0.84,
        "patient_satisfaction": 4.3,
        "num_patients_seen": 400,
        "location": "San Jose"
    },
    {
        "name": "Dr. Johnson",
        "specialty": "Ophthalmology",
        "years_experience": 9,
        "success_rate": 0.91,
        "patient_satisfaction": 4.8,
        "num_patients_seen": 350,
        "location": "Austin"
    },
    {
        "name": "Dr. Carter",
        "specialty": "Nephrology",
        "years_experience": 16,
        "success_rate": 0.86,
        "patient_satisfaction": 4.6,
        "num_patients_seen": 480,
        "location": "Jacksonville"
    },
    {
        "name": "Dr. Adams",
        "specialty": "Rheumatology",
        "years_experience": 11,
        "success_rate": 0.82,
        "patient_satisfaction": 4.4,
        "num_patients_seen": 370,
        "location": "Columbus"
    },
    {
        "name": "Dr. White",
        "specialty": "Hematology",
        "years_experience": 7,
        "success_rate": 0.89,
        "patient_satisfaction": 4.7,
        "num_patients_seen": 260,
        "location": "Charlotte"
    },
    {
        "name": "Dr. Green",
        "specialty": "Psychiatry",
        "years_experience": 13,
        "success_rate": 0.81,
        "patient_satisfaction": 4.3,
        "num_patients_seen": 420,
        "location": "Indianapolis"
    },
    {
        "name": "Dr. Cooper",
        "specialty": "Urology",
        "years_experience": 17,
        "success_rate": 0.88,
        "patient_satisfaction": 4.5,
        "num_patients_seen": 550,
        "location": "San Francisco"
    },
    {
        "name": "Dr. Parker",
        "specialty": "Otolaryngology",
        "years_experience": 10,
        "success_rate": 0.86,
        "patient_satisfaction": 4.4,
        "num_patients_seen": 330,
        "location": "Seattle"
    },
    {
        "name": "Dr. Evans",
        "specialty": "Anesthesiology",
        "years_experience": 22,
        "success_rate": 0.92,
        "patient_satisfaction": 4.9,
        "num_patients_seen": 800,
        "location": "Denver"
    },
    {
        "name": "Dr. Scott",
        "specialty": "Plastic Surgery",
        "years_experience": 19,
        "success_rate": 0.87,
        "patient_satisfaction": 4.6,
        "num_patients_seen": 650,
        "location": "Boston"
    },
    {
        "name": "Dr. Morris",
        "specialty": "Emergency Medicine",
        "years_experience": 8,
        "success_rate": 0.84,
        "patient_satisfaction": 4.3,
        "num_patients_seen": 300,
        "location": "Nashville"
    },
    {
        "name": "Dr. Ramirez",
        "specialty": "General Surgery",
        "years_experience": 15,
        "success_rate": 0.90,
        "patient_satisfaction": 4.8,
        "num_patients_seen": 570,
        "location": "Detroit"
    },
]

def get_doctors(location, specialty):
    found_doctors = []
    for doctor in doctor_data:
        print(f"Checking doctor: {doctor['name']} - Location: '{doctor['location']}', Specialty: '{doctor['specialty']}'")  #Debug print statements
        if doctor['location'] == location and doctor['specialty'] == specialty:
            found_doctors.append(doctor)
    return found_doctors


# Simplified diet recommendation data
diet_recommendations = {
    "low_activity_low_calories": {
        "description": "Low-calorie diet for low-activity individuals",
        "suggestions": [
            "Eat plenty of fruits and vegetables.",
            "Choose lean proteins.",
            "Limit processed foods and sugary drinks."
        ]
    },
    "high_activity_high_calories": {
        "description": "High-calorie diet for high-activity individuals",
        "suggestions": [
            "Eat more calories than you burn.",
            "Include complex carbohydrates.",
            "Focus on lean protein."
        ]
    },
    "vegetarian_low_fat": {
        "description": "Low-fat vegetarian diet",
        "suggestions": [
            "Focus on plant-based proteins.",
            "Include plenty of fruits and vegetables.",
            "Limit saturated fats."
        ]
    },
    "vegan_high_protein": {
        "description": "High-protein vegan diet",
        "suggestions": [
            "Eat a variety of plant-based proteins.",
            "Include legumes, tofu, tempeh, and nuts.",
            "Ensure sufficient calorie intake for high activity."
        ]
    }

}

def get_diet_recommendation(age, activity_level, dietary_restrictions):
    error_message = None

    try:
        age = int(age)
        if age < 1:
            error_message = "Please enter a valid age (greater than 0)."
        elif activity_level not in ["low", "medium", "high"]:
            error_message = "Please select a valid activity level."
    except ValueError:
        error_message = "Invalid age entered. Please enter a number."


    if error_message:
        return {"description": error_message, "suggestions": []}
    if dietary_restrictions and "vegetarian" in dietary_restrictions.lower():
        if activity_level == "low":
            return diet_recommendations.get("vegetarian_low_fat")
        else:
            return {"description": "Vegetarian high-activity diet plan not available yet.", "suggestions": []}
    elif dietary_restrictions and "vegan" in dietary_restrictions.lower():
        if activity_level == "high":
            return diet_recommendations.get("vegan_high_protein")
        else:
            return {"description": "Vegan low-activity diet plan not available yet.", "suggestions": []}
    elif activity_level == "low":
        return diet_recommendations.get("low_activity_low_calories")
    elif activity_level == "high":
        return diet_recommendations.get("high_activity_high_calories")
    else:
        return {"description": "No specific recommendation available.", "suggestions": []}

@app.route("/", methods=["GET", "POST"])
def home():
    disease_data = {"labels": [], "data": []}
    cost_estimate = None
    if request.method == "POST":
        disease_name = request.form.get("disease")
        if disease_name:
            disease_data = get_disease_data_db(disease_name)
            if disease_data and disease_data["data"]:
                cost_estimate = sum(disease_data["data"])
    return render_template("index.html", disease_data=disease_data, cost_estimate=cost_estimate)


@app.route("/doctor", methods=["GET", "POST"])
def doctor_recommendation():
    doctors = []
    if request.method == "POST":
        selected_location = request.form.get("location")
        selected_specialty = request.form.get("specialty")
        print(f"Location: {selected_location}, Specialty: {selected_specialty}")
        if selected_location and selected_specialty:
            doctors = get_doctors(selected_location, selected_specialty)
    else:
        doctors = get_doctors("New York", "Cardiology")
    return render_template("doctor.html", doctors=doctors)

@app.route("/diet", methods=["GET", "POST"])
def diet_recommendation():
    diet_plan = None
    if request.method == "POST":
        age = int(request.form.get("age"))
        activity_level = request.form.get("activity_level")
        dietary_restrictions = request.form.get("dietary_restrictions")
        diet_plan = get_diet_recommendation(age, activity_level, dietary_restrictions)
    return render_template("diet.html", diet_plan=diet_plan)

@app.route("/disease", methods=["GET", "POST"])
def disease_cost_estimator():
    disease_data = {"labels": [], "data": []}
    cost_estimate = None
    if request.method == "POST":
        disease_name = request.form.get("disease")
        if disease_name:
            disease_data = get_disease_data_db(disease_name)
            if disease_data and disease_data["data"]:
                cost_estimate = sum(disease_data["data"])
    return render_template("disease.html", disease_data=disease_data, cost_estimate=cost_estimate)


def add_diseases_from_csv():
    try:
        df = pd.read_csv("disease_costs.csv")
        with Session() as session:
            session.execute(text("DELETE FROM diseases"))
            session.commit()
            for index, row in df.iterrows():
                add_disease_to_db(row['Disease Name'], row['Medication Cost'], row['Diagnostic Test Cost'], row['Out-of-Pocket Cost'], row['Insurance Coverage'])
    except FileNotFoundError:
        print("Error: disease_costs.csv not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    add_diseases_from_csv()
    app.run(debug=True)