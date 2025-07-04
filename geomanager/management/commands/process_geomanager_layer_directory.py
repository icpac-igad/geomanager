import glob
import logging
import os

from django.core.management.base import BaseCommand

from geomanager.settings import geomanager_settings
from geomanager.utils.ingest import ingest_raster_file

logger = logging.getLogger(__name__)

ALLOWED_FILE_EVENTS = ["created", "moved"]

RASTER_FILE_EXTENSIONS = [
    ".tif",
    ".nc",
]


class Command(BaseCommand):
    help = "Process a raster file layer directory"

    def add_arguments(self, parser):
        parser.add_argument("layer_id", type=str, help="Layer ID")
        parser.add_argument("--overwrite", action="store_true", default=False, help="Overwrite existing raster file")
        parser.add_argument("--clip", action="store_true", default=False, help="Clip raster to county boundary")

    def handle(self, *args, **options):
        layer_id = options["layer_id"]
        overwrite = options["overwrite"]
        clip = options["clip"]

        auto_ingest_raster_data_dir = geomanager_settings.get("auto_ingest_raster_data_dir", None)

        if not auto_ingest_raster_data_dir:
            logger.error("[GEOMANAGER_AUTO_INGEST]: Auto ingest raster data directory not configured.")
            return

        logger.debug("[GEOMANAGER_AUTO_INGEST]: Starting directory processing...")

        directory = os.path.join(auto_ingest_raster_data_dir, layer_id)

        if not os.path.isdir(directory):
            logger.error(f"[GEOMANAGER_AUTO_INGEST]: Directory: {directory} does not exist.")
            return

        for ext in RASTER_FILE_EXTENSIONS:
            files = glob.glob(directory + f"/*{ext}")

            if not files:
                logger.warning(
                    f"[GEOMANAGER_AUTO_INGEST]: No files found in directory: {directory} with extension: {ext}"
                )

            for file in files:
                logger.info(f"[GEOMANAGER_AUTO_INGEST]: Processing file: {file}")
                ingest_raster_file(file, overwrite, clip)
                logger.info(f"[GEOMANAGER_AUTO_INGEST]: {file} done...")
