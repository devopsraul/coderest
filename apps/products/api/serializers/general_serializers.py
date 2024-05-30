from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from rest_framework import serializers

class MeasureUnitSelializer(serializers.ModelSerializer):
    
    class Meta:
        model - MeasureUnit
        exclude = ('state',)
        
class CategoryProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryProduct
        exclude = ('state',)
        
class IndicadorSerializer(serializers.ModelSerializer):
    
    class meta:
        model = Indicator
        exclude = ('state',)        