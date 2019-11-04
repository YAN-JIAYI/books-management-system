from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def home(request):
    return render(request, 'home.html')


# 出版社相关函数
def add_publish(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        addr = request.POST.get('addr')

        if name:
            models.Publish.objects.create(name=name, addr=addr)
            return redirect('/publish_list')
            # return redirect("/publish_list")
        return '出版社不能为空'
    return render(request, 'add_publish.html')


def publish_list(request):
    publish_queryset = models.Publish.objects.all()
    return render(request, 'publish_list.html', locals())


def del_publish(request):
    del_id = request.GET.get('del_id')
    models.Publish.objects.filter(pk=del_id).delete()
    return redirect('/publish_list')


def edit_publish(request):
    edit_id = request.GET.get('edit_id')
    if request.method == "POST":
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        models.Publish.objects.filter(pk=edit_id).update(name=name, addr=addr)
        return redirect('/publish_list')
    edit_obj = models.Publish.objects.filter(pk=edit_id).first()
    return render(request, 'edit_publish.html', locals())


# 书籍相关函数
def add_book(request):
    author_queryset = models.Author.objects.all()
    publish_queryset = models.Publish.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish')
        author_list = request.POST.getlist('author')
        # for author_name in author_list:
        #         #     author_obj = models.Author.objects.filter(name=author_name)
        #         #     print(author_obj)
        #         # print(author_list)
        if title:
            # publish_obj = models.Publish.objects.filter(name=publish).first()  #res是个对象
            models.Book.objects.create(title=title, price=price, publish_id=publish_id)
            book_obj = models.Book.objects.filter(title=title).first()
            book_obj.author.add(*author_list)
            # book_obj.author.add(author_obj)
        # return HttpResponse(f'{title}添加成功')
        return redirect('/book_list')
    return render(request, 'add_book.html', locals())


def book_list(request):
    book_queryset = models.Book.objects.all()
    author_queryset = models.Author.objects.all()
    publish_queryset = models.Publish.objects.all()
    return render(request, 'book_list.html', locals())


def edit_book(request):
    book_queryset = models.Book.objects.all()
    author_queryset = models.Author.objects.all()
    publish_queryset = models.Publish.objects.all()
    edit_id = request.GET.get('edit_id')
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish')
        author_list = request.POST.getlist('author')
        models.Book.objects.filter(pk=edit_id).update(title=title, price=price, publish=publish_id)
        edit_obj.author.set(author_list)
        return redirect('/book_list', locals())
    return render(request, 'edit_book.html', locals())


def del_book(request):
    del_id = request.GET.get('del_id')
    models.Book.objects.filter(pk=del_id).delete()
    return redirect('/book_list')



# 作者相关函数
def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        new_phone = request.POST.get('phone')  # 获取手机号
        models.AuthorDetail.objects.create(phone=new_phone)  # 存入数据库
        AuthorDetai_obj = models.AuthorDetail.objects.filter(phone=new_phone).first()
        # models.Author.objects.filter(name=name).values('phone')
        models.Author.objects.create(name=name, author_detail=AuthorDetai_obj)
        # return HttpResponse('作者添加成功')
        return redirect("/author_list")
    return render(request, 'add_author.html')


def author_list(request):
    author_queryset = models.Author.objects.all()
    return render(request, 'author_list.html', locals())


def edit_author(request):
    author_queryset = models.Author.objects.all()
    detail_queryset = models.AuthorDetail.objects.all()
    edit_id = request.GET.get('edit_id')
    edit_obj = models.Author.objects.filter(pk=edit_id).first()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        print(phone)
        AuthorDetail_obj = models.AuthorDetail.objects.create(phone=phone)
        print(AuthorDetail_obj)
        models.Author.objects.filter(pk=edit_id).update(name=name, author_detail=AuthorDetail_obj)
        return redirect('/author_list', locals())
    return render(request, 'edit_author.html', locals())

def del_author(request):
    del_id = request.GET.get('del_id')
    models.Author.objects.filter(pk=del_id).delete()
    return redirect('/author_list')


#结束页
def end(request):
    return render(request, 'end.html')
