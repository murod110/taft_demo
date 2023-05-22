from django.test import TestCase
from django.core.mail import send_mail

send_mail(
    "Hello",
    "Salom",
    ["ochilovmurodillo2@gmail.com"],
    ["maxsatilloazamov@gmail.com"]
)