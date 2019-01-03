from rest_framework import routers
from rental import views as api_views

router = routers.DefaultRouter()
router.register(r'friends', api_views.FriendViewset)
router.register(r'belongings', api_views.BelongingViewset)
router.register(r'borrowings', api_views.BorrowedViewset)
