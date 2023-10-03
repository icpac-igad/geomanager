import logging

from django.db.models.signals import post_save
from wagtailcache.cache import clear_cache

from .aoi import *
from .core import *
from .geostore import *
from .profile import *
from .raster_file import *
from .raster_tile import *
from .stations import *
from .tile_gl import *
from .vector_file import *
from .vector_tile import *
from .wms import *

logger = logging.getLogger(__name__)


# clear wagtail cache on saving the following models
@receiver(post_save, sender=Category)
@receiver(post_save, sender=SubCategory)
@receiver(post_save, sender=Dataset)
@receiver(post_save, sender=Metadata)
@receiver(post_save, sender=GeomanagerSettings)
@receiver(post_save, sender=RasterFileLayer)
@receiver(post_save, sender=LayerRasterFile)
@receiver(post_save, sender=RasterStyle)
@receiver(post_save, sender=WmsLayer)
@receiver(post_save, sender=MBTSource)
@receiver(post_save, sender=VectorFileLayer)
@receiver(post_save, sender=PgVectorTable)
def handle_clear_wagtail_cache(sender, **kwargs):
    logging.info("[WAGTAIL_CACHE]: Clearing cache")
    clear_cache()
