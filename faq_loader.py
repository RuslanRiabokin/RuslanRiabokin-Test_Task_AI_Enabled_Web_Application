import csv


class FAQEntry:
    """
        A class representing a single FAQ entry with ID, question, and answer.
        """

    def __init__(self, id: int, question: str, answer: str):
        """
            Load FAQ entries from a CSV file.

            Args:
                path (str): Path to the CSV file (default is "faq.csv").

            Returns:
                list[FAQEntry]: A list of FAQEntry objects loaded from the file.
            """
        self.id = id
        self.question = question
        self.answer = answer


def load_faq_csv(path: str = "faq.csv") -> list[FAQEntry]:
    """
        Search for FAQ entries that match the input question phrase.

        Args:
            question (str): The question to search for.
            faq_list (list[FAQEntry]): The list of FAQ entries to search in.

        Returns:
            list[FAQEntry]: A list of matched FAQ entries.
        """
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
