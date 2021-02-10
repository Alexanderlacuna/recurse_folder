# code adapted from https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

import os
import re
from bs4 import BeautifulSoup as soup 
target = "/home/kabui/project3/genenetwork2/wqflask/wqflask/templates"

for subdir, dirs, files in os.walk(target):
	for file in files:
		file_path = subdir + os.sep + file
		if file_path.endswith(".html"):
			# print(file_path)
			parsed_page = soup(open(file_path, encoding="utf8"), "html.parser")
			fetch_script_tags(parsed_page=parsed_page)


def fetch_script_tags(parsed_page):
    broken_links = set()
    # print("--->fetching js links")
    for link in parsed_page.findAll("script"):
        # print(link)
        js_link = link.attrs.get("src")
        if js_link is not None:
            if re.match(r'^http://', js_link):
                # broken_links.add(js_link)
                print(f"Link should not be here {link_url}")
        # else:
        # 	# print(link)
        # 	pass

            elif re.match(r"^/css", js_link) or re.match(r"^/js", js_link):
                full_path = urljoin('http://localhost:5004/', js_link)
                results = test_link(full_path)
                if results is not None:
                    broken_links.add(js_link)



