from rest_framework import routers

from books.views import BooksView

router = routers.SimpleRouter()
router.register(r'books', BooksView)
urlpatterns = router.urls