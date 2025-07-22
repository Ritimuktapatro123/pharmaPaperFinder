from pharma_paper_finder.filters import is_non_academic, is_pharma_or_biotech, parse_papers

def test_is_non_academic():
    assert is_non_academic("Stanford University") is False
    assert is_non_academic("Pfizer Inc") is True

def test_is_pharma_or_biotech():
    assert is_pharma_or_biotech("Pfizer Inc") is True
    assert is_pharma_or_biotech("MIT School of Biology") is False

def test_parse_papers_basic():
    sample_xml = """
    <PubmedArticleSet>
      <PubmedArticle>
        <MedlineCitation>
          <PMID>123456</PMID>
          <Article>
            <ArticleTitle>Research on Cancer Drugs</ArticleTitle>
            <AuthorList>
              <Author>
                <LastName>Doe</LastName>
                <ForeName>John</ForeName>
                <AffiliationInfo>
                  <Affiliation>Pfizer Inc., New York, NY john.doe@pfizer.com</Affiliation>
                </AffiliationInfo>
              </Author>
            </AuthorList>
            <Journal>
              <JournalIssue>
                <PubDate>
                  <Year>2024</Year>
                </PubDate>
              </JournalIssue>
            </Journal>
          </Article>
        </MedlineCitation>
      </PubmedArticle>
    </PubmedArticleSet>
    """
    result = parse_papers(sample_xml)
    assert len(result) == 1
    paper = result[0]
    assert paper["PubmedID"] == "123456"
    assert paper["Title"] == "Research on Cancer Drugs"
    assert paper["Publication Date"] == "2024"
    assert "Pfizer Inc." in paper["Company Affiliation(s)"][0]
