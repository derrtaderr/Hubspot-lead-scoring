from hubspot3 import Hubspot3

# Assuming `model` is loaded and `leads_data_features` is prepared
predicted_scores = model.predict_proba(leads_data_features)
lead_scores = [{'email': lead['email'], 'score': score[1]} for lead, score in zip(leads_data, predicted_scores)]

API_KEY = 'your-hubspot-api-key'
client = Hubspot3(api_key=API_KEY)

for lead in lead_scores:
    client.contacts.update_by_email(lead['email'], {'lead_score': lead['score']})
