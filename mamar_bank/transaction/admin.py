from typing import Any
from django.contrib import admin
from. models import transactions

# Register your models here.
@admin.register(transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve','is_bankrupt']
    def save_model(self, request, obj, form, change):
        if obj.loan_approve==True and obj.is_bankrupt==False:
            obj.account.balance+=obj.amount
            obj.balance_after_transaction=obj.account.balance
            obj.account.save()
            super().save_model(request, obj, form, change)
