from django.shortcuts import render,get_object_or_404,redirect
from. forms import DepositeForm,WithdrawalForm,LoanRequestForm,TransferForm
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import transactions
from.constants import DEPOSITE,LOAN_PAID,LOAN,WITHDRAWAL,TRANSFER
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.views import View
from django.urls import reverse_lazy
from accounts.models import UserBankAccount
# Create your views here.

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name="transaction/transaction_form.html"
    model=transactions
    title=""
    success_url=reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update({
          'account' : self.request.user.account, 
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })
        return context

class DepositeMoneyView(TransactionCreateMixin):
    form_class=DepositeForm
    title="Deposite Money"

    def get_initial(self):
        initial={'transaction_type' : DEPOSITE}
        return initial

    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance+=amount
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request,f"${amount} is deposited in your account")
        return super().form_valid(form)
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class=WithdrawalForm
    title="Withdraw Money"

    def get_initial(self):
        initial={'transaction_type' : WITHDRAWAL}
        return initial

    def form_valid(self, form):
        # status=get_object_or_404(transactions)
        # if self.user.status.is_bankrupt==False:
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance-=amount
        account.save(
            update_fields=['balance']
        )
        messages.success(self.request,f"${amount} is withdraw from your account successfully")
        return super().form_valid(form)
        # else:
        #     messages.warning(self.request,"bank is bankrupt")
        #     return redirect('home')
class LoanRequstView(TransactionCreateMixin):
    form_class=LoanRequestForm
    title="Request For Loan"

    def get_initial(self):
        initial={'transaction_type' : LOAN}
        return initial

    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        current_loan_count=transactions.objects.filter(account=self.request.user.account,transaction_type=3,loan_approve=True).count()
        
        if current_loan_count>=3:
            return HttpResponse('You already crossed your limits')
      
        messages.success(self.request,f"${amount} loan amount request  submited successfully")
        return super().form_valid(form)

class TransationReportView(LoginRequiredMixin,ListView):
    template_name="transaction/transaction_report.html"
    model=transactions
    balance=0

    def get_queryset(self):
        queryset=super().get_queryset().filter(
          account=self.request.user.account  
        )
        start_date_str=self.request.GET.get('start_date')
        end_date_str=self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date=datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date=datetime.strptime(end_date_str, "%Y-%m-%d").date()
            queryset=queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = transactions.objects.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance=self.request.user.account.balance
        return queryset.distinct()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })
        return context

class PayLoanView(LoginRequiredMixin,View):
    def get(self, request, loan_id):
        loan=get_object_or_404(transactions,id=loan_id)

        if loan.loan_approve:
            user_account=loan.account
            if loan.amount < user_account.balance:
                user_account.balance-=loan.amount
                loan.balance_after_transaction=user_account.balance
                user_account.save()
                loan.transaction_type=LOAN_PAID
                loan.save()
                return redirect('pay')
            else:
                messages.error(self.request, f"loan amount is greater than your current balance")
        return redirect('loan_list')

class LoanListView(LoginRequiredMixin,ListView):
    model = transactions
    template_name='transaction/loan_request.html'
    context_object_name="loans"

    def get_queryset(self):
        user_account=self.request.user.account
        queryset=transactions.objects.filter(account=user_account, transaction_type=LOAN)
        return queryset

# class TransferMoneyView(LoginRequiredMixin,View):
#     form_class=TransferForm
#     template_name='transaction/transfer_form.html'
#     title="Transfer Money"
#     # account=UserBankAccount.get('account_number')
#     account_numbers = UserBankAccount.objects.values_list('account_number', flat=True)
#     print(account_numbers)

#     def get_initial(self):
#         initial={'transaction_type' : TRANSFER}
#         return initial

#     def form_valid(self, form):
#         t_account=form.claned_data.account
#         amount=form.claned_data.amount
#         # amount=form.cleaned_data.get['amount']
#         # t_account=form.cleaned_data.get['account']
#         print(t_account,amount)
#         account=self.request.user.account
#         if t_account not in self.account_numbers:
#             messages.warning(self.request,'Invalid Account')
            
#         else:
#             account.balance-=amount
#             t_account.balance+=amount
#             # account.save(
#             #     update_fields=['balance']
#             # )
#             print(account.balance)
#             print(t_account.balance)
#             account.save()
#             t_account.save()
#             print(account.balance)
#             print(t_account.balance)
#             # t_account.save(
#             #     update_fields=['balance']
#             # )
#             messages.success(self.request,f"${amount} is transfer from your account successfully")
#             return super().form_valid(form)


class TransferMoneyView(TransactionCreateMixin):
    form_class=WithdrawalForm
    title="Transfer Money"

    def get_initial(self):
        initial={'transaction_type' : TRANSFER}
        return initial

    def form_valid(self, form):
        # loan=get_object_or_404(transactions)
        # if loan.is_bankrupt==False:
        amount=form.cleaned_data.get('amount')
        tar_account=form.cleaned_data.get('account')
        account=self.request.user.account
        tar_user=UserBankAccount.objects.get(account_number = tar_account)
        print(tar_user)
        account.balance-=amount
        # tar_user.balance+=amount
        account.save(
            update_fields=['balance']
        )
        tar_user.save(
            update_fields=['balance']
        )
        messages.success(self.request,f"${amount} is transfer from your account successfully")
        return super().form_valid(form)
        # else:
        #     messages.warning(self.request,"bank is bankrupt")
        #     return redirect('home')