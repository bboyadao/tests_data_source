from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import logging

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.__str__()
logger = logging.getLogger(__name__)


class Setting(BaseSettings):
    pass

settings = Setting()
