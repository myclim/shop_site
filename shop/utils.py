from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from shop.models import ProductModel



def search_products(search_text):
    ''' Полнотекствоый поиск '''
    search_text = search_text.strip()

    vector = (
        SearchVector('name', weight='A') +
        SearchVector('description', 'short_description', weight='B')
    )
    query = SearchQuery(search_text)
    
    if search_text.isdigit() and len(search_text) <= 5:
        return ProductModel.objects.filter(id=int(search_text))
    
    if len(search_text) >= 3:
        results = ProductModel.objects.annotate(
            rank=SearchRank(vector=vector, query=query),
        ).filter(rank__gte=0.05).order_by('-rank')
        return results

    return ProductModel.objects.none()
