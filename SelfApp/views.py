from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from .models import Contribution
from .forms import ContributionForm

# Create your views here.
# MEMBERS
def member_list(request):
    Members = Member.objects.all()
    return render(request,'members.html',{'Members':Members})

# add
def add_member(request):
    mydict={}
    form = MemberForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form'] = form
    return render(request,'add.html',mydict)


# edit
def edit_member(request,id=None):
    one_rec=Member.objects.get(id=id)
    form = MemberForm(request.POST or None,request.FILES or None,instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})

# delete
def delete_member(request,eid=None):
    one_rec=Member.objects.get(pk=eid)
    if request.method=='POST':
        one_rec.delete()
        return redirect('/')
    return render(request,'delete.html')

# view
def view_member(request,eid=None):
    mydict={}
    one_rec=Member.objects.get(pk=eid)
    mydict['user'] =one_rec
    return render(request,'view.html',mydict)

# CONTRIBUTION
def contribution_list(request):
    Contributions = Contribution.objects.all()
    return render(request,'contribution.html',{'Contributions':Contributions})

# view
def contribution_detail(request,eid=None):
    mydict={}
    one_rec=Contribution.objects.get(pk=eid)
    mydict['user'] =one_rec
    return render(request,'contribution.html',mydict)

# add
def contribution_add(request):
    mydict={}
    form = ContributionForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form'] = form
    return render(request,'contribution.html',mydict)

# edit
def contribution_edit(request,eid=None):
    one_rec=Contribution.objects.get(pk=eid)
    form = ContributionForm(request.POST or None,request.FILES or None,instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})