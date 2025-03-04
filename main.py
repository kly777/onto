from translator import Translator
from suit import TextProcessor
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
print(config)

MID = "MID.md"
processor.process_file(input_path="try.md", output_path=MID)
translator.process_file(input_path=MID, output_path="out.md")
