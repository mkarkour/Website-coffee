### Ce code a été crée par mehdi karkour ###
from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from datetime import datetime
from blog.models import User, Livre


def login(request):
    #b=Block.objects.all()
    current_datetime = datetime.now()
    if 'email' in request.GET and 'password' in request.GET :
        entered_email=request.GET['email']
        entered_password=request.GET['password']
        if len(User.objects.filter(email=entered_email).filter(password=entered_password))==1:
            # if len(b.filter(blocked=User.objects.get(email=entered_email)))==0:
            request.session['email'] = request.GET['email']
            return redirect('/homepage')
            # else:
            #     dico = {'error': 'Vous avez été bloqué pour abus et corruption.','datetime':current_datetime}
            # return render(request, 'login.html', dico)
        else:
            dico = {'error': 'Bad login or password.','datetime':current_datetime}
            return render(request, 'login.html', dico)
    else:
        dico = {'datetime':current_datetime}
        response = render(request,'login.html',dico)
        return response

def registration(request):
    a=User.objects.all()
    if 'email' in request.GET:
        e=[]
        for u in a:
            e.append(u.email)
        if request.GET['email']not in e:   
            newUser = User(firstname=request.GET['firstname'],
                          lastname=request.GET['lastname'], 
                          email=request.GET['email'], 
                          password=request.GET['password'],
                          gender=request.GET['gender'],
                          )
            newUser.save()
            return redirect('/login')
        else:
            return render (request,'registration.html',{'error':"l'email rentré existe déjà, appelé le service technique"})
    else: 
        return render(request,'registration.html')

def homepage(request):
    u1=User.objects.get(email=request.session['email'])
    utilisateur_now=u1.firstname
    dico={'user':utilisateur_now}
    score=0
    
    return render(request,'homepage.html',dico)

def logout(request):
    del request.session['email']
    return redirect ('/login')

def Welcome (request):
    heure=datetime.now()
    dico={'datetime':heure}
    return render (request,'accueil.html', dico)

def add (request):
    l=Livre.objects.all()
    num=randint(1,1000)
    list=[]
    for e in l:
        list.append(e.id_livre)
    if num in list:
        num=randint(1,1000)
        if num in list:
            num=randint(1,1000)
            if num in list:
                num=randint(1001,10000)
    if 'titre' in request.GET:
            newLivre = Livre(titre=request.GET['titre'],
                            auteur=request.GET['auteur'],
                            categorie=request.GET['categorie'],
                            id_livre=num,
                            )
            newLivre.save()

            dico={"success":"Bien enregistrez !"}
            return render (request,'add_livre.html',dico)
    else:
        return render (request,'add_livre.html')

def bibliotheque (request):
    u1=User.objects.get(email=request.session['email'])
    b=Livre.objects.all()
    dico={"b":b}
    return render (request,'biblio.html',dico)

def blackjack (request):
    u1=User.objects.get(email=request.session['email'])
    jeux=0
    cagnotte=0
    nb=" par soucis de faciliter, les figures ne sont pas represente, une dame, un valet, un roi ont comme valeur dix et cela suffit au jeux"
    while jeux<1:
        b_tot=0
        j_tot=0
        mise=input("votre mise ? :")
        mise=int(mise)
        paquet=["AS",2,3,4,5,6,7,8,9,10,10,10,10]  #11 est le valet, 12 est la dame, 13 est le roi et 1: l'as
        b_carte=randint(0,12)
        b_carte2=randint(0,12)
        banque=paquet[b_carte]
        banque2=paquet[b_carte2]
        j_carte=randint(0,12)
        j_carte2=randint(0,12)
        joueur=paquet[j_carte]
        joueur2=paquet[j_carte2]
        figure=["Valet","Dame","Roi"]
        print("le croupier a comme carte",banque,", et ? (face caché)")
        print("vos cartes sont,",joueur,"et", joueur2)

    if joueur=="AS" or joueur2=="AS":
        As=input("l'as vaut 1 ou 11 ? :")
        As=int(As)
        if joueur=="AS":
            joueur=As
        elif joueur2=="AS":
            joueur2=As
        else:
            As2=input("l'as vaut 1 ou 11 ?:")
            As2=int(As2)
            joueur=As
            joueur2=As2
            
    if banque=="AS" or banque2=="AS":
        if banque=="AS":
            if banque2==1 or banque2==2 or banque2==3 or banque2==4 or banque2==5 or banque2==6 or banque2==7 or banque2==8 or banque2==9 or banque2==10:
                banque=11
            else:
                banque=1
        elif banque2=="AS":
            if banque==1 or banque==2 or banque==3 or banque==4 or banque==5 or banque==6 or banque==7 or banque==8 or banque==9 or banque==10:
                banque2=11
            else:
                banque2=1
        else:
            banque=1
            banque2=11
                
    j_tot=joueur+joueur2
    b_tot=banque+banque2
    i=0
    while i<4:
        reprise=input("voulez vous reprendre une carte ? :")
        if reprise=="oui":
            j_carte3=randint(0,12)
            joueur3=paquet[j_carte3]
            j_tot+=joueur3
            if j_tot>21:
                print("votre nouvelle carte est",joueur3)
                i=4
            elif joueur3==11:
                i+=1
                print("votre nouvelle carte est un valet")
            elif joueur3==12:
                i+=1
                print("votre nouvelle carte est une dame")
            elif joueur3==13:
                i+=1
                print("votre nouvelle carte est un roi")
            else:
                i+=1
                print(" votre nouvelle carte est",joueur3)
        else:
            i+=4
            print("les cartes du croupier sont", banque,"et",banque2)
    if j_tot<=21:
        if b_tot<j_tot and b_tot<21:
            a=0
            while b_tot<j_tot and b_tot<21:
                b_carte3=randint(0,12)
                banque3=paquet[b_carte3]
                print("le croupier tire le",banque3)
                if banque3=="AS":
                    if b_tot>10:
                        banque3=1
                    else:
                        banque3=11
                b_tot+=banque3
                a+=1
                
            if b_tot>21:
                gain=mise*2
                print("vous gagnez",gain)
            elif b_tot>j_tot and b_tot<21:
                gain=0
                print("vous gagnez",gain)
            elif b_tot==21:
                print("BLACKJACK, le croupier gagne")
            else:
                gain=mise*2
                print("vous gagnez", gain)
        elif b_tot>21:
            gain=mise*2
            print("vous gagnez",gain)
        elif b_tot==21:
            gain=0
            print("vous gagnez",gain)
        elif b_tot>j_tot and b_tot<21:
            gain=0
            print("vous gagnez",gain)
        elif j_tot==21:
            gain=mise*2.5
            print("BLACKJACK,dans ta mère le croupier, vous gagnez",gain)
        elif j_tot>21:
            gain=0
            print("vous gagnez",gain)
        elif j_tot==b_tot:
            gain=mise
            print("égalité!, vous récupérer votre mise")
        else:
            gain=0
            print("vous gagnez",gain)
    else:
        gain=0
        print("vous avez dépassé, votre gain est de",gain)

    cagnotte+=gain
    print("votre cagnotte est de",cagnotte)
    jeux=input("désirez-vous rejouer ? :")
    if jeux=="oui" or jeux=="yes" or jeux=="Oui" or jeux=="Yes":
        jeux=0
    else:
        jeux=1
    return render (request,'bj.html')




