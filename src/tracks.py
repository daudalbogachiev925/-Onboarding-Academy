from dataclasses import dataclass, field
from enum import Enum

class TrackLevel(str, Enum):
    JUNIOR = "junior"
    MIDDLE = "middle"
    SENIOR = "senior"

@dataclass
class Track:
    level: TrackLevel
    title: str
    description: str
    duration_weeks: int
    lessons: list = field(default_factory=list)
    prerequisites: list = field(default_factory=list)
    outcomes: list = field(default_factory=list)

TRACKS = [
    Track(
        level=TrackLevel.JUNIOR,
        title="Junior 1C Developer",
        description="Основы платформы, конфигуратор, запросы",
        duration_weeks=8,
        lessons=["lesson_01_intro", "lesson_02_config", "lesson_03_queries"],
        outcomes=[
            "Работа в Конфигураторе и EDT",
            "Создание справочников, документов, регистров",
            "Простые запросы и отчёты",
            "Основы отладки",
        ],
    ),
    Track(
        level=TrackLevel.MIDDLE,
        title="Middle 1C Developer",
        description="Архитектура, интеграции, производительность",
        duration_weeks=12,
        lessons=["lesson_01_architecture", "lesson_02_integrations", "lesson_03_performance"],
        prerequisites=["junior"],
        outcomes=[
            "Проектирование подсистем",
            "HTTP-сервисы и интеграции",
            "Оптимизация запросов",
            "Расширения и СКД",
        ],
    ),
    Track(
        level=TrackLevel.SENIOR,
        title="Senior 1C Developer / Team Lead",
        description="Управление командой, архитектура, менторинг",
        duration_weeks=16,
        lessons=["lesson_01_team_lead", "lesson_02_arch_patterns", "lesson_03_mentoring"],
        prerequisites=["middle"],
        outcomes=[
            "Управление командой",
            "Архитектурные решения",
            "Code review и стандарты",
            "Менторинг junior/middle",
        ],
    ),
]

def get_track(level):
    return next((t for t in TRACKS if t.level == level), None)

def list_tracks():
    return TRACKS
