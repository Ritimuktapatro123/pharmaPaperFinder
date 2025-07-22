from typing import List, Dict
import requests

def fetch_pubmed_ids(query: str, retmax: int = 20) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data["esearchresult"]["idlist"]

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    ids = ",".join(pubmed_ids)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    return response.text  # raw XML
