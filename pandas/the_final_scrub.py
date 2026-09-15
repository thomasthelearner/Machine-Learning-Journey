import pandas as pd

patients = pd.DataFrame({
  'patient_id': [
    'PT-2001', 'PT-2001', 'PT-2002', 'PT-2003', 
    'PT-2004', 'PT-2005', 'PT-2006', 'PT-2006', 
    'PT-2007', 'PT-2008', 'PT-2009', 'PT-2010', 
    'PT-2011'
  ],
  'name': [
    'Anthony Ramirez', 'anthony ramirez', 'Grace Mitchell', 'Daniel Brooks', 
    'Nina Patel', 'Marcus Johnson', 'Elena Cruz', 'elena cruz', 
    'William Carter', 'Sophia Nguyen', None, 'Sophia Nguyen', 
    'Ethan Walker'
  ],
  'age': [
    '52', '52', 34, '28', 
    '61', 47, '26', 26, 
    '73', '39', 44, '39', 
    '58'
  ],
  'department': [
    'ER', 'er', 'Trauma', 'ER', 
    'Cardiology', 'Trauma', 'ER', 'er', 
    'ICU', 'ER', 'ER', 'ER', 
    'ICU'
  ],
  'triage_level': [
    'Critical', 'critical', 'Moderate', 'HIGH', 
    'Low', 'Moderate', 'critical', 'CRITICAL', 
    'High', 'Low', 'Moderate', 'low', 
    None
  ],
  'wait_time_minutes': [
    '12', '12', 55, '40 mins', 
    140, 60, '8', 8, 
    '95', '25', None, '25', 
    '70'
  ],
  'admitted': [
    True, True, False, True, 
    True, False, True, True, 
    False, True, False, True, 
    None
  ]
})

patients['name'] = patients['name'].str.title()
patients['age'] = pd.to_numeric(patients['age'], errors='coerce')
patients['department'] = patients['department'].str.title()
patients['triage_level'] = patients['triage_level'].str.title()
patients['wait_time_minutes'] = pd.to_numeric(patients['wait_time_minutes'], errors='coerce')
patients = patients.drop_duplicates()
patients = patients.dropna(subset=['name', 'triage_level', 'admitted'])

print(patients)