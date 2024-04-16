import urequests

# URL anpassen von webcal zu http
url = 'http://p139-caldav.icloud.com/published/2/MTE1NzQwNjE0NzQxMTU3NDmLjpu4-S1Y9s3ZY6FOrrHnIwf0-kAOhn-6sr24tcTFaqodbcvwQ-1iUIyMWm_Q-QI6qieG29wXJSUU0hdN6JI'

# Funktion zum Extrahieren der Ereignisse aus den iCalendar-Daten
def format_datetime(datetime_str):
    if 'T' in datetime_str:
        date_part, time_part = datetime_str.split('T')
        formatted_date = f"{date_part[:4]}-{date_part[4:6]}-{date_part[6:]}"
        formatted_time = f"{time_part[:2]}:{time_part[2:4]}"
        return f"{formatted_date} {formatted_time}"
    return f"{datetime_str[:4]}-{datetime_str[4:6]}-{datetime_str[6:]}"

# Funktion zum Extrahieren der Ereignisse aus den iCalendar-Daten
def extract_events(ical_data):
    events = []
    lines = ical_data.splitlines()
    in_event = False
    for line in lines:
        if line.startswith('BEGIN:VEVENT'):
            in_event = True
            current_event = {}
        elif line.startswith('END:VEVENT'):
            events.append(current_event)
            in_event = False
        elif in_event:
            if line.startswith('SUMMARY:'):
                current_event['summary'] = line.split(':', 1)[1]
            elif 'DTSTART' in line:
                time_part = line.split(':', 1)[1]
                current_event['start_time'] = format_datetime(time_part)

    return events[:5]

# HTTP-Anfrage senden, um die iCalendar-Daten zu erhalten
response = urequests.get(url)

if response.status_code == 200:
    # Ereignisse extrahieren und die nächsten fünf ausgeben
    next_events = extract_events(response.text)
    for event in next_events:
        print(f"Event: {event['summary']}, Start Time: {event['start_time']}")
else:
    print('Fehler beim Abrufen der Daten:', response.status_code)

response.close()