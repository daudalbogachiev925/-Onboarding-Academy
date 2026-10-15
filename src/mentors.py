from dataclasses import dataclass, field

@dataclass
class Mentor:
    id: str
    name: str
    specialization: list
    max_mentees: int = 3
    current_mentees: list = field(default_factory=list)
    timezone: str = "MSK"

def assign_mentor(mentors, junior, preferred_spec=None):
    candidates = []
    for m in mentors:
        if len(m.current_mentees) >= m.max_mentees:
            continue
        if preferred_spec and preferred_spec not in m.specialization:
            continue
        candidates.append(m)
    if not candidates:
        return None
    candidates.sort(key=lambda m: len(m.current_mentees))
    mentor = candidates[0]
    mentor.current_mentees.append(junior)
    return mentor

def match_by_skill(mentors, skill):
    return [m for m in mentors if skill in m.specialization and
            len(m.current_mentees) < m.max_mentees]

def mentor_stats(mentors):
    return [{
        "id": m.id,
        "name": m.name,
        "specialization": m.specialization,
        "load": f"{len(m.current_mentees)}/{m.max_mentees}",
        "available": m.max_mentees - len(m.current_mentees),
    } for m in mentors]
