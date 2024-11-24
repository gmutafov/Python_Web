from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView

from todoApp.todos.models import Todo, Category
from todoApp.todos.serializers import TodoSerializer, CategorySerializer, TodoReadSerializer


class TodoListCreateApiView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()

        category = self.request.query_params.get('category')
        is_done = self.request.query_params.get('is_done')

        if category:
            queryset = queryset.filter(category__id=category)

        if is_done:
            queryset = queryset.filter(state=is_done.lower() == 'true')

        return queryset


class CategoriesListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TodoDetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoReadSerializer