import requests

# Connect to API
url = 'https://api.freelance.nl/graphql'
payload = {"query":"\n\tquery GetProjects (\n\t\t$expertiseList: [String!], \n\t\t$excludedStrings: [String],\n\t\t$sortOrder: String,\n\t\t$search: [String],\n\t\t$onLocationArray: [String],\n\t\t$rawProvinces: [String],\n\t\t$page: Int!\n\t\t$states: [String!]\n\t\t) {\n\t  projects(\n\t\texpertises: $expertiseList, \n\t\torder_publishTimestamp: $sortOrder,\n\t\texcludedStrings: $excludedString,\n\t\tsearch: $search,\n\t\tonLocationArray: $onLocationArray,\n\t\trawProvinces: $rawProvinces,\n\t\titemsPerPage: 15, \n\t\tstates: $states,\n\t\tpage: $page\n\t\t) {\n\t\t\ttotalCount\n\t\t\tresults {\n\t\t\t\tid\n\t\t\t\tname\n\t\t\t\tonLocation\n\t\t\t\trawPlace\n\t\t\t\treplyCount\n\t\t\t\tpublishTimestamp\n\t\t\t\tstate\n\t\t\t}\n\t\t  }\n\t}\n","variables":{"page":1,"onLocationArray":["yes","unknown"],"states":["open","paused"]}}

# Retrieve data and change format
response = requests.post(url, json=payload)
data = response.json()

# Get data from dictionary
results = data['data']['projects']['results']

# Create empty list to save the data
urls = []

# Loop over dictionary in list, get id and name, and formulate url with it
for dict in results:
    id = str(dict.get('id'))
    name = str(dict.get('name'))
    name = name.replace(' ', '-').replace('(', '').replace(')', '').replace('’', '').lower()
    url = 'https://www.freelance.nl/opdracht/' + id + '-' + name
    urls.append(url)

print(urls)
