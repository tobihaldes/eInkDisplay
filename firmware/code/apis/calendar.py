import urequests

def format_datetime(datetime_str):
    """Hilfsfunktion zur Formatierung von iCalendar-Datums-/Zeitstrings."""
    if 'T' in datetime_str:
        date_part, time_part = datetime_str.split('T')
        formatted_date = f"{date_part[:4]}-{date_part[4:6]}-{date_part[6:]}"
        formatted_time = f"{time_part[:2]}:{time_part[2:4]}"
        return f"{formatted_date} {formatted_time}"
    return f"{datetime_str[:4]}-{datetime_str[4:6]}-{datetime_str[6:]}"

def extract_events(ical_data):
    """Hilfsfunktion zum Extrahieren von Ereignissen aus iCalendar-Daten."""
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

def get_next_events(url):
    """Funktion, die die nächsten 5 Ereignisse aus einem iCalendar über eine HTTP-Anfrage abruft."""
    response = None
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            events = extract_events(response.text)
            return events
        else:
            print('Fehler beim Abrufen der Daten:', response.status_code)
            events = [{'summary': 'Keine Daten', 'start_time': '9999-99-99'} for _ in range(8)]
            return events
    except OSError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        events = [{'summary': 'Keine Daten', 'start_time': '9999-99-99'} for _ in range(8)]
        return events
    
    finally:
        # Die Verbindung schließen, wenn sie geöffnet wurde
        if response is not None:
            try:
                response.close()
            except AttributeError:
                pass  # Falls response.close() fehlschlägt, nichts tun