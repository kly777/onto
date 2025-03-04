from tools.translator import Translator
from tools.suit import TextProcessor
import json

config = json.load(open("./config.json", "r"))

processor = TextProcessor(
    api_key=config['bl_api_key'],
    chunk_size=5000,
    overlap=200,
)

translator = Translator(
    api_key=config["ds_api_key"],
)

MID = "MID.md"
# processor.process_file(input_path="Category.md", output_path=MID)
translator.process_file(input_path="Category.md", output_path="CategoryT.md")
