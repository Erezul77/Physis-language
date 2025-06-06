# spinoza_rules.py

rules = {
    "Substance": {"transform": ["Thought", "Extension"]},
    "Thought": {"transform": ["Idea", "Emotion"]},
    "Extension": {"transform": ["Body", "Motion"]},
    "Idea": {"transform": ["Idea", "Emotion"]},
    "Emotion": {"transform": []},
    "Body": {"transform": ["Motion"]},
    "Motion": {"transform": []}
}
