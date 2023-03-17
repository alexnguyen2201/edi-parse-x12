from badx12 import Parser
from pathlib import Path
import json
import time

WORKING_DIR_LOCATION = Path(__file__).parents[0]
OUPUT_DIR_LOCATION = WORKING_DIR_LOCATION / "output"
INPUT_FILE_LOCATION = WORKING_DIR_LOCATION / "data"

files = list((INPUT_FILE_LOCATION).glob("*.edi"))
for f in files:
    parser = Parser(f"{INPUT_FILE_LOCATION}/{f.name}")
    document = parser.document
    doc_dict = document.to_dict()

    for key in doc_dict["document"]:
        print(key)

    file_name = f"{f.name}-{int(time.time())}-output.json"
    with open(f'{OUPUT_DIR_LOCATION}/{file_name}', 'w') as fp:
        json.dump(doc_dict, fp=fp, indent=2)