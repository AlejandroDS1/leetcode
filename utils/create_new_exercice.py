import os
import re
import sys
from pathlib import Path


DIFFICULTY_MAP = {
    1: ("easy", "🟢 Easy"),
    2: ("medium", "🟡 Medium"),
    3: ("hard", "🔴 Hard"),
}


def parse_problem(input_string: str):
    """
    "3. Two Sum" -> (3, "Two Sum")
    """
    match = re.match(r"^\s*(\d+)\.\s*(.+)$", input_string)
    if not match:
        raise ValueError("Formato inválido. Usa: '3. Two Sum'")
    number = int(match.group(1))
    title = match.group(2).strip()
    return number, title


def format_folder_name(number: int, title: str) -> str:
    """
    3, "Two Sum" -> "3-Two_Sum"
    """
    return f"{number}-{title.replace(' ', '_')}"


def format_file_name(title: str) -> str:
    """
    "Two Sum" -> "Two_sum.py"
    """
    words = title.split()
    if not words:
        raise ValueError("Título vacío")

    first = words[0].capitalize()
    rest = "_".join(w.lower() for w in words[1:])
    return f"{first}" + (f"_{rest}" if rest else "") + ".py"


def create_structure(base_path: Path, difficulty_folder: str, folder_name: str, file_name: str):
    problem_path = base_path / difficulty_folder / folder_name
    problem_path.mkdir(parents=True, exist_ok=False)

    file_path = problem_path / file_name
    file_path.touch()

    return problem_path, file_path


def build_readme_row(number: int, title: str, difficulty_label: str, difficulty_folder: str, folder_name: str, file_name: str):
    leetcode_slug = title.lower().replace(" ", "-")
    url = f"https://leetcode.com/problems/{leetcode_slug}/"

    return (
        f"| {difficulty_label} | {number} | "
        f"[{title}]({url}) | "
        f"[Python]({difficulty_folder}/{folder_name}/{file_name}) |\n"
    )


def insert_into_readme(readme_path: Path, difficulty_label: str, new_row: str):
    lines = readme_path.read_text(encoding="utf-8").splitlines(keepends=True)

    last_index = None
    for i, line in enumerate(lines):
        if line.startswith(f"| {difficulty_label}"):
            last_index = i

    if last_index is None:
        raise ValueError("No se encontró sección de esa dificultad en README")

    lines.insert(last_index + 1, new_row)
    readme_path.write_text("".join(lines), encoding="utf-8")


def main():
    if len(sys.argv) != 3:
        print("Uso: python create_problem.py \"3. Two Sum\" 1")
        sys.exit(1)

    raw_problem = sys.argv[1]
    difficulty_input = int(sys.argv[2])

    if difficulty_input not in DIFFICULTY_MAP:
        raise ValueError("Dificultad inválida: 1=Easy, 2=Medium, 3=Hard")

    difficulty_folder, difficulty_label = DIFFICULTY_MAP[difficulty_input]

    number, title = parse_problem(raw_problem)

    folder_name = format_folder_name(number, title)
    file_name = format_file_name(title)

    base_path = Path.cwd()

    create_structure(base_path, difficulty_folder, folder_name, file_name)

    readme_path = base_path / "README.md"
    new_row = build_readme_row(
        number,
        title,
        difficulty_label,
        difficulty_folder,
        folder_name,
        file_name,
    )

    insert_into_readme(readme_path, difficulty_label, new_row)

    print("Problema creado correctamente.")


if __name__ == "__main__":
    main()