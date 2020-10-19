from bs4 import BeautifulSoup
SIMPLE_HTML = '''
<html>
<head></head>
<body>
<h1>This the first header</h1>
<p class="subtitle">first html program using python</p>
<p>Here's another para tag without class</p>
<ul>
    <li>devam</li>
    <li>umang</li>
    <li>apurva</li>
    <li>heena</li>
</ul>
</body>
</html>
'''
def list_items():
    list_items= simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)

def find_subtitles():
    para = simple_soup.find('p', {'class':'subtitle'})
    print(para.string)

def find_other():
    para = simple_soup.find_all('p')
    other_para = [p for p in para if 'subtitle' not in p.attrs.get('class',[])]
    print(other_para[0].string)
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find('h1'))
list_items()
find_subtitles()
find_other()