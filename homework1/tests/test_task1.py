from subprocess import run
from pathlib import Path

def test_task1():
    task1_path = Path(__file__).parent.parent / "src" / "task1.py"
    out = run(["python3", task1_path], capture_output=True, text=True)
    assert out.stdout == "Hello, World!\n"