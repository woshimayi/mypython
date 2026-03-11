#!/usr/bin/env python3
"""
EasyConnect 自动登录脚本
适用于 Ubuntu 24.04
功能：自动启动 EasyConnect 并填写凭证登录
"""

import time
import subprocess
import os
import sys
import re
from pathlib import Path

# ================= 配置区域 =================
# EasyConnect 配置
EASYCONNECT_PATH = "/usr/share/sangfor/EasyConnect/EasyConnect"  # 默认安装路径

# VPN 凭证
VPN_USERNAME = 'xxxxx'
VPN_PASSWORD = 'xxxxx'

# 密码重置配置（当 EasyConnect 要求修改密码时使用）
ENABLE_PASSWORD_RESET = True          # 是否启用自动处理密码重置
VPN_NEW_PASSWORD = ''                 # 新密码，留空则自动生成
PASSWORD_RESET_PATTERNS = [           # 密码重置窗口标题关键词
    r"修改密码",
    r"重置密码",
    r"更改密码",
    r"Change.*Password",
    r"Reset.*Password",
    r"Modify.*Password",
    r"password.*expir",
    r"密码.*过期",
    r"密码.*到期",
]

# 自动化设置
TYPING_INTERVAL = 0.1  # 打字间隔（秒）
WAIT_BETWEEN_STEPS = 1.0  # 步骤间等待时间（秒）
WINDOW_WAIT_TIMEOUT = 30  # 窗口等待超时（秒）

# 窗口名称模式（用于定位 EasyConnect 窗口）
WINDOW_PATTERNS = [
    r"EasyConnect",
    r"EASYCONNECT",
    r"深信服",
    r"Sangfor",
    r"SSL VPN",
    r"SSLVPN",
    r"登录",
    r"Login"
]

# 坐标定位（如果需要）
CLICK_CENTER = True  # 是否点击窗口中央

# 调试模式
DEBUG = True

# 监控配置
ENABLE_MONITOR = True          # 是否启用监控
MONITOR_INTERVAL = 30           # 检查间隔（秒）
MAX_RECONNECT_ATTEMPTS = 10    # 最大重连次数
RECONNECT_DELAY = 10           # 重连前等待时间（秒）
# ===========================================


class EasyConnectAutoLogin:
    def __init__(self):
        self.is_connected = False
        self.easyconnect_pid = None
        self.window_id = None

    def log_debug(self, message):
        """输出调试信息"""
        if DEBUG:
            print(f"[DEBUG] {message}")

    def check_xdotool(self):
        """检查 xdotool 是否已安装"""
        try:
            subprocess.run(
                ["which", "xdotool"],
                check=True,
                capture_output=True
            )
            self.log_debug("xdotool 已安装")
            return True
        except subprocess.CalledProcessError:
            print("[-] xdotool 未安装")
            print("请安装: sudo apt install xdotool")
            return False

    def check_wmctrl(self):
        """检查 wmctrl 是否已安装"""
        try:
            subprocess.run(
                ["which", "wmctrl"],
                check=True,
                capture_output=True
            )
            self.log_debug("wmctrl 已安装")
            return True
        except subprocess.CalledProcessError:
            self.log_debug("wmctrl 未安装")
            return False

    def get_window_list(self):
        """获取当前所有窗口列表"""
        try:
            if self.check_wmctrl():
                result = subprocess.run(
                    ["wmctrl", "-l"],
                    capture_output=True,
                    text=True
                )
                return result.stdout
            else:
                # 使用 xdotool 获取窗口列表
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", "--name", "."],
                    capture_output=True,
                    text=True
                )
                return result.stdout
        except Exception as e:
            self.log_debug(f"获取窗口列表失败: {e}")
            return ""

    def find_window_by_pid(self):
        """通过进程 PID 查找窗口"""
        if not self.easyconnect_pid:
            return False

        try:
            # 使用 xdotool 按进程 PID 搜索窗口
            result = subprocess.run(
                ["xdotool", "search", "--pid", str(self.easyconnect_pid)],
                capture_output=True,
                text=True
            )

            if result.stdout.strip():
                # 取最后一个窗口 ID（通常是主窗口）
                window_ids = result.stdout.strip().split('\n')
                self.window_id = window_ids[-1]
                print(f"[+] 通过 PID 找到窗口: {self.window_id}")
                return True
        except Exception as e:
            self.log_debug(f"通过 PID 查找窗口失败: {e}")

        return False

    def find_easyconnect_window(self):
        """查找 EasyConnect 窗口"""
        print("[*] 查找 EasyConnect 窗口...")

        # 方法1: 通过 PID 查找（最可靠）
        if self.find_window_by_pid():
            return True

        # 方法2: 使用 xdotool 直接搜索窗口名
        for pattern in WINDOW_PATTERNS:
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", "--name", pattern],
                    capture_output=True,
                    text=True
                )
                if result.stdout.strip():
                    self.window_id = result.stdout.strip().split('\n')[0]
                    print(f"[+] 找到匹配窗口: {pattern}")
                    self.log_debug(f"窗口 ID: {self.window_id}")
                    return True
            except:
                pass

        # 方法3: 使用 xdotool 搜索窗口类名
        for pattern in WINDOW_PATTERNS:
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", "--class", pattern],
                    capture_output=True,
                    text=True
                )
                if result.stdout.strip():
                    self.window_id = result.stdout.strip().split('\n')[0]
                    print(f"[+] 找到匹配窗口类: {pattern}")
                    self.log_debug(f"窗口 ID: {self.window_id}")
                    return True
            except:
                pass

        # 方法4: 使用 wmctrl 列表
        if self.check_wmctrl():
            window_output = subprocess.run(
                ["wmctrl", "-l"],
                capture_output=True,
                text=True
            ).stdout

            self.log_debug(f"窗口列表:\n{window_output}")

            for pattern in WINDOW_PATTERNS:
                match = re.search(
                    r'^(0x[0-9a-f]+).*' + re.escape(pattern),
                    window_output,
                    re.IGNORECASE | re.MULTILINE
                )
                if match:
                    self.window_id = match.group(1)
                    print(f"[+] 找到匹配窗口: {pattern}")
                    self.log_debug(f"窗口 ID: {self.window_id}")
                    return True

        print("[-] 未找到 EasyConnect 窗口")
        return False

    def wait_for_window(self, timeout=WINDOW_WAIT_TIMEOUT):
        """等待 EasyConnect 窗口出现"""
        print(f"[*] 等待 EasyConnect 窗口出现 (最多 {timeout} 秒)...")

        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.find_easyconnect_window():
                return True
            time.sleep(1)

        print("[-] 等待窗口超时")
        return False

    def activate_window(self):
        """激活 EasyConnect 窗口"""
        if not self.window_id:
            print("[-] 没有找到窗口 ID")
            return False

        print(f"[*] 激活窗口: {self.window_id}")

        try:
            # 方法1: 使用 xdotool 激活并提升窗口
            subprocess.run(
                ["xdotool", "windowactivate", "--sync", self.window_id],
                check=True
            )
            time.sleep(0.5)

            # 方法2: 使用 windowfocus 确保获得焦点
            subprocess.run(
                ["xdotool", "windowfocus", "--sync", self.window_id],
                check=True
            )
            time.sleep(0.5)

            # 方法3: 如果启用，点击窗口中央
            if CLICK_CENTER:
                # 获取窗口几何信息
                result = subprocess.run(
                    ["xdotool", "getwindowgeometry", self.window_id],
                    capture_output=True,
                    text=True
                )
                self.log_debug(f"窗口几何: {result.stdout}")

                # 提取窗口位置和大小
                x_match = re.search(r'Position:\s*(\d+),(\d+)', result.stdout)
                g_match = re.search(r'Geometry:\s*(\d+)x(\d+)', result.stdout)

                if x_match and g_match:
                    x = int(x_match.group(1)) + int(g_match.group(1)) // 2
                    y = int(x_match.group(2)) + int(g_match.group(2)) // 2
                    self.log_debug(f"点击坐标: ({x}, {y})")

                    # 移动鼠标到窗口中央并点击
                    subprocess.run(["xdotool", "mousemove", str(x), str(y)], check=True)
                    time.sleep(0.2)
                    subprocess.run(["xdotool", "click", "1"], check=True)
                    time.sleep(0.5)

                    # 再点击一次确保获得焦点
                    subprocess.run(["xdotool", "click", "1"], check=True)
                    time.sleep(0.5)

            # 方法4: 尝试使用 Alt+Tab 切换回来
            subprocess.run(["xdotool", "key", "Alt+Tab"], check=True)
            time.sleep(0.3)
            subprocess.run(["xdotool", "key", "Alt", "Tab"], check=True)
            time.sleep(0.3)

            print("[+] 窗口已激活")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[-] 激活窗口失败: {e}")
            return False

    def type_text_xdotool(self, text):
        """使用 xdotool 输入文本"""
        try:
            subprocess.run(
                ["xdotool", "type", "--delay", str(int(TYPING_INTERVAL * 1000)), text],
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            self.log_debug(f"xdotool 输入失败: {e}")
            return False

    def press_key_xdotool(self, key):
        """使用 xdotool 按键"""
        try:
            subprocess.run(["xdotool", "key", key], check=True)
            return True
        except subprocess.CalledProcessError as e:
            self.log_debug(f"xdotool 按键失败: {e}")
            return False

    def check_easyconnect_installed(self):
        """检查 EasyConnect 是否已安装"""
        possible_paths = [
            "/usr/share/sangfor/EasyConnect/EasyConnect",
            "/opt/EasyConnect/EasyConnect",
            "/usr/bin/EasyConnect",
            "/usr/local/bin/EasyConnect"
        ]

        for path in possible_paths:
            if os.path.exists(path):
                self.log_debug(f"找到 EasyConnect: {path}")
                return path

        return None

    def start_easyconnect(self):
        """启动 EasyConnect"""
        print("[*] 检查 EasyConnect 安装...")
        easyconnect_path = self.check_easyconnect_installed()

        if not easyconnect_path:
            print("[-] 未找到 EasyConnect，尝试使用默认路径...")
            easyconnect_path = EASYCONNECT_PATH

        # 检查工具
        if not self.check_xdotool():
            return False

        print(f"[*] 启动 EasyConnect: {easyconnect_path}")

        # 先关闭可能存在的实例
        self.kill_easyconnect()

        try:
            # 后台启动 EasyConnect
            process = subprocess.Popen(
                [easyconnect_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            self.easyconnect_pid = process.pid
            print(f"[+] EasyConnect 已启动 (PID: {process.pid})")

            # 等待窗口出现
            if self.wait_for_window():
                # 激活窗口
                if self.activate_window():
                    return True
                else:
                    print("[-] 无法激活窗口")
                    return False
            else:
                print("[-] 窗口未出现")
                return False

        except Exception as e:
            print(f"[-] 启动失败: {e}")
            return False

    def kill_easyconnect(self):
        """关闭所有 EasyConnect 进程"""
        self.log_debug("关闭现有 EasyConnect 进程...")
        subprocess.run(["pkill", "-f", "EasyConnect"], stderr=subprocess.DEVNULL)
        time.sleep(1)

    def login(self):
        """自动填写登录信息"""
        print("[*] 开始自动登录流程...")

        # 确保窗口激活
        if not self.activate_window():
            print("[-] 无法激活窗口，尝试继续...")
            # 尝试再次激活
            time.sleep(1)
            if not self.activate_window():
                print("[-] 窗口激活失败，使用备用方法")
                return False

        # 等待窗口完全加载
        print("  -> 等待窗口加载...")
        time.sleep(3)

        # 点击窗口中央确保获得焦点
        if CLICK_CENTER and self.window_id:
            try:
                result = subprocess.run(
                    ["xdotool", "getwindowgeometry", self.window_id],
                    capture_output=True,
                    text=True
                )
                x_match = re.search(r'Position:\s*(\d+),(\d+)', result.stdout)
                g_match = re.search(r'Geometry:\s*(\d+)x(\d+)', result.stdout)
                if x_match and g_match:
                    x = int(x_match.group(1)) + int(g_match.group(1)) // 2
                    y = int(x_match.group(2)) + int(g_match.group(2)) // 2
                    subprocess.run(["xdotool", "mousemove", str(x), str(y)], check=True)
                    time.sleep(0.2)
                    subprocess.run(["xdotool", "click", "1"], check=True)
                    time.sleep(0.5)
            except:
                pass

        # 先按 Esc 重置焦点状态，避免焦点落在错误的输入框
        self.press_key_xdotool('Escape')
        time.sleep(0.5)

        # 用 Shift+Tab 多次回退，确保焦点回到最前面的输入框（用户名）
        for _ in range(5):
            self.press_key_xdotool('shift+Tab')
            time.sleep(0.15)

        # 再 Tab 一次定位到第一个输入框（用户名框）
        self.press_key_xdotool('Tab')
        time.sleep(0.3)

        # 步骤 1: 输入用户名
        print("  -> 输入用户名...")

        # 清空可能的现有内容
        self.press_key_xdotool('Ctrl+a')
        time.sleep(0.2)
        self.press_key_xdotool('Delete')
        time.sleep(0.2)

        # 输入用户名
        if not self.type_text_xdotool(VPN_USERNAME):
            print("[-] 用户名输入失败")
            return False

        time.sleep(WAIT_BETWEEN_STEPS)

        # 步骤 2: Tab 到密码框并输入密码
        print("  -> 输入密码...")

        self.press_key_xdotool('Tab')
        time.sleep(0.5)

        # 清空可能的现有内容
        self.press_key_xdotool('Ctrl+a')
        time.sleep(0.2)
        self.press_key_xdotool('Delete')
        time.sleep(0.2)

        # 输入密码
        if not self.type_text_xdotool(VPN_PASSWORD):
            print("[-] 密码输入失败")
            return False

        time.sleep(WAIT_BETWEEN_STEPS)

        # 步骤 3: 点击登录按钮
        print("  -> 点击登录按钮...")

        self.press_key_xdotool('Return')
        time.sleep(2)

        print("[+] 登录操作已完成")

        # 登录后检查是否弹出密码重置对话框
        time.sleep(3)
        if self.detect_password_reset_dialog():
            print("[!] 检测到密码重置对话框")
            if ENABLE_PASSWORD_RESET:
                return self.handle_password_reset()
            else:
                print("[-] 密码重置处理未启用，请手动修改密码")
                return False

        return True

    def detect_password_reset_dialog(self):
        """检测是否出现了密码重置/修改对话框"""
        self.log_debug("检测是否出现密码重置对话框...")

        try:
            # 方法1: 通过窗口标题检测
            result = subprocess.run(
                ["xdotool", "search", "--onlyvisible", "--name", ".*"],
                capture_output=True,
                text=True
            )
            if result.stdout.strip():
                for wid in result.stdout.strip().split('\n'):
                    try:
                        name_result = subprocess.run(
                            ["xdotool", "getwindowname", wid],
                            capture_output=True,
                            text=True
                        )
                        win_name = name_result.stdout.strip()
                        for pattern in PASSWORD_RESET_PATTERNS:
                            if re.search(pattern, win_name, re.IGNORECASE):
                                self.log_debug(f"匹配到密码重置窗口: '{win_name}'")
                                self.window_id = wid
                                return True
                    except:
                        pass

            # 方法2: 使用 wmctrl 检测
            if self.check_wmctrl():
                wm_result = subprocess.run(
                    ["wmctrl", "-l"],
                    capture_output=True,
                    text=True
                )
                for pattern in PASSWORD_RESET_PATTERNS:
                    if re.search(pattern, wm_result.stdout, re.IGNORECASE):
                        self.log_debug(f"wmctrl 检测到密码重置窗口")
                        match = re.search(
                            r'^(0x[0-9a-f]+).*' + pattern,
                            wm_result.stdout,
                            re.IGNORECASE | re.MULTILINE
                        )
                        if match:
                            self.window_id = match.group(1)
                        return True

        except Exception as e:
            self.log_debug(f"检测密码重置对话框出错: {e}")

        return False

    def generate_new_password(self, old_password):
        """根据旧密码生成新密码（在末尾数字上递增）"""
        match = re.search(r'^(.*?)(\d+)$', old_password)
        if match:
            prefix = match.group(1)
            num = int(match.group(2))
            new_num = num + 1
            return f"{prefix}{new_num}"
        else:
            return old_password + '1'

    def handle_password_reset(self):
        """处理密码重置对话框"""
        global VPN_PASSWORD

        new_password = VPN_NEW_PASSWORD if VPN_NEW_PASSWORD else self.generate_new_password(VPN_PASSWORD)
        print(f"[*] 开始处理密码重置...")
        print(f"  -> 新密码: {new_password[:2]}{'*' * (len(new_password) - 2)}")

        # 激活密码重置窗口
        self.activate_window()
        time.sleep(1)

        # 重置焦点到第一个输入框
        self.press_key_xdotool('Escape')
        time.sleep(0.3)
        for _ in range(5):
            self.press_key_xdotool('shift+Tab')
            time.sleep(0.15)
        self.press_key_xdotool('Tab')
        time.sleep(0.3)

        # 输入旧密码
        print("  -> 输入旧密码...")
        self.press_key_xdotool('Ctrl+a')
        time.sleep(0.2)
        self.press_key_xdotool('Delete')
        time.sleep(0.2)
        self.type_text_xdotool(VPN_PASSWORD)
        time.sleep(0.5)

        # Tab 到新密码框
        self.press_key_xdotool('Tab')
        time.sleep(0.3)

        # 输入新密码
        print("  -> 输入新密码...")
        self.press_key_xdotool('Ctrl+a')
        time.sleep(0.2)
        self.press_key_xdotool('Delete')
        time.sleep(0.2)
        self.type_text_xdotool(new_password)
        time.sleep(0.5)

        # Tab 到确认密码框
        self.press_key_xdotool('Tab')
        time.sleep(0.3)

        # 输入确认密码
        print("  -> 输入确认密码...")
        self.press_key_xdotool('Ctrl+a')
        time.sleep(0.2)
        self.press_key_xdotool('Delete')
        time.sleep(0.2)
        self.type_text_xdotool(new_password)
        time.sleep(0.5)

        # 提交
        print("  -> 提交密码修改...")
        self.press_key_xdotool('Return')
        time.sleep(3)

        # 更新内存中的密码
        old_password = VPN_PASSWORD
        VPN_PASSWORD = new_password
        print(f"[+] 密码已更新（内存）")

        # 将新密码写入配置文件，方便下次使用
        self.save_new_password(new_password, old_password)

        # 密码修改后可能需要重新登录
        time.sleep(2)
        if self.detect_password_reset_dialog():
            print("[-] 密码重置似乎未成功（对话框仍存在）")
            VPN_PASSWORD = old_password
            return False

        print("[+] 密码重置完成，尝试重新登录...")
        time.sleep(2)

        # 检查是否需要重新登录
        if not self.check_vpn_connection():
            if self.find_easyconnect_window():
                self.activate_window()
                time.sleep(1)
                return self.login()

        return True

    def save_credentials(self):
        """登录成功后，将当前账号密码记录到 vpn_pass.txt"""
        try:
            pass_file = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'vpn_pass.txt'
            )
            login_time = time.strftime('%Y-%m-%d %H:%M:%S')
            entry = f"[{login_time}] username={VPN_USERNAME} password={VPN_PASSWORD}\n"

            # 追加写入，保留历史记录
            with open(pass_file, 'a', encoding='utf-8') as f:
                f.write(entry)

            print(f"[+] 登录凭证已记录到: {pass_file}")
        except Exception as e:
            print(f"[-] 保存登录凭证失败: {e}")

    def save_new_password(self, new_password, old_password):
        """密码重置后，更新脚本和凭证文件中的密码"""
        try:
            # 更新本脚本文件中的 VPN_PASSWORD
            script_path = os.path.abspath(__file__)
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()

            updated = content.replace(
                f"VPN_PASSWORD = '{old_password}'",
                f"VPN_PASSWORD = '{new_password}'"
            )
            if updated == content:
                updated = content.replace(
                    f'VPN_PASSWORD = "{old_password}"',
                    f'VPN_PASSWORD = "{new_password}"'
                )

            if updated != content:
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(updated)
                print(f"[+] 脚本文件中的密码已更新: {script_path}")

        except Exception as e:
            print(f"[-] 保存新密码失败: {e}")
            print(f"[!] 请手动更新密码为: {new_password}")

    def login_with_pyautogui(self):
        """使用 pyautogui 的备用登录方法"""
        print("[*] 使用 pyautogui 备用方法...")

        try:
            import pyautogui

            # 先按 Esc 重置焦点
            pyautogui.press('escape')
            time.sleep(0.5)

            # Shift+Tab 多次回退到最前面
            for _ in range(5):
                pyautogui.hotkey('shift', 'tab')
                time.sleep(0.15)

            # Tab 一次定位到用户名输入框
            pyautogui.press('tab')
            time.sleep(0.3)

            # 输入用户名
            print("  -> 输入用户名...")
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(VPN_USERNAME, interval=TYPING_INTERVAL)
            time.sleep(0.5)

            # Tab 到密码框
            pyautogui.press('tab')
            time.sleep(0.5)

            # 输入密码
            print("  -> 输入密码...")
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.write(VPN_PASSWORD, interval=TYPING_INTERVAL)
            time.sleep(0.5)

            # 点击登录
            print("  -> 点击登录按钮...")
            pyautogui.press('enter')
            time.sleep(2)

            return True

        except ImportError:
            print("[-] pyautogui 未安装")
            return False

    def wait_for_connection(self, timeout=60):
        """等待 VPN 连接成功"""
        print(f"[*] 等待 VPN 连接建立 (最多 {timeout} 秒)...")

        for i in range(timeout):
            # 检查网络连接状态
            if self.check_vpn_connection():
                print("[+] VPN 连接成功!")
                self.is_connected = True
                return True
            time.sleep(1)

        print("[-] VPN 连接超时")
        return False

    def check_vpn_connection(self):
        """检查 VPN 是否已连接（通过 ping 172.20.1.217）"""
        try:
            # 主要方法: ping 内网地址
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "2", "172.20.1.217"],
                capture_output=True
            )

            if result.returncode == 0:
                self.log_debug(f"Ping 172.20.1.217 成功")
                return True
            else:
                self.log_debug(f"Ping 172.20.1.217 失败")

            # 备用方法: 检查 tun/tap 接口
            result2 = subprocess.run(
                ["ip", "link", "show"],
                capture_output=True,
                text=True
            )
            if "tun" in result2.stdout or "tap" in result2.stdout:
                self.log_debug("检测到 tun/tap 接口")
                return True

        except Exception as e:
            self.log_debug(f"检查连接失败: {e}")

        return False

    def close_easyconnect(self):
        """关闭 EasyConnect"""
        print("[*] 关闭 EasyConnect...")
        self.kill_easyconnect()
        print("[+] EasyConnect 已关闭")

    def reconnect(self):
        """重新连接 VPN"""
        print(f"\n{'='*50}")
        print("[*] 检测到 VPN 断开，开始重新连接...")
        print(f"{'='*50}\n")

        # 关闭现有进程
        self.kill_easyconnect()
        time.sleep(2)

        # 重置状态
        self.is_connected = False
        self.window_id = None
        self.easyconnect_pid = None

        # 重新启动并登录
        if not self.start_easyconnect():
            print("[-] 重新启动 EasyConnect 失败")
            return False

        if not self.login():
            print("[-] 重新登录失败")
            return False

        if not self.wait_for_connection():
            print("[-] 重新连接超时")
            return False

        print("\n[+] 重新连接成功!")
        self.save_credentials()
        return True

    def monitor_connection(self):
        """监控 VPN 连接状态，断开时自动重连"""
        if not ENABLE_MONITOR:
            print("[*] 监控功能未启用")
            return

        print(f"\n{'='*50}")
        print(f"[*] VPN 监控已启动 (检查间隔: {MONITOR_INTERVAL} 秒)")
        print(f"[*] 按 Ctrl+C 停止监控")
        print(f"{'='*50}\n")

        reconnect_count = 0
        last_connected = True

        while True:
            try:
                # 检查连接状态
                current_status = self.check_vpn_connection()

                if current_status:
                    if not last_connected:
                        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [+] VPN 已连接")
                        last_connected = True
                        reconnect_count = 0
                else:
                    if last_connected:
                        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [-] VPN 已断开!")
                        last_connected = False

                    # 检查重连次数
                    if reconnect_count < MAX_RECONNECT_ATTEMPTS:
                        reconnect_count += 1
                        print(f"[*] 尝试重连 ({reconnect_count}/{MAX_RECONNECT_ATTEMPTS})...")
                        time.sleep(RECONNECT_DELAY)

                        if self.reconnect():
                            last_connected = True
                            reconnect_count = 0
                        else:
                            print(f"[-] 重连失败 ({reconnect_count}/{MAX_RECONNECT_ATTEMPTS})")
                    else:
                        print(f"[-] 已达到最大重连次数 ({MAX_RECONNECT_ATTEMPTS})，停止监控")
                        break

                # 等待下次检查
                time.sleep(MONITOR_INTERVAL)

            except KeyboardInterrupt:
                print(f"\n[!] 用户中断监控")
                break
            except Exception as e:
                print(f"\n[-] 监控过程出错: {e}")
                import traceback
                traceback.print_exc()
                time.sleep(5)  # 出错后等待一段时间再继续


def setup_requirements():
    """检查并安装必要的依赖"""
    print("[*] 检查系统依赖...")

    # 检查 xdotool
    try:
        subprocess.run(["which", "xdotool"], check=True, capture_output=True)
        print("[+] xdotool 已安装")
    except subprocess.CalledProcessError:
        print("[*] 安装 xdotool...")
        subprocess.run(["sudo", "apt", "install", "-y", "xdotool"], check=True)

    # 检查 wmctl
    try:
        subprocess.run(["which", "wmctrl"], check=True, capture_output=True)
        print("[+] wmctrl 已安装")
    except subprocess.CalledProcessError:
        print("[*] 安装 wmctrl...")
        subprocess.run(["sudo", "apt", "install", "-y", "wmctrl"], check=True)

    print("[+] 依赖检查完成\n")


def main():
    print("="*60)
    print("EasyConnect 自动登录 & 监控工具")
    print("Ubuntu 24.04")
    print("="*60 + "\n")

    # 检查依赖
    try:
        setup_requirements()
    except Exception as e:
        print(f"[-] 依赖安装失败: {e}")
        return 1

    # 创建实例
    client = EasyConnectAutoLogin()

    try:
        # ====== 优先检测现有状态 ======
        print("[*] 检测当前状态...")

        # 检查 VPN 是否已连接
        if client.check_vpn_connection():
            print("[+] VPN 已连接，无需重新登录")
            # 直接进入监控模式
            if ENABLE_MONITOR:
                client.is_connected = True
                client.monitor_connection()
            else:
                print("[*] 监控功能未启用，脚本退出")
            return 0

        # VPN 未连接，检查 EasyConnect 是否在运行
        easyconnect_running = False
        try:
            result = subprocess.run(
                ["pgrep", "-f", "EasyConnect"],
                capture_output=True,
                text=True
            )
            if result.stdout.strip():
                easyconnect_running = True
                pids = result.stdout.strip().split('\n')
                print(f"[+] EasyConnect 进程已在运行 (PID: {', '.join(pids)})")
        except Exception:
            pass

        if easyconnect_running:
            # 进程在运行但 VPN 未连接，尝试找到窗口并登录
            print("[*] EasyConnect 已运行但 VPN 未连接，尝试登录...")
            if client.find_easyconnect_window():
                if client.activate_window():
                    time.sleep(1)
                    if not client.login():
                        print("登录失败，尝试备用方法...")
                        if not client.login_with_pyautogui():
                            print("所有登录方法都失败了，将重启 EasyConnect...")
                            easyconnect_running = False
                else:
                    print("[-] 无法激活现有窗口，将重启 EasyConnect...")
                    easyconnect_running = False
            else:
                print("[-] 未找到 EasyConnect 窗口，将重启 EasyConnect...")
                easyconnect_running = False

        # ====== 需要全新启动 ======
        if not easyconnect_running:
            print("[*] 启动 EasyConnect...")
            if not client.start_easyconnect():
                print("无法启动 EasyConnect，请手动启动后重试")
                return 1

            if not client.login():
                print("登录失败，尝试备用方法...")
                if not client.login_with_pyautogui():
                    print("所有登录方法都失败了")
                    return 1

        # 等待连接
        if not client.wait_for_connection():
            print("VPN 连接未建立")
            return 1

        print("\n[+] EasyConnect 自动登录完成!")

        # 登录成功，记录账号密码
        client.save_credentials()

        # 启动监控模式
        if ENABLE_MONITOR:
            client.monitor_connection()
        else:
            print("[*] 监控功能未启用，脚本退出")

        return 0

    except KeyboardInterrupt:
        print("\n[!] 用户中断，脚本退出（EasyConnect 保持运行）")
        return 130
    except Exception as e:
        print(f"\n[-] 发生错误: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
