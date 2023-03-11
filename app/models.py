from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
import random


class BankAccount(models.Model):
    UserId = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, blank=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    AccountBalance = models.DecimalField(decimal_places=2, max_digits=20)
    DateOpened = models.DateField(default=date.today, blank=True)
    # Do Accout Type

    def __init__(self, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.set_account_number()

    def set_account_number(self):
        # Todo: Work on the account Nuber generation Algorithm
        if self.account_number == "":
            self.account_number = str(self.id) + str(self.id*450) + \
                str(random.randint(100, 999))

    def __str__(self) -> str:
        return str(self.FirstName)

    def TransferCash(self, amount: float, recipientAccountNumber: int) -> bool:
        '''
        This Accepts the Account Number of the Recipient and searches the database for that Account and transfers money to that account
        '''
        # checks Senders Balance if it meets stndard of Sending
        if amount > self.AccountBalance or amount == 0 or self.AccountBalance == 0:
            return Exception
        # check if recipient Account Exists first
        recipientAccount = BankAccount.objects.get(
            AccountNumber=recipientAccountNumber)
        self.AccountBalance -= int(amount)
        self.save()
        recipientAccount.AccountBalance += int(amount)
        recipientAccount.save()
        return

    def deposit(self, amountToDeposit: float):
        # Check Account type to determine Amount they cAn deposit
        self.AccountBalance


class Transactions(models.Model):
    sender = models.ForeignKey(
        BankAccount, on_delete=models.DO_NOTHING, related_name='sender_transaction')
    receiver = models.ForeignKey(
        BankAccount, on_delete=models.DO_NOTHING, related_name='receiver_transaction')
    transaction_date = models.DateField(default=date.today, blank=True)
    transaction_receipt = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20, blank=True, default=0)
    def __str__(self):
        return str(sender.account_number)
