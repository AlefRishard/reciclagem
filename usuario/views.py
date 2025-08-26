# Em usuario/views.py


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, get_user_model

# Pega o modelo de usuário que está ativo no projeto (o seu 'Usuario' customizado)
User = get_user_model()





def cadastrar(request):
    if request.method == 'POST':
        # Pega os campos do formulário
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        senha1 = request.POST.get('password')
        senha2 = request.POST.get('password2')

        # Verificar verifica se as senhas são iguais
        if senha1 != senha2:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('cadastrar') #Volta para tela de cadastro

        # Verifica se o email existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já foi cadastrado.')
            return redirect('cadastrar')

        # Criar o usuário
        user = User.objects.create_user(
            username=email, 
            email=email,
            password=senha1
        )
        user.cpf = cpf
        user.save()
        
        messages.success(request, 'Cadastro realizado com sucesso! Faça o login.')
        return redirect('login')
    
    # apenas mostra a tela de cadastro
    return render(request, 'usuario/cadastro.html')


def login_view(request):
    if request.method == 'POST':
        
        email_como_username = request.POST.get('email')
        senha = request.POST.get('password')

        if not email_como_username or not senha:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('login')

    
        user = authenticate(request, username=email_como_username, password=senha)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
            return redirect('login')

    return render(request, 'usuario/login.html') #mostra a tela de login