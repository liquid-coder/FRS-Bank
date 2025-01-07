from django import forms
from .models import Transaction
class TransactionForm(forms.ModelForm): # Transaction form tai deposit,withdraw,loan_request e inherit korbo
    class Meta:
        model = Transaction
        fields = ['amount','transaction_type']  #amount user dibe and transaction type backend theke dbo    

    def __init__(self, *args, **kwargs): # transaction_type ta jeno user dekhte na pai oijnne eida kortesi 
        self.account = kwargs.pop('account') # account value ke pop kore anlam,kwargs onk keyword thakbe oida then bair korsi,pop/get ekta use korlei hbe
        super().__init__(*args, **kwargs)   
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korbo #clean_amount ekta built in method
        min_deposit_amount = 500
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount


class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 550
        max_withdraw_amount = 20000
        balance = account.balance # 1000
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )
        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount



class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount