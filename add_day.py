from pathlib import Path
import shutil

YEAR = "2015"
DAY = "16"

source_dir: Path = Path("./template/")
py_files = ["AoC_YEAR_DAY_test.py", "AoC_YEAR_DAY.py"]
txt_files = ["example.txt", "input.txt"]


def main(year: str, day: str) -> None:
    create_target_directories(year, day)
    copy_template_files(year, day)


def create_target_directories(year: str, day: str) -> None:
    target_dir = Path(year) / day
    target_dir.mkdir(parents=True, exist_ok=True)


def copy_template_files(year: str, day: str) -> None:
    target_dir: Path = Path(year) / day
    files = py_files + txt_files
    for file in files:
        source_path: Path = source_dir / file
        target_path: Path = target_dir / file
        # Rename target path names before copying the files
        target_filename = file.replace("YEAR", year).replace("DAY", day)
        target_path = target_dir / target_filename
        print(f"[DEBUG] [{source_path}], [{target_path}]")
        if not target_path.exists():
            shutil.copy(source_path, target_path)
            update_file_contents(target_path, year, day)


def update_file_contents(filepath: Path, year: str, day: str) -> None:
    content = filepath.read_text()
    content = content.replace("YEAR", year)
    content = content.replace("DAY", day)
    filepath.write_text(content)


if __name__ == "__main__":
    main(YEAR, DAY)
