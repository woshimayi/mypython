# -*- mode: python -*-

block_cipher = None


a = Analysis(['exec_timeview.py'],
             pathex=['D:\\python27\\win_api'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='exec_timeview',
          debug=False,
          strip=False,
          upx=True,
          console=True )