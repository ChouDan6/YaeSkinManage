# Licensed under the GNU General Public License v3.0, see <http://www.gnu.org/licenses/gpl-3.0.html>.
# d3dxSkinManage Copyright (C) 2023 numlinka.

# local
import core
import window
import constant


msg = [
    "该软件由LucyTtk & 影修改，支持更改进程名，仅供个人使用，禁止用于商业用途",
]

index = -1


def title_cycle(*_):
    global index
    index += 1
    if index == len(msg): index = 0
    text = core.env.MAIN_TITLE + "  :  " + msg[index]
    window.mainwindow.title(text)
    window.mainwindow.after(10000, title_cycle)


def ready():
    window.mainwindow.after(5000, title_cycle)


def initial():
    if core.argv.demomode: return
    core.construct.event.register(constant.E.ENTER_MAINPOOL, ready)
