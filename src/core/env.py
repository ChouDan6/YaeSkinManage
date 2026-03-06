# Licensed under the GNU General Public License v3.0, see <http://www.gnu.org/licenses/gpl-3.0.html>.
# d3dxSkinManage Copyright (C) 2023 numlinka.

# std
import os
import sys
import ctypes
import subprocess
from os.path import join as __

# self
import libs.econfiguration
from libs.dirstruct import *

# local
from .exceptions import *

# ==================== 动态获取程序名称与任务栏图标修复 ====================
_exe_name = os.path.basename(sys.executable)
_is_compiled = False
if _exe_name.lower().endswith('.exe') and not _exe_name.lower().startswith('python'):
    PROJECT = _exe_name[:-4]
    _is_compiled = True
else:
    PROJECT = "YaeSkinManage"

# 强制注册 AppUserModelID，让 Windows 任务栏使用我们 EXE 自身的图标而不是 Python 默认图标
try:
    if sys.platform == 'win32':
        myappid = f'numlinka.d3dxSkinManage.{PROJECT}.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass
# =======================================================================

AUTHOR = "numlinka"

VERSION_CODE = 1_06_04_000
VERSION_TYPE = ""
VERSION_NAME = "1.6.4"

MAIN_TITLE = f"{PROJECT} v{VERSION_NAME} -by {AUTHOR}"

CODE_NAME = "kamisa"
INDEX = f"https://numlinka.oss-cn-shanghai.aliyuncs.com/code-name/{CODE_NAME}/index.json"

class __CurrentWorkingDirectory (Directory):
    _include_ = False

    class resources (Directory):
        mods = "mods"
        d3dxs = "3dmigoto"
        preview = "preview"
        preview_screen = "preview_screen"
        thumbnail = "thumbnail"
        cache = "cache"
        redirection = FilePath(__("thumbnail", "_redirection.ini"))

    class local (Directory):
        t7zip = "7zip"
        t7z = FilePath(__("7zip", "7z.exe"))
        # ==================== 窗口图标脱离依赖修复 ====================
        if _is_compiled:
            # 如果是打包后的 exe，直接让 Tkinter 提取自身的图标，不再依赖 external ico
            iconbitmap = sys.executable 
        else:
            iconbitmap = FilePath("iconbitmap.ico")
        # ==============================================================
        configuration = FilePath("configuration")

    home = "home"
    plugins = "plugins"

    update = FilePath("update.exe")
    self = FilePath(f"{PROJECT}.exe")


cwd = __CurrentWorkingDirectory(os.getcwd())
base = cwd
directory = cwd
file = cwd

abscwd = __CurrentWorkingDirectory(os.getcwd())
abscwd._include_ = True

class configuration(libs.econfiguration.Configuration):
    log_level: int | str
    annotation_level: int
    style_theme: str
    view_explorer_path: str
    view_file_rule: str
    view_directory_rule: str
    thumbnail_approximate_algorithm: str

try:
    configuration = libs.econfiguration.Configuration(file.local.configuration)
except Exception:
    configuration = libs.econfiguration.Configuration()

class Link (object):
    help = "https://d3dxskinmanage.numlinka.com/help"
    afdian = "https://afdian.com/a/numlinka"
    afdian_ticca = "https://afdian.com/a/ticca"

try: 
    uuid = subprocess.check_output("wmic csproduct get UUID", shell=True).decode("utf-8").replace("UUID", "").strip()
except Exception:
    try:
        uuid = subprocess.check_output("powershell /c \"(Get-WmiObject Win32_ComputerSystemProduct).UUID\"").decode("utf-8").strip()
    except Exception:
        uuid = ""

try:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
except Exception as _:
    is_admin = None

__all__ = [
    "PROJECT",
    "AUTHOR",
    "VERSION_CODE",
    "VERSION_TYPE",
    "VERSION_NAME",
    "MAIN_TITLE",
    "CODE_NAME",
    "INDEX",
    "base",
    "directory",
    "file",
    "configuration",
    "Link"
]