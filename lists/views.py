from django.shortcuts import redirect, render
from lists.models import Item
#from django.http import HttpResponse

def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'home.html')
#
#        new_item_text = request.POST['item_text']
#        Item.objects.create(text=new_item_text)
#    else:
#        new_item_text = ''
#
#    return render(request, 'home.html', {
#        'new_item_text': new_item_text,
#    })
    
#    if request.method == 'POST':
#        return HttpResponse(request.POST['item_text'])
#    return render(request, 'home.html')
