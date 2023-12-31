from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.db.models import Avg, Count, F
from googletrans import Translator

translator = Translator()


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get('lang', 'ru')


def retrieve_housetrans(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.housing_name = translator.translate(instance.housing_name, dest=lang).text
    instance.address = translator.translate(instance.address, dest=lang).text
    instance.region = translator.translate(instance.region, dest=lang).text
    instance.housing_type = translator.translate(instance.housing_type, dest=lang).text
    instance.accommodation_type = translator.translate(instance.accommodation_type, dest=lang).text
    instance.food_type = translator.translate(instance.food_type, dest=lang).text
    instance.breakfast_type = translator.translate(instance.breakfast_type, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)


def retrieve_room(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.housing = translator.translate(instance.housing, dest=lang).text
    instance.room_name = translator.translate(instance.room_name, dest=lang).text
    instance.room_amenities = translator.translate(instance.room_amenities, dest=lang).text
    instance.kitchen = translator.translate(instance.kitchen, dest=lang).text
    instance.outside = translator.translate(instance.outside, dest=lang).text
    instance.bathroom = translator.translate(instance.bathroom, dest=lang).text
    instance.bed_type = translator.translate(instance.bed_type, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)


def retrieve_room_reservation(self, request, *args, **kwargs):
    instance = self.get_object()
    lang = self.get_language()

    instance.housing = translator.translate(instance.housing, dest=lang).text

    serializer = self.get_serializer(instance)
    return Response(serializer.data)


def perform_create(self, serializer):
    instance = serializer.save()
    subject = 'Новое бронирование'
    message = (
        f"Уважаемый {instance.username}\n\n"
        f"Ваше бронирование на место жительства '{instance.housing}' ваша заявка принята.\n"
        f"Дата заезда: {instance.check_in_date}\n"
        f"Дата выезда: {instance.check_out_date}\n"
    )
    from_email = "abdykadyrovsyimyk0708@gmail.com"
    recipient_email = instance.client_email
    try:
        send_mail(subject, message, from_email, [recipient_email])
    except Exception as e:
        return Response(
            {"error": "Не удалось отправить уведомление на почту клиенту"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    subject_forowner = 'Новое бронирование'
    message_forowner = (
        f"У вас есть новое бронирование на место жительства '{instance.housing}'\n"
        f"Дата заезда: {instance.check_in_date}\n"
        f"Дата выезда: {instance.check_out_date}\n"
        f"Имя клиента: {instance.username}\n"
        f"Почта клиента: {instance.client_email}\n"
        f"Номер телефона клиента: {instance.phone_number}\n"
        f"Количество взрослых: {instance.adults}\n"
        f"Количество детей: {instance.children}\n"
    )
    owner_email = instance.housing.user.email
    try:
        send_mail(subject_forowner, message_forowner, from_email, [owner_email])
    except Exception as e:
        return Response(
            {"error": "Не удалось отправить уведомление на почту владельцу"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return Response(serializer.data, status=status.HTTP_201_CREATED)


def annotate_housing_queryset(queryset):
    return queryset.annotate(
        average_rating=Avg(
            F('reviews__staff_rating') +
            F('reviews__comfort_rating') +
            F('reviews__cleanliness_rating') +
            F('reviews__value_for_money_rating') +
            F('reviews__food_rating') +
            F('reviews__location_rating')
        ) / 6,
        review_count=Count('reviews')
    ).distinct()
