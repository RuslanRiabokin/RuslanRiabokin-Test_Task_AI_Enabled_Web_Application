import csv

class FAQEntry:
    def __init__(self, id: int, question: str, answer: str):
        self.id = id
        self.question = question
        self.answer = answer

def load_faq_csv(path: str = "faq.csv") -> list[FAQEntry]:
    faq_entries = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            faq_entries.append(FAQEntry(
                id=int(row["id"]),
                question=row["question"],
                answer=row["answer"]
            ))
    return faq_entries

def search_faq(question: str, faq_list: list[FAQEntry]) -> list[FAQEntry]:
    """Пошук за фразою у питанні"""
    return [
        entry for entry in faq_list
        if question.lower() in entry.question.lower()
    ]

