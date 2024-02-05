from django.db import transaction
from .models import Attraction, AttractionsPicture

def create_attraction_with_pictures(attraction_data, pictures_data):
    with transaction.atomic():
        # 创建 Attractions 对象
        attraction = Attraction.objects.create(**attraction_data)

        # 创建 AttractionsPictures 对象
        pictures = []
        for picture_data in pictures_data:
            picture_data['related_attr'] = attraction
            picture = AttractionsPicture(**picture_data)
            pictures.append(picture)

        AttractionsPicture.objects.bulk_create(pictures)

    return attraction