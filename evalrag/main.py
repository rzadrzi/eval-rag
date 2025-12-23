# from core import Ingestion
# from core import load_core_config
# from pathlib import Path

# path  = Path(__file__).resolve().parent / "sample.pdf"

# config = load_core_config().ingestion

# ingestion = Ingestion(config=config)
# ingestion.indexing(filename=str(path))
# print(config)
# print(path)

from core import load_core_config, load_prompt_config

print(load_core_config())

print(load_prompt_config().judge_template)
