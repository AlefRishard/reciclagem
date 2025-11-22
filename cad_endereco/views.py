from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Endereco # Importamos o MODEL, não o Form

@login_required
def cad_endereco(request):
    return render(request, 'cad_endereco/cad_endereco.html')

def criar_endereco(request):
    # Lógica para quando o utilizador clica em "Cadastrar"
    if request.method == 'POST':
        
        # 1. Pegamos os dados "na mão" direto dos inputs do HTML
        cep_input = request.POST.get('cep')
        cidade_input = request.POST.get('cidade')
        bairro_input = request.POST.get('bairro')
        rua_input = request.POST.get('rua')
        numero_input = request.POST.get('numero')

        # Validação: Não deixa salvar se faltar o básico
        if not rua_input or not numero_input:
            messages.error(request, "Rua e Número são obrigatórios.")
            return render(request, 'cad_endereco/cad_endereco.html')

        try:
            # 2. Criamos o objeto na memória (sem forms.py)
            novo_endereco = Endereco(
                cep=cep_input,
                cidade=cidade_input,
                bairro=bairro_input,
                rua=rua_input,
                numero=numero_input
            )

            # 3. Salvamos no banco
            # O .save() vai acionar o models.py, criar o Ponto e buscar o mapa automaticamente
            novo_endereco.save()

            messages.success(request, "Endereço cadastrado e geolocalizado com sucesso!")
            return redirect('index') 

        except Exception as e:
            messages.error(request, f"Erro técnico ao salvar: {e}")
            return render(request, 'cad_endereco/cad_endereco.html')
    
    # Se for apenas acesso à página (GET)
    return render(request, 'cad_endereco/cad_endereco.html')