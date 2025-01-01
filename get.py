import requests
import os
import sys
rpn=None
if len(sys.argv)==2:
    rpn=sys.argv[1]
    with open("rpn.txt","w",encoding="utf-8") as f:
        f.write(rpn)
with open("rpn.txt","r",encoding="utf-8") as f:
    rpn=f.read()
import os

current_dir = os.getcwd()
for root, dirs, files in os.walk(current_dir):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        if dir_path!= os.path.join(current_dir, "js") and dir_path!= os.path.join(current_dir, ".github") and dir_path!= os.path.join(current_dir, ".git") and os.path.dirname(dir_path) == current_dir:
            import shutil
            shutil.rmtree(dir_path)
url = f"https://api.github.com/repos/{rpn}/releases"

response = requests.get(url)
releases = response.json()
dls2=""
# 遍历每个发行版
for release in releases:
    version = release["tag_name"]
    assets = release["assets"]
    dir_name = version

    # 创建对应版本号的目录
    os.makedirs(dir_name, exist_ok=True)
    dls=""
    # 遍历发行版中的文件
    for asset in assets:
        file_name = asset["name"]
        file_url = asset["browser_download_url"]
        
        dls=dls+f"""        <li><a href="https://gh.api.99988866.xyz/{file_url}">{file_name}</a></li>\n"""

    html_text=f'''
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Index of /{version}</title>
</head>

<body>
    <h1>Index of /{version}</h1>
    <input type="text" id="searchInput" placeholder="输入关键字搜索文件"> <!-- 添加了id属性 -->
    <ul id="fileList"> <!-- 添加了id属性 -->
{dls}
    </ul>
    <script src="/js/scr.js"></script>
</body>

</html>
    '''
    import os
    htfl=os.path.join(dir_name,"index.html")
    with open(htfl,"w",encoding="utf-8") as f:
        f.write(html_text)
    
    dls2=dls2+f"""        <li><a href="{version}/index.html">{version}</a></li>\n"""
html_text2=f'''
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Index of /</title>
</head>

<body>
    <h1>Index of /</h1>
    <input type="text" id="searchInput" placeholder="输入关键字搜索文件"> <!-- 添加了id属性 -->
    <ul id="fileList"> <!-- 添加了id属性 -->
{dls2}
    </ul>
    <script src="/js/scr.js"></script>
</body>

</html>
'''
import os
with open("index.html","w",encoding="utf-8") as f:
    f.write(html_text2)
