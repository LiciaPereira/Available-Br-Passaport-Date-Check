from requests_html import HTMLSession
from datetime import datetime
from plyer import notification
import time

# URL you want to monitor
target_url = 'https://ec-toronto.itamaraty.gov.br/availability'
threshold_date = datetime.strptime("March 21, 2025", "%B %d, %Y")

# Initialize the HTML session and set cookies
session = HTMLSession()

# Replace with your actual cookies (name-value pairs)
cookies = {
    'FGTServer': 'DD1EF3BDF21D114F06347FA70BE64CEFB21A85C1F22DC6D21D4B13EE647F7BE509A75CF2DED3E3DBCE59A7BDBC9141941D51',
    'ec-session': 'eyJ0b2tlbiI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpsYldGcGJDSTZJbXhwWTJsaGNHVnlaV2x5WVVCcFkyeHZkV1F1WTI5dElpd2ljR0Z6Y3lJNlptRnNjMlVzSW14dloybHVkVzVwWTI4aU9uUnlkV1VzSW1OdmNtUnBiR2hsYVhKaElqcG1ZV3h6WlN3aWFXRjBJam94TnpReE56ZzNNVEE1TENKbGVIQWlPakUzTkRFNE1UVTVNRGw5LlJ1anpTdmJnSC1NMkpBVjB3TjM4WWp1SzhOY0lRXzBmVWlsejFua2Z0QmMifQ==',
    'ec-session.sig': 'ziNSfoeQ49e687oX5CfK5OBlRhI'
}

# Set cookies for the session
session.cookies.update(cookies)

def fetch_website(url):
    response = session.get(url)
    print(f"Target page status: {response.status_code}")
    soup = response.html
    rows = soup.find('tr')
    return rows

def check_for_earlier_date(rows, threshold_date):
    for row in rows:
        cells = row.find('td')
        if len(cells) > 1 and "Passaporte para maiores de 18 anos PRESENCIAL/POR AGENDAMENTO" in cells[0].text:
            date_text = cells[1].text.strip()
            print(f"Checking date: {date_text}")  # Debugging statement
            try:
                appointment_date = datetime.strptime(date_text, "%A, %B %d, %Y")
                print(f"Parsed date: {appointment_date}")  # Debugging statement
                if appointment_date < threshold_date:
                    return True, appointment_date
            except ValueError:
                print(f"Invalid date format: {date_text}")  # Debugging statement
    return False, None

def show_notification(appointment_date):
    notification.notify(
        title='Date Alert',
        message=f'Found an earlier date than March 21, 2025: {appointment_date.strftime("%A, %B %d, %Y")}',
        timeout=10
    )

print('The code is running...')

# Main logic
while True:
    rows = fetch_website(target_url)
    found_earlier_date, appointment_date = check_for_earlier_date(rows, threshold_date)
    if found_earlier_date:
        show_notification(appointment_date)
        print(f"Found an earlier date than March 21, 2025: {appointment_date.strftime('%A, %B %d, %Y')}")
    else:
        print("No earlier date found.")
    time.sleep(60)  # Check every 1 minute
