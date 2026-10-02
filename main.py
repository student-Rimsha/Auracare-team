3.	# AuraCare Health System Core
4.	APP_VERSION = "1.0.0"
5.	MODULES_ENABLED = []
def get_doctor_schedule(doctor_name):
    return f"Schedule for Dr. {doctor_name}: Available Mon-Fri, 9 AM - 4 PM"





def patient_triage(symptoms):
    if "chest pain" in symptoms:
        return "Emergency"
    elif "fever" in symptoms:
        return "Urgent"
    else:
        return "Routine"
