from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

def valida_senha(senha1,senha2):
    if senha1 == senha2:
        return True

def valida_email(email1,email2):
    if email1 == email2:
        return True

def valida_senha(senha1,senha2):
    if senha1 == senha2:
        return True

def cadastro(request):
    if request.method == "GET":
        return render(request, "usuario/cadastro.html")
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        senha_confirm = request.POST.get('senhaconfirm')
        email = request.POST.get('email')
        email_confirm = request.POST.get('emailconfirm')
        lider_comunitario = request.POST.get('lider')
        
        user = User.objects.filter(username=usuario).first()
        if user:
            return render(request, "usuario/cadastro.html", {'error_message': 'Nome de usúario em uso'})
        
        check = User.objects.filter(email=email).first()
        if check:
            return render(request, "usuario/cadastro.html", {'error_email': 'Email já cadastrado'})
            
        if valida_senha(senha,senha_confirm) and valida_senha(email,email_confirm):
            user = User.objects.create_user(username=usuario, password=senha, email=email)
            user.save()
            if lider_comunitario:
                lider_grupo = Group.objects.filter(name="Líder Comunitário").first()
                if lider_grupo:
                    user.groups.add(lider_grupo)
            else:
                comum_grupo = Group.objects.filter(name="Comum").first()
                if comum_grupo:
                    user.groups.add(comum_grupo)                
            return render(request, "usuario/login.html", {'sucessful_message': 'Usuário cadastrado com sucesso'} )
        else:
            return render(request, "usuario/cadastro.html", {'error_email_senha': 'Os emails ou senha não conferem'})
        
        
        
            
def user_login(request):
    if request.method == "GET":
        return render(request, 'usuario/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()

        if user:
            user = authenticate(username=user.username, password=senha)
            login(request, user)
            return render(request, "home.html", {'sucessful_message': 'Usuário Logado com sucesso'} )
        else:
            lista_mensagem = {}
            lista_mensagem['mensagem_erro'] = 'E-mail ou senha inválidos'
            return render(request, 'usuario/login.html', lista_mensagem)
        
def user_logout(request):
    logout(request)
    return redirect('home')