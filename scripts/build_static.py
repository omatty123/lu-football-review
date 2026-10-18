from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
out=root/'_site'
out.mkdir(exist_ok=True)
for name in ['index.html','full-report.html','style.css','story.css','fonts.css','app.js','story.js','data.js']:
 shutil.copy2(root/name,out/name)
for name in ['assets','data']:
 shutil.copytree(root/name,out/name,dirs_exist_ok=True)
