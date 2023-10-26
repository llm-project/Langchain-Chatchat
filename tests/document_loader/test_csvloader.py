import sys
from pathlib import Path

root_path = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))
from pprint import pprint

test_files = {
    "ocr_test.csv": str(root_path / "tests" / "samples" / "ocr_test.csv"),
}

def test_rapidcsvloader():
    img_path = test_files["ocr_test.csv"]
    from document_loaders import RapidCSVLoader

    loader = RapidCSVLoader(img_path)
    docs = loader.load()
    pprint(docs)
    assert isinstance(docs, list) and len(docs) > 0 and isinstance(docs[0].page_content, str)


