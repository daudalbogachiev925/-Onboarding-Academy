from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class LessonProgress:
    lesson_id: str
    status: str = "not_started"  # not_started, in_progress, completed
    started_at: str = ""
    completed_at: str = ""
    time_spent_min: int = 0

@dataclass
class UserProgress:
    user_id: str
    track: str
    lessons: dict = field(default_factory=dict)
    quiz_results: list = field(default_factory=list)
    enrolled_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def start_lesson(self, lesson_id):
        lp = self.lessons.setdefault(lesson_id, LessonProgress(lesson_id))
        lp.status = "in_progress"
        lp.started_at = datetime.utcnow().isoformat()

    def complete_lesson(self, lesson_id, time_min=0):
        lp = self.lessons.setdefault(lesson_id, LessonProgress(lesson_id))
        lp.status = "completed"
        lp.completed_at = datetime.utcnow().isoformat()
        lp.time_spent_min += time_min

    def add_quiz_result(self, quiz_id, score, passed):
        self.quiz_results.append({
            "quiz_id": quiz_id,
            "score": score,
            "passed": passed,
            "taken_at": datetime.utcnow().isoformat(),
        })

    def completion_pct(self, total_lessons):
        if total_lessons == 0:
            return 0
        done = sum(1 for lp in self.lessons.values() if lp.status == "completed")
        return round(done / total_lessons * 100, 1)

    def quiz_avg(self):
        if not self.quiz_results:
            return 0
        return round(sum(q["score"] for q in self.quiz_results) / len(self.quiz_results), 1)
