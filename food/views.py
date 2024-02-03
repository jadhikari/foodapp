from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
#models loaader
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    

    context={
            'item_list': item_list ,
    }

    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse('this is the items list ')


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={
            'item': item ,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('food:index')  # Redirect to the desired URL after successful form submission
    else:
        form = ItemForm()

    context = {'form': form}
    return render(request, 'food/item-form.html', context)

def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('food:index')  # Redirect to the desired URL after successful form submission
    else:
        form = ItemForm(instance=item)

    context = {'form': form, 'item': item}
    return render(request, 'food/item-form.html', context)

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        
        if item:
            item.delete()
            return redirect('food:index')
        else:
            return HttpResponse(status=404)
    else:
        return render(request, 'food/delete-item.html')
