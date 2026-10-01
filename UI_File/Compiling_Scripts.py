from pathlib import Path
import subprocess
import sys

def Compile_ALL():
    BASE_DIR = Path(__file__).resolve().parent

    # Folder hasil compile
    OUTPUT_DIR = BASE_DIR / "Compiled"
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Cari semua file .ui di direktori utama
    ui_files = BASE_DIR.glob("*.ui")

    for ui_file in ui_files:
        output_file = OUTPUT_DIR / f"{ui_file.stem}.py"

        print(f"Compiling: {ui_file.name} -> Compiled/{output_file.name}")

        subprocess.run(
            [
                "pyside6-uic",
                str(ui_file),
                "-o",
                str(output_file),
            ],
            check=True
        )

print("Compilation selesai.")
