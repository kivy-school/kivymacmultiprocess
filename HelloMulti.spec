# -*- mode: python ; coding: utf-8 -*-
# from kivy_deps import sdl2, glew

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

    #*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='HelloMulti',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app= BUNDLE(
    exe, 
    name = 'Hello Multiprocessing Mac test.app',
    icon = None,
    bundle_identifier=None,
)