from django.shortcuts import render
from .models import BankAccount, Transactions
from PIL import Image, ImageFont, ImageDraw
from core.settings import BASE_DIR
from django.utils import timezone
# from django.http import HttpResponse


def get_all_accounts(request):

    all_bank_account = BankAccount.objects.all()
    return render(request, "all_users.html", {"users": all_bank_account, "loggedInUser": request.user})

# todo :work on redirect


def send_money(request):
    check_user_Validity(request)
    senderAccount = BankAccount.objects.get(UserId=request.user)
    receiver_account_number = request.POST['account_number'] 
    senderAccount.TransferCash(
        int(request.POST['amount']), receiver_account_number)
    edit_photo((receiver_account_number+ " " +str(timezone.now().time())) + " "+senderAccount.UserId.username)

    Transactions.objects.create(sender=senderAccount, receiver=BankAccount.objects.get(
        account_number=receiver_account_number))
    return get_all_accounts(request)


def check_user_Validity(request):
    if request.user.is_authenticated == False:
        return render(request, "all_users.html", {"users": "Not Authenticated"})
    if request.method != "POST":
        return render(request, "all_users.html", {"users": "Not Valuable"})
    if request.POST['account_number'] == "" and request.POST['amount'] == "":
        return render(request, "all_users.html", {"users": "Not Valuable"})


def edit_photo(text):
    my_image = Image.open(BASE_DIR/'nature.jpg')
# title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)
    image_editable = ImageDraw.Draw(my_image)
    font = ImageFont.truetype("Roboto-Regular.ttf", 100)
    image_editable.text((28, 36), text, fill=(255, 0, 0), font=font)
    my_image.save("result.jpg")
