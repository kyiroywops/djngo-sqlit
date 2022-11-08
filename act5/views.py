from django.shortcuts import render, redirect
import act5.modelo.users as model

def inicio(request):
    return render(request, "index.html")

def listar(request):
    lista = model.listar()   
    dict={
        "total": len(lista),
        "usuarios": lista
    }
    return render(request, "listar.html", dict)

def eliminar(request,rut):
    usu=busca(rut)
    usu.eliminar()
    return redirect(listar)

##
def busca(rut):
    u = model.Usuario()
    u.Rut = rut
    u.buscar()
    if u.Rut is None:
        print("Usuario no encontrado.")
    else:
        print(u)
    return u

def modificar(request,rut):
    return render(request, "index.html")

def agregar(request):
    return render(request, "index.html")
