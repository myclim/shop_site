from api.serializers import ProductApi, SubCategoryApi, CategoryApi
from rest_framework.generics import ListAPIView, RetrieveAPIView 
from shop.models import CategoryModel, ProductModel, SubCategoryModel



class AllProductApi(ListAPIView):

    queryset = ProductModel.objects.all()
    serializer_class = ProductApi

class DetailProductApi(RetrieveAPIView):

    serializer_class = ProductApi
    queryset = ProductModel.objects.all()


class AllCategoryApi(ListAPIView):

    serializer_class = CategoryApi
    queryset = CategoryModel.objects.all()

class DetailCategoryApi(RetrieveAPIView):

    serializer_class = CategoryApi
    queryset = CategoryModel.objects.all()


class AllSubCategoryApi(ListAPIView):

    serializer_class = SubCategoryApi
    queryset = SubCategoryModel.objects.all()

class DetailSubCategoryApi(RetrieveAPIView):

    serializer_class = SubCategoryApi
    queryset = SubCategoryModel.objects.all()

