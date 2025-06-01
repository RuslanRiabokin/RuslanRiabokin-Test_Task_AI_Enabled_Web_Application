import sys
import os
from faq_loader import search_faq, FAQEntry
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_search_faq_exact_match():
    faq_list = [
        FAQEntry(id=1, question="Що таке API?", answer="API — це інтерфейс..."),
        FAQEntry(id=2, question="Що таке машинне навчання?", answer="Це метод..."),
    ]

    result = search_faq("Що таке API?", faq_list)

    assert len(result) == 1
    assert result[0].question == "Що таке API?"
    assert "інтерфейс" in result[0].answer
