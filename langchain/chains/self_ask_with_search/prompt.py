# flake8: noqa
from pathlib import Path

from langchain.prompts.data import BaseExample
from langchain.prompts.prompt import Prompt

example_path = Path(__file__).parent / "examples.json"
import json


class SelfAskWithSearchExample(BaseExample):
    question: str
    answer: str

    def formatted(self) -> str:
        return f"Question: {self.question}\n{self.answer}"


with open(example_path) as f:
    raw_examples = json.load(f)
    examples = [SelfAskWithSearchExample(**example) for example in raw_examples]

PROMPT = Prompt.from_examples(
    examples,
    "Question: {input}",
    ["input"],
)
