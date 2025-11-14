from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.accounts.urls import router as accounts_router
from apps.dating.urls import router as dating_router
from apps.astrology.urls import router as astrology_router
from apps.wedding.urls import router as wedding_router
from apps.finance.urls import router as finance_router
from apps.subscriptions.urls import router as subscriptions_router
from apps.chat.urls import router as chat_router

router = routers.DefaultRouter()
for r in [
    accounts_router,
    dating_router,
    astrology_router,
    wedding_router,
    finance_router,
    subscriptions_router,
    chat_router,
]:
    for prefix, viewset, basename in r.registry:
        router.register(prefix, viewset, basename=basename)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('apps.accounts.auth_urls')),
]
