from django.core.mail import send_mass_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from mysql.connector import connect

from Homework.settings import EMAIL_HOST_USER
from .forms import SLOT_CHOICE
from .models import BookingModel

# for SIGNALS write following code in app.py and __init__.py
# ---------------------------------------------------------------
#     -class BookingConfig(AppConfig):
#         name = 'booking'
#
#     def ready(self):
#         import booking.signals
# --------------------------------------------------------------------
#     default_app_config = 'booking.apps.BookingConfig'(in __init__.py)


@receiver(post_save,sender=BookingModel)
def email_send(sender,instance,created,**kwargs):
    if created:
        # recepient = (instance.objects.get(pk=instance.cleaner).user.email)

        cleaner_msg = "You have been Booked for a Date:" + str(instance.date) + SLOT_CHOICE[int(instance.timeslot)][1] + " for cleaning service at " + instance.city.city_name + "\nCustomer name : " + instance.user.first_name + "\nSee Your Orders List :127.0.0.1:8000/bookorder/'"
        print(cleaner_msg)
        customer_msg = "Congratulations!You have successfully booked a cleaner for date :" + str(instance.date) + " cleaning service at " + instance.city.city_name + "\nCustomer name : " + instance.user.first_name + "\nSee Your Orders List :127.0.0.1:8000/bookorder/'"
        print(customer_msg)
        cleaner_mail = ('You Booked', cleaner_msg, EMAIL_HOST_USER, [instance.cleaner.user.email])
        customer_mail = ('You Book', customer_msg, EMAIL_HOST_USER, [instance.user.email])

        res = send_mass_mail((cleaner_mail, customer_mail), fail_silently=False)

        print(res)  # return render(request,'booking/postbooking.html')
    else:
        raise('Not Booked!!!')
