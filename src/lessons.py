from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class Lesson:
    id: str
    title: str
    track: str
    content: str
    duration_min: int
    tags: list = field(default_factory=list)

def load_lesson(path):
    text = Path(path).read_text(encoding="utf-8")
    lines = text.split("\n")
    title = lines[0].lstrip("# ").strip() if lines else "Untitled"
    return Lesson(
        id=Path(path).stem,
        title=title,
        track=Path(path).parent.name,
        content=text,
        duration_min=30,
    )

def load_track_lessons(track_folder):
    folder = Path("content") / track_folder
    if not folder.exists():
        return []
    return [load_lesson(p) for p in sorted(folder.glob("*.md"))]

def get_lesson(track, lesson_id):
    folder = Path("content") / track
    path = folder / f"{lesson_id}.md"
    if not path.exists():
        return None
    return load_lesson(path)
