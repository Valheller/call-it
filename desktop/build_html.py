# Inlines the Google Fonts into the game so the desktop build works offline.
# Writes desktop/resources/index.html from ../index.html.
import re,base64,subprocess,os
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'..','index.html'),encoding='utf-8').read()
css=open(os.path.join(here,'fonts.css'),encoding='utf-8').read()
def fetch(u):
    return subprocess.run(['curl','-sS',u],capture_output=True,check=True).stdout
def inline(m):
    return 'url(data:font/woff2;base64,'+base64.b64encode(fetch(m.group(1))).decode()+')'
css=re.sub(r'url\((https://[^)]+)\)',inline,css)
src=src.replace('<link rel="preconnect" href="https://fonts.googleapis.com">\n','').replace('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n','')
src=re.sub(r'<link href="https://fonts.googleapis.com/css2[^>]*>','<style>'+css+'</style>',src)
src=re.sub(r"url\((https://fonts.gstatic.com/[^)]+)\)",inline,src)
assert 'googleapis' not in src and 'gstatic' not in src
open(os.path.join(here,'resources','index.html'),'w',encoding='utf-8').write(src)
print('wrote resources/index.html',len(src))
