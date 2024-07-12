'''3) create a Python dict
   of Patient id  Patient name ailment - call it as patient_dict
   keep adding the details till the user types -1 to STOP
   convert patient_dict to json str - patient_json_str
   check whether patient_json_str is valid or not ::: test that on https://jsonlint.com/
'''
import json
def inpt():
    temp_dict={}
    while True:
        patient_id = int(input('Enter Patient ID: '))
        if patient_id == -1:
            break
        patient_name = input('Enter Patient Name: ')
        ailment = input('Enter Ailment: ')
        print()

        temp_dict[patient_id] = {"Patient Name": patient_name, "Ailment": ailment}
    return temp_dict
print('--------------MAIN BLOCK START-------------')
patient_dict = inpt()

patient_json_str = json.dumps(patient_dict)
print()
print('JSON RESULT:\n',patient_json_str)
