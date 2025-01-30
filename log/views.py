from django.shortcuts import get_object_or_404, render, redirect
from .forms import BoardForm, FavoriteFrom
from .models import Board, Favorite
from django.db.models import Count
from django.db import models
from django.contrib.auth.decorators import login_required


def index(request):
    user = request.user if request.user.is_authenticated else None
    boards = Board.objects.annotate(
        is_favorite=Count("favorite", filter=models.Q(favorite__user=user))
    ).order_by("-updated_at")
    # boards = Board.objects.all().order_by("-updated_at")
    return render(request, "index.html", {"boards": boards})


def new(request):
    form = BoardForm()
    return render(request, "new.html", {"form": form})


def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log:index")
    else:
        form = BoardForm()
    return render(request, "new.html", {"form": form})


def show(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, "show.html", {"board": board})


def edit(request, pk):
    board = Board.objects.get(pk=pk)
    form = BoardForm(instance=board)
    return render(request, "edit.html", {"form": form, "board": board})


def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect("log:show", pk=pk)
    else:
        form = BoardForm(instance=board)
    return render(request, "edit.html", {"form": form, "board": board})


def delete(request, pk):
    print(f"Received pk={pk}")
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect("log:index")
    return redirect("log:index")


def board_search(request):
    query = request.GET.get("query")
    search_type = request.GET.get("search_type")
    boards = Board.objects.all()

    if search_type == "partial":
        boards = boards.filter(title__icontains=query)
    elif search_type == "prefix":
        boards = boards.filter(title__startswith=query)
    elif search_type == "suffix":
        boards = boards.filter(title__endswith=query)
    else:
        boards = boards.filter(title__icontains=query)

    return render(request, "index.html", {"boards": boards})


@login_required
def add_favorite(request):
    if request.method == "POST":
        form = FavoriteFrom(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("index")
    return redirect("index")


def remove_favorite(request):
    if request.method == "POST":
        favorite = Favorite.objects.get(
            user=request.user, board=request.POST.get("board")
        )
        favorite.delete()
        return redirect("index")
    return redirect("index")
