from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacts


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact_obj = Contacts(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                           user_id=user_id)
        contact_obj.save()

        if request.user.is_authenticated:
            user_id = request.user.id
            has_made_inquiry = Contacts.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_made_inquiry:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)
        return redirect('/listings/' + listing_id)
