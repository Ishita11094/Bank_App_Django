from django.shortcuts import render
from .forms import CreateForm, TransactionForm
from .models import CreateModel, TransactionModel

def home(request):
	return render(request, "home.html")

def create(request):
	if request.method == "POST":
		f = CreateForm(request.POST)
		if f.is_valid():
			f.save()
			fm = CreateForm()
			return render(request, "create.html", {'fm':fm, 'msg':'User Created Successfully'})
	else:
		fm = CreateForm()
		return render(request, "create.html", {'fm':fm})

def transfer(request):
	if request.method == "POST":
		f = TransactionForm(request.POST)
		s = request.POST.get('sender')
		r = request.POST.get('receiver')
		a = request.POST.get('amount')
		a = int(a)
		data = CreateModel.objects.all()
		
		if a==0:
			fm = TransactionForm()
			return render(request, "transfer.html", {'fm':fm, 'msg':'Amount cannot be 0'})	
		
		if CreateModel.objects.filter(name=s).exists() and CreateModel.objects.filter(name=r).exists():

			if s==r:
				fm = TransactionForm()
				return render(request, "transfer.html", {'fm':fm, 'msg':'Sender and receiver cannot be same'})	
		
			for d in data:
				if d.name == s:
					if a<d.balance:
						d.balance = d.balance - a
						d.save()
					else:
						fm = TransactionForm()
						return render(request, "transfer.html", {'fm':fm, 'msg':'Sender does not have that much balance'})

			for d in data:
				if d.name == r:
					d.balance = d.balance + a
					d.save()

			if f.is_valid():
				f.save()
				fm = TransactionForm()
				return render(request, "transfer.html", {'fm':fm, 'msg':'Amount transferred'})

		else:
			fm = TransactionForm()
			return render(request, "transfer.html", {'fm':fm, 'msg':'Enter registered user names only'})		

	else:
		fm = TransactionForm()
		return render(request, "transfer.html", {'fm':fm})

def view_acc(request):
	data = CreateModel.objects.all()
	return render(request, "view_acc.html", {"data":data})

def history(request):
	data = TransactionModel.objects.all()
	return render(request, "history.html", {"data":data})


