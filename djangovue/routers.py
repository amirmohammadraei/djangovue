from rest_framework import routers
from catalog.viewsets import ArticleViewSet
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
