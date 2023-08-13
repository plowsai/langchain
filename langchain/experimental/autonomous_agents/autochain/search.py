from typing import Any, Dict, List

import json
import re
from abc import abstractmethod
from typing import Dict, NamedTuple

from langchain.schema import BaseOutputParser

class AutoChain(NamedTuple):
    name: str
    args: Dict