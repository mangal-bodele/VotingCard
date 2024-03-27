from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import VotingCardForm
from .models import VotingCard

@login_required(login_url='login_url')
def create_votingcard(request):
    template_name = 'crud_app/create.html'
    form = VotingCardForm()
    if request.method == "POST":
        form = VotingCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request,template_name,context)
@login_required(login_url='login_url')
def show_votingcard(request):
    template_name = 'crud_app/show.html'
    votingcards = VotingCard.objects.all()
    context = {'votingcards':votingcards}
    return render(request,template_name,context)

def update_votingcard(request,pk):
    template_name = 'crud_app/create.html'
    obj = VotingCard.objects.get(id=pk)
    form = VotingCardForm(instance=obj)
    if request.method == "POST":
        form = VotingCardForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_votingcard(request, pk):
    template_name = 'crud_app/confirm.html'
    obj = VotingCard.objetcs.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request,template_name)
