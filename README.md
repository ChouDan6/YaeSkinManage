YaeSkinManage  
d3dxskinmanage修改版  
移除更新检查，支持进程名修改  
python -m venv venv  
call venv\Scripts\activate.bat  
pip install --upgrade pip  
pip install -r requirements.txt  
pyinstaller --clean -F -w -n YaeSkinManage -i src\yae.ico src\d3dxSkinManage.py  
