from aiohttp import request
from django import urls
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    return render(request,'login.html')

def send(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    username = usr
    room_id = request.POST['room_id']
    message = request.POST['message']
    new_message = Private_Message.objects.create(Message = message, User = username, Room = room_id)
    new_message.save()
    return redirect('/chat_mp/'+room_id)

def chat_mp(request, room):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    messages = Private_Message.objects.filter(Room = room)
    context = {
        'usr': usr,
        'room': room,
        'messages': messages,
    }
    return render(request,'chat_mp.html',context)

def chat(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    Ast = Message.objects.filter(User_send_msg = usr)
    context = {
        'usr': usr,
        'Ast': Ast,
    }
    return render(request,'chat.html',context)

def assistance(request):
    msg = Message.objects.all()
    ptc = Assistance.objects.all()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'msg': msg,
        'usr': usr,
        'ptc': ptc,
    }
    return render(request,'messagerie.html',context)

def send_msg(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    user_send_msg = usr
    object_msg = request.POST['Object_msg']
    content_msg = request.POST['Content_msg']
    statut_msg = 'Non pris en charge'
    create_send_msg = Message(User_send_msg = user_send_msg, Object_msg = object_msg, Content_msg = content_msg, Status_msg = statut_msg)
    create_send_msg.save()
    theme = object_msg
    create_room = Room(Theme = theme)
    create_room.save()
    
    return redirect('/manage_stress_app')

def profil(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    pub = News_Post.objects.filter(Auteur_pub = usr)
    context = {
        'usr': usr,
        'pub': pub,
    }
    return render(request,'profil.html',context)

def cas(request,id):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    name = usr.Nom_Complet
    msg = Message.objects.get(pk=id)
    msg.Status_msg = 'Pris en charge'
    msg.save()
    create_assistance = Assistance(Cas = msg, Suivi = usr)
    create_assistance.save()
    return redirect('/assistance')

def non_cas(request,id):
    msg = Message.objects.get(pk=id)
    msg.Status_msg = 'Non pris en charge'
    msg.save()
    assistance = Assistance.objects.get(Cas = msg)
    assistance.delete()
    return redirect('/assistance')
    
def profil_user(request,id):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    ustr = Utilisateur.objects.get(Nom_Complet = id)
    pub = News_Post.objects.filter(Auteur_pub = ustr)
    context = {
        'usr': usr,
        'pub': pub,
        'ustr': ustr,
    }
    return render(request,'profil_user.html',context)
    

def create_comment(request,id):
    post = News_Post.objects.get(pk=id)
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    titre_pub = post.Titre
    comment_pub = request.GET['comment']
    auteur_comment_pub = usr.Nom_Complet
    create_comment = Commentaires(Titre_pub = titre_pub, Auteur_Comment_pub = usr, Comment_pub = comment_pub)
    create_comment.save()
    cmt = Commentaires.objects.filter(Titre_pub = titre_pub)
    cpt = Commentaires.objects.count()
    # usr_comment = Utilisateur.objects.get(Nom_Complet = auteur_comment_pub)
    context = {
        'post': post,
        'titre_pub': titre_pub,
        'usr': usr,
        'cmt': cmt,
        'cpt': cpt,
    }
    return render(request,'pub.html',context)

def login(request):
    uname = request.POST.get('Username')
    pwd = request.POST.get('Password')
    check_user = Utilisateur.objects.filter(Username = uname, Password = pwd)
    if check_user:
        usr = Utilisateur.objects.get(Username = uname, Password = pwd)
        if usr.Status == 'Administrateur':
            request.session['user'] = uname
            return redirect('/index_admin')
        if usr.Status == 'Psychologue':
            request.session['user'] = uname
            return redirect('/index_app')
        else:
            request.session['user'] = uname
            return redirect('index_app')
        
    else:
        return render(request,'login_notif.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/')
    return redirect('/')

def index_app(request):
    NP = News_Post.objects.order_by('Date_pub').reverse()[:3]
    MS = Manage_Stress.objects.order_by('Date_pub_MS').reverse()[:3]
    RS = Ressources.objects.order_by('Date_pub_Ressource').reverse()[:3]
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'NP': NP,
        'MS': MS,
        'RS': RS,
        'usr': usr,
    }
    return render(request,'index_app.html',context)

def ressource_app(request):
    Ressource = Ressources.objects.order_by('Date_pub_Ressource').reverse()
    usr = Utilisateur.objects.filter(Status = 'Psychologue')
    ust = request.session['user']
    ustr = Utilisateur.objects.get(Username = ust)
    context = {
        'Ressource': Ressource,
        'usr': usr, 
        'ustr': ustr,
    }
    return render(request,'ressource_app.html',context)

def manage_stress_app(request):
    MS = Manage_Stress.objects.order_by('Date_pub_MS').reverse()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'MS': MS,
        'usr': usr,
    }
    return render(request,'manage_stress_app.html',context)

def journal_app(request):
    pst = News_Post.objects.filter(Type = 'Posts').order_by('Date_pub').reverse()
    nws = News_Post.objects.filter(Type = 'News').order_by('Date_pub').reverse()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    
    context = {
        'pst': pst,
        'nws': nws,
        'usr': usr,
    }
    return render(request,'journal_app.html',context)

def like_post(request, id):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    post = News_Post.objects.get(pk=id)
    pst = post.Titre
    reaction = usr
    if News_Post.objects.filter(Titre = pst, Like = reaction).exists():
        post.Like.remove(reaction)
    else:
        post.Like.add(reaction)
        
    return redirect('/journal_app')
    

def pub_post_user(request):
    titre = request.POST['Titre']
    contenu = request.POST['Contenu']
    type = 'Posts'
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    auteur_pub = usr.Nom_Complet
    fichier = request.FILES.get('Fichier')
    if fichier != None:
        create_np = News_Post(Titre = titre, Contenu = contenu, Type = type, Fichier = fichier)
        create_np.save()
    else:
        create_np = News_Post(Titre = titre, Contenu = contenu, Type = type)
        create_np.save()
    return redirect('/journal_app')

def details_pub(request,id):
    post = News_Post.objects.get(pk=id)
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    cmt = Commentaires.objects.filter(Titre_pub = post.Titre)
    cpt = Commentaires.objects.filter(Titre_pub = post.Titre).count()
    context = {
        'post': post,
        'usr': usr,
        'cmt':cmt,
        'cpt': cpt,
    }
    return render(request,'pub.html',context)

def index_admin(request):
    user_S = Utilisateur.objects.filter(Status = "Utilisateur Simple").count()
    user_P = Utilisateur.objects.filter(Status = "Psychologue").count()
    nbr_MS = Manage_Stress.objects.count()
    nbr_RS = Ressources.objects.count()
    nbr_NP = News_Post.objects.count()
    nbr_msg = Message.objects.count()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'user_S' : user_S,
        'user_P' : user_P,
        'nbr_MS' : nbr_MS,
        'nbr_RS' : nbr_RS,
        'nbr_NP': nbr_NP,
        'usr': usr,
        'nbr_msg': nbr_msg,
    }
    return render(request,'index_admin.html',context)

def manage_stress_admin(request):
    MS = Manage_Stress.objects.all()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'MS' : MS,
        'usr': usr,
    }
    return render(request,'manage_stress_admin.html',context)

def add_manage_stress_admin(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'usr': usr,
    }
    return render(request,'add_manage_stress_admin.html',context)

def edit_manage_stress_admin(request,id):
    MS = Manage_Stress.objects.get(pk=id)
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'MS' : MS,
        'usr': usr,
    }
    return render(request,'edit_manage_stress_admin.html',context)

def delete_manage_stress_admin(request,id):
    MS = Manage_Stress.objects.get(pk=id)
    MS.delete()
    return redirect('/manage_stress_admin')

def create_manage_stress_admin(request):
    print(request.POST)
    titre_MS = request.POST['Titre_MS']
    description_MS = request.POST['Description_MS']
    fichier_MS = request.FILES.get('Fichier_MS')
    create_MS = Manage_Stress(Titre_MS = titre_MS, Description_MS = description_MS, Fichier_MS = fichier_MS)
    create_MS.save()
    return redirect('/manage_stress_admin')

def update_manage_stress_admin(request,id):
    update_MS = Manage_Stress.objects.get(pk=id)
    update_MS.Titre_MS = request.GET['Titre_MS']
    update_MS.Description_MS = request.GET['Description_MS']
    update_MS.Fichier_MS = request.FILES.get('Fichier_MS')
    update_MS.save()
    return redirect('/manage_stress_admin')
    
def ressources_admin(request):
    Src = Ressources.objects.all()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'Src' : Src, 
        'usr': usr,
    }
    return render(request,'ressources_admin.html',context)

def add_ressource_admin(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'usr': usr,
    }
    return render(request,'add_ressource_admin.html',context)

def edit_ressource_admin(request,id):
    Src = Ressources.objects.get(pk=id)
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'Src' : Src,
        'usr': usr,
    }
    return render(request,'edit_ressource_admin.html',context)

def delete_ressource_admin(request,id):
    Src = Ressources.objects.get(pk=id)
    Src.delete()
    return redirect('/ressources_admin')

def create_ressource_admin(request):
    #print(request.POST)
    Titre_R = request.POST['Titre_Ressource']
    Description_R = request.POST['Description_Ressource']
    Fichier_R = request.FILES.get('Fichier_Ressource')
    create_R = Ressources(Titre_Ressource = Titre_R, Description_Ressource = Description_R, Fichier_Ressource = Fichier_R)
    create_R.save()
    return redirect('/ressources_admin')

def update_ressource_admin(request,id):
    update_R = Ressources.objects.get(pk=id)
    update_R.Titre_Ressource = request.GET['Titre_Ressource']
    update_R.Description_R = request.GET['Description_Ressource']
    update_R.Fichier_R = request.FILES.get('Fichier_Ressource')
    update_R.save()
    return redirect('/ressources_admin')

def user_admin(request):
    Users = Utilisateur.objects.all()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'Users' : Users,
        'usr': usr,
    }
    return render(request,'user_admin.html',context)

def add_user_admin(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'usr': usr,
    }
    return render(request,'add_user_admin.html',context)

def create_user_admin(request):

    nom = request.POST['Nom']
    prenom = request.POST['Prenom']
    age= request.POST['Age']
    email = request.POST['Email']
    departement = request.POST['Departement']
    Fonction = request.POST['Fonction']
    username = request.POST['Username']
    password = request.POST['Password']
    status = request.POST['Status']
    image_profile = request.FILES.get('Image_Profil')
    create_user = Utilisateur(Image_profil = image_profile, Nom = nom, Prenom = prenom, Age = age, Email = email, Departement = departement, Fonction = Fonction, Username = username, Password = password, Status = status)
    create_user.save()
    return redirect('/user_admin')

def update_user_app(request, id):
    create_user_app_edit = Utilisateur.objects.get(pk=id)
    create_user_app_edit.Nom_Complet = request.POST['Nom']
    create_user_app_edit.Departement = request.POST['Departement']
    create_user_app_edit.Email = request.POST['Email']
    create_user_app_edit.Age = request.POST['Age']
    create_user_app_edit.Fonction = request.POST['Fonction']
    # create_user_app_edit.Image_profil = request.FILES.get('Image_profil')
    create_user_app_edit.Username = request.POST['Username']
    create_user_app_edit.Password = request.POST['Password']
    create_user_app_edit.save()
    return redirect('/logout')
    
def edit_user_admin(request, id):
    Users_e = Utilisateur.objects.get(pk=id)
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'Users_e' : Users_e,
        'usr': usr,
    }
    return render(request,'edit_user_admin.html',context)

def update_user_admin(request, id):
    create_user_edit = Utilisateur.objects.get(pk=id)
    create_user_edit.Nom_Complet = request.POST['Nom']
    create_user_edit.Departement = request.POST['Departement']
    create_user_edit.Email = request.POST['Email']
    create_user_edit.Age = request.POST['Age']
    create_user_edit.Fonction = request.POST['Fonction']
    create_user_edit.Status = request.POST['Status']
    create_user_edit.Image_profil = request.FILES.get('Image_profil')
    create_user_edit.Username = request.POST['Username']
    create_user_edit.Password = request.POST['Password']
    create_user_edit.save()
    return redirect('/user_admin')

def delete_user_admin(request,id):
    Users = Utilisateur.objects.get(pk=id)
    Users.delete()
    return redirect('/user_admin')

def news_post_admin(request):
    News_Posts = News_Post.objects.all()
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'News_Posts' : News_Posts,
        'usr': usr,
    }
    return render(request,'news_post.html',context)

def add_news_post_admin(request):
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'usr': usr,
    }
    return render(request,'add_news_post.html',context)

def create_news_post_admin(request):
    #print(request.POST, request.FILES)
    titre = request.POST['Titre']
    contenu = request.POST['Contenu']
    type = request.POST['Type']
    fichier = request.FILES.get('Fichier')
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    create_np = News_Post(Titre = titre, Contenu = contenu, Type = type, Fichier = fichier, Auteur_pub = usr)
    create_np.save()
        
    return redirect('/news_post_admin')

def edit_news_post_admin(request, id):
    NP = News_Post.objects.get(pk=id)
    ust = request.session['user']
    usr = Utilisateur.objects.get(Username = ust)
    context = {
        'NP' : NP,
        'usr': usr,
    }
    return render(request,'edit_news_post.html',context)

def update_news_post_admin(request, id):
    update_NP = News_Post.objects.get(pk=id)
    update_NP.Titre = request.GET['Titre']
    update_NP.Contenu = request.GET['Contenu']
    update_NP.Type = request.GET['Type']
    update_NP.Fichier = request.FILES.get('Fichier')
    update_NP.save()
    return redirect('/news_post_admin')

def delete_news_post_admin(request, id):
    delete_NP = News_Post.objects.get(pk=id)
    delete_NP.delete()
    return redirect('/news_post_admin')
