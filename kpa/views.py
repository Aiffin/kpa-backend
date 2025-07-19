from rest_framework import generics,filters,status
from .models import WheelSpecification
from .serializers import WheelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response



# Create your views here.

class WheelSpecificationAPIVIEW(generics.ListCreateAPIView):
    queryset=WheelSpecification.objects.all()
    serializer_class=WheelSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['formNumber', 'submittedBy', 'submittedDate']
    search_fields = ['formNumber', 'submittedBy']
    ordering_fields = ['submittedDate']
    ordering = ['submittedDate']


    def list(self, request, *args, **kwargs):
           
                queryset = self.filter_queryset(self.get_queryset())  # This applies search and ordering
                
                if queryset.count() == 0 :
                        return Response({
                                'success':False,
                                'message':'Data not presesnt',
                                'data':[],
                        },status=status.HTTP_404_NOT_FOUND)
                
                serializer = self.get_serializer(queryset, many=True)
                # print(serializer.data)
          
                # print("Requested params:", request.query_params)
                # print("Queryset before filter:", WheelSpecification.objects.count())
                # print("After filter:", queryset.count())

                return Response({
                    'success': True,
                    'message': 'Filtered wheel specification forms fetched successfully.',
                    'data': serializer.data,
                }, status=status.HTTP_200_OK)
