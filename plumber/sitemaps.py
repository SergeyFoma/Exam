from django.contrib.sitemaps import Sitemap
from materials.models import CategoryMaterials
from plumber.models import Mashine

class PlumberSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return CategoryMaterials.objects.all()

class MashineSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Mashine.objects.all()