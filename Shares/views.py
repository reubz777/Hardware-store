from idlelib.rpc import request_queue

from django.shortcuts import render, get_object_or_404, redirect
from .models import Shares
# Create your views here.


def promotion_on_goods(request):
    shares = Shares.objects.all()
    status = request.GET.get('status')

    if status:
        shares = shares.filter(status = status)

    return render(
        request,
        "shares/promotions-on-goods.html",
        {'shares': shares}
    )

def shares_info(request, shares_id):
    share = get_object_or_404(Shares, id=shares_id)
    share.views +=1
    share.save()
    return render(request, "shares/shares-info.html")


def increment_view(request, shares_id):
    if request.method == "POST":
        share = get_object_or_404(Shares, id=shares_id)
        share.views += 1
        share.save()
        return redirect('promotion-on-goods')