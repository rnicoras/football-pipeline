import json
import logging
from datetime import datetime, timezone
from azure.storage.blob import BlobServiceClient
from ingestion.utils.config import Config

logger = logging.getLogger(__name__)

class AzureUpload:
    def __init__(self):
        self.client = BlobServiceClient(account_url=f"https://{Config.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=Config.AZURE_STORAGE_ACCOUNT_KEY)
        self.container = Config.AZURE_CONTAINER_NAME

    def json_to_azure(self, data: dict | list, source: str, filename: str):
        # path format: raw/{source}/{year}/{month}/{day}/{filename}.json

        today = datetime.now(timezone.utc)
        blob_path = (f"raw/{source}/"f"{today.year}/{today.month:02d}/{today.day:02d}/"f"{filename}.json")
        
        blob_client = self.client.get_blob_client(container = self.container, blob = blob_path)

        blob_client.upload_blob(json.dumps(data, indent = 2), overwrite = True, content_type = "application/json")

        logger.info(f"Uploaded to Azure: {blob_path}")
        return blob_path