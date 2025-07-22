import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "hospital", "lab"]
    return not any(keyword in affiliation.lower() for keyword in academic_keywords)

def is_pharma_or_biotech(affiliation: str) -> bool:
    pharma_keywords = ["pharma", "biotech", "therapeutics", "biosciences", "laboratories", "inc", "ltd", "gmbh"]
    return any(keyword in affiliation.lower() for keyword in pharma_keywords)

def parse_papers(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    result = []
    for article in root.findall(".//PubmedArticle"):
        paper = {
            "PubmedID": article.findtext(".//PMID"),
            "Title": article.findtext(".//ArticleTitle"),
            "Publication Date": article.findtext(".//PubDate/Year", default=""),
            "Non-academic Author(s)": [],
            "Company Affiliation(s)": [],
            "Corresponding Author Email": "",
        }

        for author in article.findall(".//Author"):
            aff = author.findtext(".//AffiliationInfo/Affiliation", default="")
            name = (author.findtext("ForeName", "") + " " + author.findtext("LastName", "")).strip()
            if aff:
                if is_non_academic(aff):
                    paper["Non-academic Author(s)"].append(name)
                if is_pharma_or_biotech(aff):
                    paper["Company Affiliation(s)"].append(aff)
        # Very basic heuristic for email
        emails = [a for a in aff.split() if "@" in a]
        if emails:
            paper["Corresponding Author Email"] = emails[0]

        if paper["Company Affiliation(s)"]:
            result.append(paper)
    return result
