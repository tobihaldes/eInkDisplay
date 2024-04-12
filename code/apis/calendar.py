import ussl
import usocket

def get_https_content(url):
    _, _, host, path = url.split('/', 3)
    addr_info = usocket.getaddrinfo(host, 443)
    addr = addr_info[0][-1]

    s = usocket.socket()
    s.connect(addr)
    s = ussl.wrap_socket(s, server_hostname=host)

    s.write(b"GET /{} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(path, host))

    in_content = False
    content = ''
    while True:
        data = s.read(512)
        if data:
            # Beginn des Inhalts nach dem Header-Ende suchen
            if not in_content:
                data_str = data.decode('utf-8')
                if '\r\n\r\n' in data_str:
                    headers, content = data_str.split('\r\n\r\n', 1)
                    in_content = True
            else:
                content += data.decode('utf-8')
        else:
            break

    s.close()
    return content

def parse_ics(data):
    in_event = False
    event_count = 0
    for line in data.splitlines():
        if line.startswith("BEGIN:VEVENT"):
            in_event = True
        elif line.startswith("END:VEVENT"):
            in_event = False
            event_count += 1
            if event_count >= 5:
                break
        elif in_event:
            if line.startswith("SUMMARY:"):
                print("Summary:", line[len("SUMMARY:"):].strip())
            elif line.startswith("DTSTART;") or line.startswith("DTSTART:"):
                print("Start Time:", line.split(':', 1)[1].strip())

ics_content = get_https_content("https://calendar.google.com/calendar/ical/de.german%23holiday%40group.v.calendar.google.com/public/basic.ics")
parse_ics(ics_content)
