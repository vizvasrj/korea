
# Create your views here.
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import KonlpySerializer
from rest_framework.exceptions import APIException
import time
from gluonnlp.data import SentencepieceTokenizer
from .kobert import get_tokenizer
tok_path = get_tokenizer()
sp = SentencepieceTokenizer(tok_path)

class Success(APIException):
    status_code = status.HTTP_202_ACCEPTED
    default_detail = 'Success .'
    default_code = 'success'


class KonlpyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = KonlpySerializer



    def update(self, request, *args, **kwargs):
        text = request.data['text']
        start_time = time.time()
        k2 = "".join(sp(text)).split("▁")
        endtime = time.time() - start_time
        data = {'words': k2, 'time': endtime}
        raise Success(data)
    

    def get(self, request, *args, **kwargs):
        raise Success('a')

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
