# These data reading functions can be used over and over by just importing them
# from this file, which prevents redundancy.

def split_data():
    data = get_data_dict('./data/alzheimers_disease_data.csv')
    metadata_keys = ["PatientID", "Diagnosis", "DoctorInCharge"]
    internal_factors_keys = [
        "Age", "Gender", "Ethnicity", "BMI", "FamilyHistoryAlzheimers",
        "CardiovascularDisease", "Diabetes", "Depression", "Hypertension",
        "SystolicBP", "DiastolicBP", "CholesterolTotal", "CholesterolLDL",
        "CholesterolHDL", "CholesterolTriglycerides", "MMSE", "FunctionalAssessment",
        "MemoryComplaints", "BehavioralProblems", "ADL", "Confusion",
        "Disorientation", "PersonalityChanges", "DifficultyCompletingTasks",
        "Forgetfulness", "HeadInjury"
    ]
    external_factors_keys = ["EducationLevel", "Smoking", "AlcoholConsumption",
                             "PhysicalActivity", "DietQuality", "SleepQuality"]

    metadata = {key: data[key] for key in metadata_keys if key in data}
    internal_factors = {key: data[key]
                        for key in internal_factors_keys if key in data}
    external_factors = {key: data[key]
                        for key in external_factors_keys if key in data}

    return metadata, internal_factors, external_factors


def get_data_dict(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    header = lines[0].strip().split(',')
    data = {column: [] for column in header}
    for line in lines[1:]:
        values = line.strip().split(',')
        for i, value in enumerate(values):
            try:
                num = float(value)
                num = int(num) if num.is_integer() else num
                data[header[i]].append(num)
            except ValueError:
                data[header[i]].append(value)
    return data
