import requests
from jinja2 import Template

ORCID_IDS = ["0000-0001-9720-3899", "0000-0002-8333-5687", "0000-0003-2664-1634"]  # Replace with actual ORCID IDs

def fetch_orcid_publications(orcid_id):
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/activities"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []
    data = response.json()
    publications = []
    if 'works' in data and 'group' in data['works']:
        for group in data['works']['group']:
            work = group['work-summary'][0]
            title = work['title']['title']['value']
            year = work['publication-date']['year']['value']
            authors = []

            #Extract authors from contributors, if available
            if 'contributors' in work:
                for contributor in work['contributors']['contributor']:
                    if 'credit-name' in contributor:
                        authors.append(contributor['credit-name']['value'])
                      
            doi = next(
                (id['external-id-value'] for id in work['external-ids']['external-id']
                 if id['external-id-type'] == 'doi'), None
            )
            publications.append({'title': title, 'year': year, 'authors': authors, 'doi': doi})
    return publications

# Fetch data and group by year
all_publications = []
for orcid_id in ORCID_IDS:
    all_publications.extend(fetch_orcid_publications(orcid_id))

# Sort and group publications by year
publications_by_year = {}
for pub in all_publications:
    publications_by_year.setdefault(pub['year'], []).append(pub)
sorted_years = sorted(publications_by_year.keys(), reverse=True)

# Generate HTML
template = Template(open("template.html").read())
html_content = template.render(publications_by_year=publications_by_year, sorted_years=sorted_years)

# Save HTML
with open("publications.html", "w") as f:
    f.write(html_content)
