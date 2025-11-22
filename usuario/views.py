# Em usuario/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, get_user_model

User = get_user_model()


def cadastro_usuario(request):

    return render(request, 'usuario/cadastro.html')


def cadastrar(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')
        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')


        # validações
        if password != password2:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('cadastrar')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
            return redirect('cadastrar')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já foi cadastrado.')
            return redirect('cadastrar')

        # criação de usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.cpf = cpf
        user.cep = cep
        user.bairro = bairro
        user.rua = rua
        user.numero = numero
        user.save()
        
        messages.success(request, 'Cadastro realizado com sucesso! Faça o login.')
        return redirect('login')
    
    return render(request, 'usuario/cadastro.html')


def login_view(request):
    if request.method == 'POST':
        email_form = request.POST.get('email')
        password_form = request.POST.get('password')

        try:
            user_to_auth = User.objects.get(email=email_form)
        except User.DoesNotExist:
            messages.error(request, "Nenhum usuário encontrado com este e-mail.")
            return redirect('login')

        user = authenticate(
            request,
            username=user_to_auth.username,
            password=password_form
        )

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Senha incorreta.")
            return redirect('login')

    return render(request, 'usuario/login.html')