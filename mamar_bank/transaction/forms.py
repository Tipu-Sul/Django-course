from typing import Any
from django import forms
from. models import transactions

class TransactionForm(forms.ModelForm):
    class Meta: 
        model=transactions
        fields=['amount','transaction_type']

    def __init__(self, *args, **kwargs):
        self.account =kwargs.pop('account') 
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled=True
        self.fields['transaction_type'].widget=forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account=self.account
        self.instance.balance_after_transaction=self.account.balance
        return super().save()

class TransferMoneyForm(forms.ModelForm):
    class Meta: 
        model=transactions
        fields=['amount','account','transaction_type']

    def __init__(self, *args, **kwargs):
        self.account =kwargs.pop('account') 
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled=True
        self.fields['transaction_type'].widget=forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account=self.account
        self.instance.balance_after_transaction=self.account.balance
        return super().save()



class DepositeForm(TransactionForm):
    def clean_amount(self):
        min_diposite_amount=100
        amount=self.cleaned_data.get('amount')
        if amount<min_diposite_amount:
            raise forms.ValidationError(
                f"You can deposite at least $ {min_diposite_amount}"
            )
        return amount

class WithdrawalForm(TransactionForm):
    def clean_amount(self):
        account=self.account
        min_withdraw_amount=100
        max_withdraw_amount=10000
        balance=account.balance
        amount=self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f"You cann't withdraw below $ {min_withdraw_amount}"
            )
        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f"You cann't withdraw more than $ {max_withdraw_amount}"
            )
        if amount > balance:
            raise forms.ValidationError(
                f"You have ${balance} in your account, You can not  withdraw more than  your balance"
            )
        return amount
    
    def clean_account(self):
        account=self.cleaned_data.get('account')
        return account

class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount=self.cleaned_data.get('amount')
        return amount

class TransferForm(forms.ModelForm):
    class Meta:
        model=transactions
        fields=['account', 'amount','transaction_type']
    def clean(self):
        cleaned_data=super().clean()
        account=cleaned_data.get('account'),  
        amount=cleaned_data.get('amount')
         

        min_transfer=100

        if not account:
            raise forms.ValidationError(
               'invalid account' 
            )
        user_account=account
        balance=user_account.balance

        if amount<min_transfer:
            raise forms.ValidationError(
                f"You can transfer at least {min_transfer} $"
            )
        
        if amount>balance:
            raise forms.ValidationError(
                f"You have ${balance} in your account.Insufficient balance"

            )
        return cleaned_data
                
            
            
           
            

# class TransferForm(TransferMoneyForm):

#     def clean_amount(self):
#         account=self.account
#         min_withdraw_amount=10
#         max_withdraw_amount=10000
#         balance=account.balance
#         amount=self.cleaned_data.get('amount')
#         if amount < min_withdraw_amount:
#             raise forms.ValidationError(
#                 f"You cann't transfer below $ {min_withdraw_amount}"
#             )
#         if amount > max_withdraw_amount:
#             raise forms.ValidationError(
#                 f"You cann't transfer more than $ {max_withdraw_amount}"
#             )
#         if amount > balance:
#             raise forms.ValidationError(
#                 f"You have ${balance} in your account, You can not  transfer more than  your balance"
#             )
#         return amount

#     def clean_account(self):
#         account=self.cleaned_data.get('account')
#         return account
    
