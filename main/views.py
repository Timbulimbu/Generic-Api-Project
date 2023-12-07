from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.response import Response
from rest_framework import status

#APIView = generics
#Create = POST
#List = GET
#Model = Contact

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['name', 'email']
    search_fields = ['name', 'email']
    

    def get_queryset(self):
        queryset = Contact.objects.all()
        search_term = self.request.query_params.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term) |\
                       queryset.filter(email__icontains=search_term) 
        return queryset

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if len(request.data.get('name', '')) < 10:
                return Response(
                    {'error': 'Имя не может быть меньше 10 символов.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                return super().post(request, *args, **kwargs)
        else:
            return Response(
                {'error': 'Вы не авторизованы.'},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    
    