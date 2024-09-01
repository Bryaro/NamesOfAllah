from django.core.mail import send_mail
from django.utils.timezone import now
from reminders.models import NameOfAllah

def send_daily_reminder():
    day_number = now().timetuple().tm_yday % 99 + 1  # Loops through the 99 names
    name = NameOfAllah.objects.get(day_number=day_number)
    subject = f"Day {name.day_number}: {name.name} - {name.meaning}"
    message = f"Name: {name.name}\nTransliteration: {name.transliteration}\nMeaning: {name.meaning}"
    send_mail(
        subject, 
        message, 
        'noreply@example.com',  # Sender's email
        ['bryarosman.bo@gmail.com']  # Replace with actual recipient emails
    )
