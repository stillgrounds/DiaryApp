from django.shortcuts import redirect, render
from .models import Diary
from .forms import updateform
# Create your views here.

def index(request):
    if request.method == 'POST':
        diary = request.POST['ediary']
        create = Diary(text=diary)

        create.save()
        return redirect('showdiary')
    return render(request,'mydiary/index.html')

#show all diary entries
def showdiary(request):
    # show = Diary.objects.all()
    show = Diary.objects.order_by('-date_created')
    context={
        'show':show
    }
    return render(request,'mydiary/showdiary.html',context)

# retrieve single data
def singlediary(request,id):
    getsingle = Diary.objects.get(id=id)
    context={
        'show':getsingle
    }
    return render(request,'mydiary/singlediary.html',context)

# updatedata
def updatediary(request,id):
    getsingle = Diary.objects.get(id=id)
    form = updateform(request.POST or None, instance=getsingle)
    if form.is_valid():
        form.save()

        return redirect('showdiary')

    context={
        'show':getsingle,
        'form':form
    }
    return render(request, 'mydiary/updatediary.html',context)

# deletedata
def deletediary(request,id):
    getsingle = Diary.objects.get(id=id)
    getsingle.delete()
    return redirect('showdiary')




