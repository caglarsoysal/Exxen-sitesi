import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import string
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userRegister (request):
    if request.method == 'POST':
        kullanici = request.POST ['kullanici']
        email = request.POST['email']
        sifre = request.POST['sifre']
        sifre2 = request.POST['sifre2']

        if kullanici != '' and email != '' and sifre != '':
            if sifre == sifre2:
                #  username in var olup olmadıgını kontrol eder
                if User.objects.filter(username = kullanici).exists():
                    messages.error(request, 'Bu Kullanici adı Zaten Mevcut')
                    return redirect('register')
                #  emailin var olup olmadıgını kontrol eder
                elif User.objects.filter(email = email).exists():
                    messages.error(request, 'Bu Email Kullanımda')
                    return redirect('register')
                #  sifrenın uzunlugunu kontrol eder
                elif len(sifre) < 8:
                    messages.error(request, 'Şifre En Az 8 Karakter Olmalı')
                    return redirect ('register')
                #  şifrede kullanıcı adı varmı yokmu onu kontrol eder
                elif kullanici in sifre:
                    messages.error(request, 'Şifre ile Kullanici adi Benzer olamaz')
                    return redirect ('register')
                elif sifre [0] in string.ascii_lowercase:
                    messages.error(request, 'Baş Harf Büyük Olması Gerekiyor')
                    return redirect ('register')
                #  kullanıcıyı olusturur
                else: 
                    user = User.objects.create_user(username = kullanici, email = email, password = sifre )
                    user.save()
                    messages.success(request, 'Kullanici Oluşturuldu')
                    return redirect ('index')
            else:
                messages.error(request, 'Şifreler Uyuşmuyor')
                return redirect('register')
        else:
            messages.error(request, 'Tüm Alanların Doldurulması Zorunludur')
            return redirect ('register')
               
    return render (request, 'register.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre= request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya Şifre Hatalı')
            return redirect('login')
    return render (request, 'login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('index')
    