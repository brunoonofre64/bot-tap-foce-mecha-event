from cx_Freeze import setup, Executable
import os


# ============================================================
# COLETAR TODOS OS ARQUIVOS DA PASTA images/
# ============================================================
include_files = []

IMAGES_DIR = "images"

if os.path.isdir(IMAGES_DIR):
    for f in os.listdir(IMAGES_DIR):
        full = os.path.join(IMAGES_DIR, f)
        if os.path.isfile(full) and f.lower().endswith((".png", ".jpg", ".jpeg")):
            include_files.append((full, os.path.join(IMAGES_DIR, f)))


# ============================================================
# CONFIGURAÇÕES DE BUILD
# ============================================================
build_options = {
    "packages": ["cv2", "numpy", "pyautogui", "PIL"],
    "include_files": include_files,
    "include_msvcr": True,
}


# ============================================================
# SETUP FINAL
# ============================================================
setup(
    name="TapForceBot",
    version="1.0",
    description="Bot TapForce",
    options={"build_exe": build_options},
    executables=[Executable("main.py", base=None)]
)
