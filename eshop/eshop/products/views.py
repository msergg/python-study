# coding=utf-8
from random import randint

from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .models import Comment
from .models import Product
from .forms import CommentForm, CommentModelForm

from .tasks import send_order





def index(request):


    all_products = Product.available.all()

    if 'k' not in request.session:
        request.session['k'] = randint(1000, 100000)

    if 'q' in request.GET:
        all_products = all_products.filter(name__contains=request.GET['q'])

    product = Paginator(all_products, 2).page(request.GET.get('page',1))

    return render(request, 'index.html', {
            'products' : product,
            'q':request.GET.get('q',''),
            'k':request.session['k']
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



def edit_comments(request, comment_id):
    comment = get_object_or_404(Comment, pk=int(comment_id))

    product = get_object_or_404(Product, comment=comment_id)

    form = CommentModelForm(instance=comment)

    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.id = int(comment_id)
            comment.product = product
            comment.save()
            return redirect('/products/edit/{}'.format(comment_id))

    return render(request, 'edit_comment.html', {
        'form' : form,
        'product': comment.product
    })




def order(request, product_id):
    product = get_object_or_404(Product, pk=int(product_id))

    send_order.delay(request.user.email, product.name)

    messages.info(request, 'Order was sent')
    return redirect('/products/detail/{}'.format(product_id))

