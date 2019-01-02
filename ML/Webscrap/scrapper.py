# Extracting product information into dictionaries
product_information = []
visited = set()
for url in product_urls:
    if url in visited:
        continue
    visited.add(url)
    product = {'url': url}
    soup = get_page(url)
if not soup:
    continue # something went wrong with the download
h1 = soup.find('h1')
if h1:
    product['name'] = h1.text.strip()
pricing = soup.find('div', class_='pricing')
if pricing:
    p = pricing.find('p', class_='pricePerUnit')
    unit = pricing.find('span', class_='pricePerUnitUnit')
    if p:
        product['price'] = p.text.strip()
            if unit:
                product['unit'] = unit.text.strip()
label = soup.find('label', class_='numberOfReviews')
if label:
    img = label.find('img', alt=True)
    if img:
        product['rating'] = img['alt'].strip()
    reviews = reviews_pattern.findall(label.text.strip())
    if reviews:
        product['reviews'] = reviews[0]
item_code = soup.find('p', class_='itemCode')
if item_code:
    item_codes = item_code_pattern.findall(item_code.text.
    strip())
    if item_codes:
        product['itemCode'] = item_codes[0]
table = soup.find('table', class_='nutritionTable')
if table:
    rows = table.findAll('tr')
    for tr in rows[1:]:
        th = tr.find('th', class_='rowHeader')
        td = tr.find('td')
        if not th:
            product['Energy kcal'] = td.text
        else:
            product[th.text] = td.text
product_origin_header = soup.find('h3',
class_='productDataItemHeader', text='Country of Origin')
if product_origin_header:
    product_text = product_origin_header.find_next_
    sibling('div', class_='productText')
if product_text:
    origin_info = []
for p in product_text.find_all('p'):
    origin_info.append(p.text.strip())
    product['Country of Origin'] = '; '.join(origin_info)
product_information.append(product)