def describe_city(city, country='Philippines'):
  
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Manila')
describe_city('Dubai', 'United Arab Emirates')
describe_city('Cebu')