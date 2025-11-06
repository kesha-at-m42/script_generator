"""
Metadata Mapper
Maps input sequence fields to Godot mastery metadata structure
"""

def map_to_mastery_metadata(sequence):
    """
    Map input sequence fields to new mastery metadata structure
    
    Args:
        sequence: Input sequence with problem_id, difficulty, verb, goal, goal_id, fractions
        
    Returns:
        dict: Metadata structure for Godot schema with:
            - @type: "SequenceMetadata"
            - mastery_tier: str ("0"-"4", maps from difficulty)
            - mastery_component: str ("PROCEDURAL" or "CONCEPTUAL" or "TRANSFER)
            - mastery_verb: str (Bloom's taxonomy verb)
            - goal_id: int
            - goal_text: str
            - variables_covered: dict with fractions list
    
    Examples:
        >>> seq = {"difficulty": 2, "verb": "CREATE", "goal_id": 1,
        ...        "goal": "Student can partition", "fractions": ["1/4"]}
        >>> metadata = map_to_mastery_metadata(seq)
        >>> metadata["mastery_tier"]
        '2'
        >>> metadata["mastery_component"]
        'PROCEDURAL'
    """
    difficulty = sequence.get('difficulty', 0)
    verb = sequence.get('verb', 'CREATE')
    goal_id = sequence.get('goal_id', 1)
    goal_text = sequence.get('goal', '')
    fractions = sequence.get('fractions', [])
    
    # Map difficulty → mastery_tier (EMasteryTiers enum)
    # Mapping:
    #   0-1: BASELINE (Core assessment, standard difficulty)
    #   2: STRETCH (Extended assessment, moderately difficult)
    #   3-4: CHALLENGE (Above-grade exploration, for high performers)
    #   Note: SUPPORT and CONFIDENCE are dynamically assigned based on student performance
    if difficulty <= 1:
        mastery_tier = "BASELINE"
    elif difficulty == 2:
        mastery_tier = "STRETCH"
    elif difficulty >= 3:
        mastery_tier = "CHALLENGE"
    else:
        mastery_tier = "BASELINE"  # default
    
    # Map verb → mastery_component
    procedural_verbs = ['CREATE']
    conceptual_verbs = ['IDENTIFY', 'COMPARE']
    transfer_verbs = ['TRANSFER', 'CONNECT']

    if verb in procedural_verbs:
        mastery_component = "PROCEDURAL"
    elif verb in conceptual_verbs:
        mastery_component = "CONCEPTUAL"
    elif verb in transfer_verbs:
        mastery_component = "TRANSFER"
    else:
        mastery_component = "PROCEDURAL"  # default
    
    # Map verb → mastery_verbs array (Bloom's taxonomy)
    mastery_verbs = [str(verb)]
    
    return {
        "@type": "SequenceMetadata",
        "mastery_tier": str(mastery_tier),
        "mastery_component": mastery_component,
        "mastery_verbs": mastery_verbs,
        "goal_id": goal_id,
        "goal_text": goal_text,
        "variables_covered": {"fractions": fractions}
    }