from dataclasses import dataclass, field

@dataclass
class Question:
    id: str
    text: str
    options: list
    correct: int
    explanation: str = ""

@dataclass
class Quiz:
    id: str
    title: str
    track: str
    questions: list
    passing_score: int = 80

QUIZZES = [
    Quiz("q_junior_1", "Основы 1С", "junior", [
        Question("q1", "Что такое Конфигуратор?", [
            "Среда разработки 1С",
            "Клиентское приложение",
            "Сервер базы данных",
            "Веб-сервер",
        ], 0, "Конфигуратор — основная среда разработки"),
        Question("q2", "Какой тип реквизита ссылается на другой объект?", [
            "Строка",
            "Число",
            "СправочникСсылка",
            "Булево",
        ], 2),
        Question("q3", "Что делает директива &НаСервере?", [
            "Выполняет код на клиенте",
            "Выполняет код на сервере",
            "Компилирует модуль",
            "Блокирует данные",
        ], 1),
    ]),
    Quiz("q_middle_1", "Архитектура", "middle", [
        Question("q1", "Что такое расширение конфигурации?", [
            "Дополнительный модуль",
            "Механизм доработки без изменения типовой",
            "Внешний отчёт",
            "Плагин EDT",
        ], 1),
        Question("q2", "Какой HTTP-метод идемпотентен?", [
            "POST", "GET", "PATCH", "CONNECT",
        ], 1),
    ]),
]

def get_quiz(quiz_id):
    return next((q for q in QUIZZES if q.id == quiz_id), None)

def list_quizzes(track=None):
    if track:
        return [q for q in QUIZZES if q.track == track]
    return QUIZZES

def evaluate(quiz, answers):
    correct = 0
    details = []
    for q, a in zip(quiz.questions, answers):
        ok = a == q.correct
        correct += int(ok)
        details.append({
            "question": q.text,
            "your_answer": q.options[a] if 0 <= a < len(q.options) else "?",
            "correct": q.options[q.correct],
            "ok": ok,
        })
    score = round(correct / len(quiz.questions) * 100, 1)
    return {
        "score": score,
        "passed": score >= quiz.passing_score,
        "correct": correct,
        "total": len(quiz.questions),
        "details": details,
    }
