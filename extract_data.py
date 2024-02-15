from hubspot3 import Hubspot3
import pandas as pd

API_KEY = 'your-hubspot-api-key'
client = Hubspot3(api_key=API_KEY)

email_events = client.email_events.get_all()
leads_data = [{
    'email': event['recipient'],
    'open_rate': event['open_rate'],
    'click_rate': event['click_rate']
} for event in email_events]

# Convert to DataFrame
leads_df = pd.DataFrame(leads_data)
leads_df.to_csv('leads_data.csv', index=False)
