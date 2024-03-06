from django.shortcuts import render


def home_cont(requests):
    return render(requests,'catalog/home.html')


def contacts_cont(requests):

    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')

        print(f'name -> {name}\n '
              f'phone -> {phone}\n'
              f'message -> {message}\n')

    return render(requests, 'catalog/contacts.html')