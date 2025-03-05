from tools.translator import Translator
from tools.suit import TextProcessor
import json

config = json.load(open("./config.json", "r"))

processor = TextProcessor(
    api_key=config["bl_api_key"],
    chunk_size=5000,
    overlap=200,
)

translator = Translator(
    api_key=config["ds_api_key"],
)

target = "./.md"
Mid = target.replace(".md", "M.md")
Final = target.replace(".md", "T.md")
processor.process_file(input_path=target, output_path=Mid)
translator.process_file(input_path=Mid, output_path=Final)
