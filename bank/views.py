from django.shortcuts import render


from django.shortcuts import  get_object_or_404, redirect
from bank.models import Customer, Transfer

def home(request):
    return render(request, 'home.html')

def view_customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'view_customers.html', context)

def view_customer(request, id):
    data = Customer.objects.get(id=id)
    
    context = {'customer': data}
    return render(request, 'view_customer.html', context)

def tranfer(request,id):
    data = Customer.objects.get(id=id)
    customers = Customer.objects.all()
    return render(request, 'transfer_money.html',{'customers': customers,'data': data})


def tranferhome(request):
    customers = Customer.objects.all()
    return render(request, 'transfermoney.html',{'customers': customers})


def transfer_money(request):
    if request.method == 'POST':
        sender_id = request.POST['sender']
        receiver_id = request.POST['receiver']
        amount = request.POST['amount']
        sender = Customer.objects.get(id=sender_id)
        senderbalance=sender.current_balance
        receiver = Customer.objects.get( id=receiver_id)
        receiverbalance=receiver.current_balance
        newsenderbalance=int(senderbalance)-int(amount)
        newreceiverbalance=int(receiverbalance)-int(amount)
        sender.current_balance = newsenderbalance
        receiver.current_balance = newreceiverbalance
        sender.save()
        receiver.save()
        Transfer.objects.create(sender=sender, receiver=receiver, amount=amount)
        return redirect('/view_customers')
    else:
        customers = Customer.objects.all()
        context = {'customers': customers}
        return render(request, 'transfer_money.html', context)
    
    # sender_id = request.POST['sender']
    #     receiver_id = request.POST['receiver']
    #     amount = request.POST['amount']
    #     sender = Customer.objects.get(id=sender_id)
    #     receiver = Customer.objects.get( id=receiver_id)
    #     sender.current_balance -= amount
    #     receiver.current_balance += amount
    #     sender.save()
    #     receiver.save()
    #     Transfer.objects.create(sender=sender, receiver=receiver, amount=amount)
    #     return redirect('/view_customers')


# Create your views here.
