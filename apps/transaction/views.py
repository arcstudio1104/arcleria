from iamport import Iamport
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from apps.art.models import Picture

User = get_user_model()
iamport = Iamport(imp_key=settings.IAMPORT_API_KEY, imp_secret=settings.IAMPORT_API_SECRET)


@login_required
def cash_payment(request, pk):
    picture = get_object_or_404(Picture, id=pk)
    amount = picture.price
    context = {'amount': amount, 'object': picture}
    return render(request, 'transaction/transaction_ing.html', context)


@login_required
def cash_payment_done(request, pk):
    picture = get_object_or_404(Picture, id=pk)
    user = get_object_or_404(User, email=request.user)
    amount = picture.price
    check = request.GET['imp_uid']  # URL 에서 파라미터 가져오기
    response = iamport.find(imp_uid=check)  # 아임포트 uid 값으로 거래 내역 가져오기
    response_pay = iamport.is_paid(int(amount), response=response)  # 결제 해야하는 금액과 실제 결제된 금액이 같은지 확인 True, False 리턴

    if response_pay:
        # 결제 완료

        # 컨텍스트에 데이터 삽입
        context = {'amount': amount}
        return render(request, 'transaction/transaction_done.html', context)  # 리프레쉬 시키기
    else:
        return redirect('404')  # 충전 값과 실제 결제액이 다름, 변조 의심