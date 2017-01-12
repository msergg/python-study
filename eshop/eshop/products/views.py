# coding=utf-8

from django.core.paginator import Paginator
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .models import Comment
from .models import Product
from .forms import CommentForm





def index(request):


    all_products = Product.objects.all()

    if 'q' in request.GET:
        all_products = all_products.filter(name__contains=request.GET['q'])

    product = Paginator(all_products, 2).page(request.GET.get('page',1))

    return render(request, 'index.html', {
            'products' : product,
            'q':request.GET.get('q','')
    } )



def detail(request, product_id):
    # try:
    #     Product.objects.get(pk=int(product_id))
    # except:
    #     raise Http404
    product = get_object_or_404(Product, pk=int(product_id))

    comments = Comment.objects.filter(product=product)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                comment=form.cleaned_data['comment'],
                product=product,
            )

            # if ModelForm
            # comment = format.save(commit=False)
            # comment.product = product
            # comment.save()
            #
            messages.add_message(request, messages.INFO, 'Succesfully added')


            comment.save()



            return redirect('/products/detail/{}'.format(product_id))



        print(request.POST)





    return render(request, 'detail.html', {
        'product': product,
        'form': form,
        'comments': comments,
        'messages': messages.get_messages(request)
    })
