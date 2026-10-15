import json
from pathlib import Path
from src.progress import UserProgress, LessonProgress

class ProgressStorage:
    def __init__(self, folder="progress"):
        self.folder = Path(folder)
        self.folder.mkdir(exist_ok=True)

    def save(self, up: UserProgress):
        path = self.folder / f"{up.user_id}.json"
        data = {
            "user_id": up.user_id,
            "track": up.track,
            "enrolled_at": up.enrolled_at,
            "lessons": {k: lp.__dict__ for k, lp in up.lessons.items()},
            "quiz_results": up.quiz_results,
        }
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                        encoding="utf-8")
        return path

    def load(self, user_id):
        path = self.folder / f"{user_id}.json"
        if not path.exists():
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        up = UserProgress(user_id=data["user_id"], track=data["track"])
        up.enrolled_at = data["enrolled_at"]
        up.lessons = {k: LessonProgress(**v) for k, v in data["lessons"].items()}
        up.quiz_results = data["quiz_results"]
        return up

    def list_users(self):
        return [p.stem for p in self.folder.glob("*.json")]
