# ethics_rules.py

rules = {
    "Mind": {"transform": ["Idea", "Body"]},
    "Body": {"transform": ["Motion"]},
    "Motion": {"transform": []},
    "Idea": {"transform": ["Cause", "Effect"]},
    "Cause": {"transform": []},
    "Effect": {"transform": []},
    "Emotion": {"transform": ["Idea"]},
    "Bondage": {"transform": ["Emotion", "Emotion"]},
    "Freedom": {"transform": ["AdequateIdea"]},
    "AdequateIdea": {"transform": ["Cause"]}
}
