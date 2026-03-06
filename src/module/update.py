# Licensed under the GNU General Public License v3.0, see <http://www.gnu.org/licenses/gpl-3.0.html>.
# d3dxSkinManage Copyright (C) 2023 numlinka.

# std
import os
import hashlib
import threading

# site
import requests

# local
import core
from constant import *

__event = threading.Event()

def deadlock():
    __event.wait()
    __event.clear()

def release_deadlock():
    __event.set()

def stop_control(msg: str = "未知错误"):
    core.window.messagebox.showerror(title="更新检查", message=f"module.update::stop_control\n{msg}")
    return
    core.window.status.set_status(f"{msg}", 1)
    deadlock()

def check():
    # ==================== 屏蔽更新检查 ====================
    return
    # ======================================================
    core.log.info("检查更新...", L.MODULE_UPDATE)
    try: # 我不是很相信这个东西
        if verify_key(core.argv.noupdatecheck):
            core.log.warning("跳过更新检查", L.MODULE_UPDATE)
            return
    except Exception as _:
        ...
    core.window.block.setcontent("正在检查更新...")
    try:
        index_requests = requests.get(core.env.INDEX)
        status_code = index_requests.status_code
        if status_code != 200:
            stop_control(f"检查更新失败: {status_code} 错误")
            return

    except requests.exceptions.ProxyError:
        core.window.messagebox.showerror("网络代理错误", "请检查网络代理设置或关闭代理后重试")
        stop_control(f"检查更新失败: 代理错误")
        return

    except Exception as e:
        stop_control(f"{e.__class__} 检查更新失败: 未知错误")
        return

    try:
        index_content = index_requests.json()
        version_code = index_content["version_code"]
        version_name = index_content["version_name"]
        content = index_content["content"]
        message = index_content["message"]

        if core.env.VERSION_CODE < version_code:
            get_update(index_content)

        if index_content["block"]:
            block(message)

    except Exception as e:
        stop_control(f"检查更新失败: 信息解析异常")
        return

def get_update(index_content: dict):
    pass

def progress_bar(chunk_number, chunk_size, total_size):
    percent_complete = int((chunk_number * chunk_size / total_size) * 100)
    core.window.status.set_progress(percent_complete)

def block(message):
    core.window.block.setcontent(message)
    stop_control("启动程序被拒绝")
    ...

def verify_key(key: str):
    u8 = "utf-8"
    s1, s2, s3 = hashlib.sha512(), hashlib.sha512(), hashlib.md5()
    s1.update(key.encode(u8))
    s2.update(s1.hexdigest().encode(u8))
    s3.update(s2.hexdigest().encode(u8))
    return s3.hexdigest() == "c9bca91be66be860c2505d4a93e2b704"