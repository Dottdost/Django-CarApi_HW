from typing import Dict
from threading import Lock
from models import *
_store: Dict[str, CarRead] = {}
_next_id: int = 1
_lock: Lock = Lock()