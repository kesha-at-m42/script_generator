# **Universal Mastery Tracking	 Framework v3.0**

*Production Ready with Phased Implementation*

## **📊 CURRENT STATUS**

```
ACTIVE PHASE: Phase 1 - Simple Scoring
STATUS: Testing internally
TRACKING: Full component data collection active

ROUTING VERSION: 2.0
- Exit Check: 1/3 triggers intervention
- Practice: Max 2 attempts before path switch
- Adaptive: 2 wrong in row → SUPPORT problem
- No Early Exit: Must complete all problems
```

### **Quick Reference: What's Active Now vs. Coming**

| Feature | Phase 1 (NOW) | Phase 2 (FUTURE) |
| ----- | ----- | ----- |
| **Pass Threshold** | 70% overall | 70% \+ components |
| **Transfer Gate** | 1+ correct required | 1+ correct required |
| **Component Minimums** | Tracked only | 60% enforced |
| **Weights** | N/A | Module-specific |
| **Intervention** | Basic routing | Precision targeting |
| **Exit Check Routing** | 1/3 → intervention | Same (validated) |
| **Practice Attempts** | 2 before switch | 2-3 (data-driven) |
| **Adaptive Support** | 2 wrong → easier | Enhanced patterns |
| **Early Exit** | Never (anti-gaming) | Never (maintained) |

---

## **Executive Summary**

This framework provides a scalable, pedagogically-sound system for tracking student mastery across all subjects and grades. It uses universal components for consistent measurement while allowing domain-specific language that teachers understand.

**Core Innovation:** Domain-authentic cognitive verbs map to universal mastery components, enabling both pedagogical flexibility and standardized reporting.

### **Implementation Strategy: Phased Rollout**

We're deploying this framework in two phases to ensure data-driven validation:

**Phase 1 (Current): Simple Scoring**

* 70% accuracy threshold for mastery  
* Track all component data in background  
* Validate core assumptions with real students  
* Timeline: Internal testing period

**Phase 2 (Target): Full Component System**

* Component-based scoring with weights  
* Precision intervention routing  
* Stakeholder translations  
* Timeline: After validation 

This phased approach allows us to ship quickly while ensuring our sophisticated framework is validated by actual student data rather than assumptions.

### **What We're Building Now**

* Component-based mastery tracking for Grade 3 Fractions  
* 4 practical intervention types

### **Future Vision**

* Expansion to all Grade 3 Math, then English  
* Predictive analytics and clustering  
* Full teacher dashboards

---

## **Architecture Overview**

### **Three-Layer System**

```
LAYER 1: Universal Components (Constant)
    ↓ maps to ↓
LAYER 2: Domain-Specific Verbs (Flexible)
    ↓ produces ↓
LAYER 3: Stakeholder Translations (Contextual)
```

---

## **Phased Implementation Approach**

### **Phase 1: Simple Scoring (Active During Testing)**

**Purpose:** Validate core pedagogy with minimal complexity

**What We're Doing:**

```
MASTERY REQUIREMENTS:
- 70% correct on BASELINE/STRETCH problems
- At least 1 TRANSFER problem correct (APPLY or CONNECT)
- Minimum 6 attempts for validity

INTERVENTION ROUTING:
- Exit Check: 1/3 or less → Intervention options
- Practice Attempt 1: <70% → Try once more
- Practice Attempt 2: <70% → Auto path switch
```

**What We're Tracking (for Phase 2):**

* All component breakdowns  
* Cognitive verb distribution  
* Time and attempt patterns  
* Tool usage diagnostics

### **Phase 2: Component System (Production Target)**

**Purpose:** Provide precise diagnostics and targeted interventions

**Enhanced Requirements:**

```
MASTERY REQUIREMENTS:
- 70% overall on BASELINE/STRETCH
- PLUS each component ≥ 60%:
  - PROCEDURAL (execution)
  - CONCEPTUAL (understanding)
  - TRANSFER (application)
- At least 1 TRANSFER problem correct (gate)
- Weighted scoring by module level
```

### **Migration Criteria**

Move from Phase 1 → Phase 2 when:

* ✓ 70% threshold validated as predictive  
* ✓ Component patterns identified  
* ✓ Teacher feedback incorporated  
* ✓ Intervention effectiveness measured

### **Why This Phased Approach**

1. **Risk Mitigation:** Test simple before committing to complex  
2. **Data-Driven:** Validate assumptions before cementing them  
3. **Speed to Market:** Ship in weeks, not months  
4. **Learning Opportunity:** Discover what actually matters  
5. **Flexibility:** Can keep simple if it works

---

## **Layer 1: Universal Components**

### **Core Components (All Domains, All Grades)**

| Component | Definition | Phase 1 Use | Phase 2 Weight Range |
| ----- | ----- | ----- | ----- |
| **PROCEDURAL** | Can execute the core skill/process | Tracked only | 25-40% |
| **CONCEPTUAL** | Understands underlying concepts | Tracked only | 25-35% |
| **TRANSFER** | Can apply in novel contexts | Must pass 1+ | 25-40% |
| **METACOGNITIVE** | Can explain and evaluate approach | Future | 0-20% (Gr 4+) |

### **Component Scoring**

#### **Phase 1 (Simple):**

```py
# Simple pass/fail based on overall percentage
score = (correct_baseline_stretch / total_baseline_stretch)
transfer_passed = any(p.correct for p in problems 
                      if p.verb in ['APPLY', 'CONNECT'])

mastery = score >= 0.70 and transfer_passed
# Components tracked for analysis but not enforced
```

#### **Phase 2 (Target \- Production):**

```py
# For each component, calculate:
component_score = correct_attempts / total_attempts

# Overall mastery requires:
- Each component meets minimum threshold (60%)
- No critical gates failed
- Sufficient attempts made
- Weighted average ≥ 70%
```

---

## **Layer 2: Domain Configurations**

### **Mathematics Grade 3 Configuration**

```
domain: MATHEMATICS
grade: 3
default_tool_weight: 0  # Phase 1: diagnostic only

fractions_unit:
  cognitive_verbs:
    CREATE: 
      definition: "Construct fractions using visual tools"
      example: "Shade 3/4 of a rectangle"
      maps_to: PROCEDURAL
      
    IDENTIFY:
      definition: "Recognize fractions and their properties"
      example: "Select all equivalent fractions"
      maps_to: CONCEPTUAL
      
    COMPARE:
      definition: "Determine relationships between fractions"
      example: "Which is larger: 2/3 or 3/4?"
      maps_to: CONCEPTUAL
      
    APPLY:
      definition: "Use fractions in contexts"
      example: "If you ate 2/3 of a pizza..."
      maps_to: TRANSFER
      
    CONNECT:
      definition: "Link concepts and representations"
      example: "Show 3/4 three different ways"
      maps_to: TRANSFER
      
  transfer_gate:
    requirement: "Must pass at least 1 APPLY or CONNECT problem"
    rationale: "Transfer demonstrates true understanding"
```

### **English Language Arts Grade 3 Configuration**

```
domain: ENGLISH_LANGUAGE_ARTS
grade: 3
default_tool_weight: 0.10

reading_unit:
  cognitive_verbs:
    DECODE:
      definition: "Read words accurately"
      example: "Sound out unfamiliar words"
      maps_to: PROCEDURAL
      
    COMPREHEND:
      definition: "Understand meaning"
      example: "Identify main idea"
      maps_to: CONCEPTUAL
      
    ANALYZE:
      definition: "Examine text elements"
      example: "How does character change?"
      maps_to: CONCEPTUAL
      
    CONNECT:
      definition: "Link texts and ideas"
      example: "Compare two stories"
      maps_to: TRANSFER
      
    EVALUATE:
      definition: "Make judgments about text"
      example: "Was character's choice wise?"
      maps_to: TRANSFER
```

---

## **Layer 3: Stakeholder Translations**

### **Translation Matrix**

| Internal Data | Teacher View | Parent View | Admin View |
| ----- | ----- | ----- | ----- |
| PROCEDURAL: 67% | "Needs practice with execution steps" | "Working on: Doing fraction problems" | "Below proficiency in procedural skills" |
| CONCEPTUAL: 85% | "Strong understanding of concepts" | "Understands fractions well" | "Meets conceptual standards" |
| TRANSFER: 45% | "Struggles with word problems" | "Needs help applying to real situations" | "Application skills developing" |

### **Standards Alignment (Metadata Layer)**

```ts
interface StandardsMapping {
  module_id: string;
  standards: {
    primary: string[];      // ["3.NF.A.1"]
    supporting: string[];   // ["3.NF.A.2"]
  };
  component_alignment: {
    PROCEDURAL: string[];   // Standards tested by procedural work
    CONCEPTUAL: string[];   // Standards tested by conceptual work
    TRANSFER: string[];     // Standards tested by transfer work
  };
}
```

### **DOK/Bloom's Translation Layer (Available for Reporting)**

For stakeholders who need traditional taxonomy alignment, we can generate these mappings:

```ts
interface TaxonomyTranslation {
  problem_id: string;
  our_classification: {
    cognitive_verb: "COMPARE";
    component: "CONCEPTUAL";
  };
  traditional_mapping: {
    dok_level: 2;
    blooms_level: "Analyze";
    explanation: "Comparing fractions requires conceptual analysis (DOK 2)";
  };
}
```

This allows us to:

* Generate DOK-aligned reports for administrators  
* Show Bloom's levels for curriculum alignment  
* Provide crosswalk documentation for accreditation  
* Support teachers familiar with traditional frameworks

---

## **Problem Classification System**

### **Every Problem Gets Three Labels**

```
Problem X: [TIER] / [COMPONENT] / [DIAGNOSTIC]

Where:
- TIER = BASELINE | STRETCH | CHALLENGE | SUPPORT | CONFIDENCE
- COMPONENT = Which component it primarily tests
- DIAGNOSTIC = What additional data it provides
```

### **Classification Rules**

| Tier | Counts Toward Mastery | Purpose | When Used |
| ----- | ----- | ----- | ----- |
| **BASELINE** | Yes | Core assessment problems | Standard difficulty |
| **STRETCH** | Yes | Extended assessment | Slightly harder |
| **CHALLENGE** | Bonus only | Above-grade exploration | For high performers |
| **SUPPORT** | No | Confidence building | After 2 wrong in row |
| **CONFIDENCE** | No | Emotional support | After SUPPORT failed |

### **Minimum Attempts for Valid Mastery**

* **Foundational Modules (1-4):** 4+ BASELINE/STRETCH problems  
* **Building Modules (5-8):** 5+ BASELINE/STRETCH problems  
* **Complex Modules (9-12):** 6+ BASELINE/STRETCH problems

---

## **Phase-Based Assessment Flow**

### **Exit Check (3 problems) \- Quick Confidence Check**

**Purpose:** Early detection of comprehension issues before deep practice

**Routing Logic:**

```
3/3 correct → Advance to Practice
2/3 correct → Advance to Practice (marginal pass)
1/3 correct → Intervention Options:
              a) Repeat Lesson after break
              b) Offer Path Switch choice
0/3 correct → Strongly recommend Path Switch
```

**Rationale:** Small sample size demands quick response to prevent frustration buildup

### **Practice Phase (10-12 problems per attempt) \- Mastery Development**

**Multi-Level Adaptive System:**

#### **Within-Attempt Adaptation (Immediate)**

```
- 2 incorrect in row → Insert SUPPORT problem (easier)
- SUPPORT problems don't count toward mastery
- SUPPORT failed → Insert CONFIDENCE problem (very easy)
- MUST complete all 10-12 problems (no early exit)
```

#### **Between-Attempt Routing**

```
Attempt 1: <70% → Try once more with adjustments
Attempt 2: <70% → AUTOMATIC PATH SWITCH
Maximum attempts: 2 (testing hypothesis, may adjust to 3 based on data)
```

**Critical Design Decisions:**

* **No Early Exit:** Prevents strategic failing/gaming  
* **2 Attempts Before Switch:** Balance between persistence and frustration  
* **Adaptive Support:** Each attempt already includes 3-4 easier problems

### **Synthesis Phase**

Only accessible after passing Practice (≥70% with APPLY success)

---

## **Diagnostic Streams (Separate from Mastery)**

### **Available Diagnostics by Domain**

```
MATHEMATICS (Tracking Now, May Use Later):
  tool_competence:      # Visual tool usage (threshold TBD)
  calculation_fluency:  # Speed and accuracy
  vocabulary_precision: # Mathematical language

ENGLISH (Future):
  reading_fluency:      # WPM and accuracy
  vocabulary_knowledge: # Word understanding
  writing_mechanics:    # Grammar, spelling

UNIVERSAL (Always Tracked):
  engagement:          # Time on task, persistence
  help_seeking:        # When and how they ask for help
  confidence:          # Self-reported + behavioral
```

### **Diagnostic Tracking**

```py
class DiagnosticStream:
    def __init__(self, stream_type):
        self.type = stream_type
        self.weight = 0  # Diagnostics NEVER affect mastery
        
    def track(self, interaction):
        # Collect diagnostic data
        # Flag for potential future intervention
        # Phase 1: Track only
        # Phase 2: May trigger tool support if <50%
```

**Phase 1 Status:** All diagnostics tracked but not used for routing **Phase 2 Plans:** Tool competence \<50% may trigger intervention

---

## MISCONCEPTION TRACKING (Both Phases)

Phase 1: Detection and Logging

- Tag problems with potential misconceptions  
- Track frequency per student  
- Log for future analysis

Phase 2: Active Intervention (If Validated)

- TBD

Misconception Coding: M\[module\].\[number\] Example: M3.1 \= Module 3, Misconception 1

---

## **Intervention System**

### **Multi-Level Intervention Architecture**

#### **Level 1: Problem-Level (Immediate)**

* **Light Remediation:** Gentle hint after wrong answer  
* **Medium Remediation:** Conceptual support if still wrong  
* **Heavy Remediation:** Full modeling with \[Modeling\] tag

#### **Level 2: Within-Attempt Adaptation**

* **SUPPORT Problem:** Auto-inserted after 2 wrong in row  
* **CONFIDENCE Problem:** Inserted after SUPPORT fails  
* **Diagnostic Tracking:** Monitor but don't count these

#### **Level 3: Phase-Based Routing**

**EXIT CHECK Interventions:**

```
Score          → Action
━━━━━━━━━━━━━━━━━━━━━━
3/3            → Advance to Practice
2/3            → Advance to Practice (marginal)
1/3 or 0/3     → Options:
                 a) Repeat Lesson after break
                 b) Offer Path Switch
```

**PRACTICE PHASE Interventions:**

```
Attempt    Score    → Action
━━━━━━━━━━━━━━━━━━━━━━━━━━
1          <70%     → Try once more with adjustments
1          ≥70%     → Advance to Synthesis
2          <70%     → Automatic Path Switch
2          ≥70%     → Advance to Synthesis
```

#### **Level 4: Module-Level Interventions**

* **SPIRAL REVIEW:** Return to prerequisite modules (foundation gaps)  
* **TOOL SUPPORT:** Tutorial for visualization tools (if tracking shows \<50%)  
* **CHALLENGE PATH:** For consistent high performers (\>90%)

### **Intervention Routing Logic**

```py
def route_intervention(phase, attempt, score, diagnostics):
    """Unified routing logic for all phases"""
    
    if phase == "EXIT_CHECK":
        if score <= 1/3:
            return ["REPEAT_LESSON", "PATH_SWITCH_OPTION"]
        return "CONTINUE_TO_PRACTICE"
    
    elif phase == "PRACTICE":
        # Check TRANSFER gate first
        if not has_transfer_success:
            return "MUST_PASS_TRANSFER"
            
        if attempt == 1 and score < 0.70:
            return "TRY_AGAIN_WITH_SUPPORT"
        elif attempt == 2 and score < 0.70:
            return "AUTO_PATH_SWITCH"
        else:
            return "ADVANCE_TO_SYNTHESIS"
    
    # Future: Component-based routing in Phase 2
    # Will check which component is weakest
```

### **Key Intervention Principles**

1. **Never End Early:** Prevents gaming, maintains expectations  
2. **Escalating Support:** Problem → Attempt → Path → Module  
3. **Data-Driven Thresholds:** All triggers adjustable based on evidence  
4. **TRANSFER Gate:** Must demonstrate application ability

---

## **Module Complexity Adaptation**

### **Module-Level Progressions (Within Grade 3\)**

| Module Range | Type | Component Weights | Scaffolding |
| ----- | ----- | ----- | ----- |
| **Modules 1-4** | Foundational | PROC: 40%, CONC: 35%, TRANS: 25% | Heavy |
| **Modules 5-8** | Building | PROC: 33%, CONC: 33%, TRANS: 34% | Moderate |
| **Modules 9-12** | Complex | PROC: 30%, CONC: 30%, TRANS: 40% | Light |

### **Grade-Level Progressions (Future)**

| Grade Band | Characteristics | Tool Use | Abstract Thinking |
| ----- | ----- | ----- | ----- |
| **Grades K-2** | Concrete operations | Heavy tool dependence | Minimal |
| **Grades 3-5** | Semi-concrete | Balanced tools | Emerging |
| **Grades 6-8** | Semi-abstract | Tool optional | Developed |
| **Grades 9-12** | Formal operations | Symbolic focus | Primary |

Note: Currently implementing Module progressions within Grade 3\. Grade progressions planned for future expansion.

### **Tool Weight by Context**

```py
def get_tool_weight(grade, domain, unit):
    # Note: In Phase 1, tool is diagnostic only
    # This function for Phase 2 planning
    
    base_weight = {
        'MATHEMATICS': 0.30,
        'ENGLISH': 0.10,
        'SCIENCE': 0.20
    }[domain]
    
    # Decrease by grade
    grade_modifier = max(0.5, 1.0 - (grade - 3) * 0.1)
    
    # Special cases
    if unit in ['GEOMETRY', 'MEASUREMENT', 'DATA_VIZ']:
        return base_weight  # Keep high even in upper grades
        
    return base_weight * grade_modifier

# Phase 1: Tool tracked but weight = 0
# Phase 2: May apply weights above
```

---

## **Implementation Examples**

### **Example 1: Module 3 Routing Flow**

```
STUDENT JOURNEY THROUGH MODULE 3:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXIT CHECK (3 problems):
P1: Create 2/4 → ✓
P2: Identify equivalent → ✗
P3: Compare fractions → ✗
Result: 1/3 correct → INTERVENTION OPTIONS

Option A: Repeat Lesson after recess
Option B: Try different path

[Student chooses: Repeat Lesson]

EXIT CHECK (After repeat):
P1: Create 3/4 → ✓
P2: Identify equivalent → ✓
P3: Compare fractions → ✗
Result: 2/3 correct → PROCEED TO PRACTICE

PRACTICE ATTEMPT 1:
P1: BASELINE → ✓
P2: BASELINE → ✗
P3: BASELINE → ✗ [2 wrong in row!]
P4: SUPPORT → ✓ [easier problem inserted]
P5: STRETCH → ✗
P6: BASELINE → ✗ [2 wrong in row!]
P7: CONFIDENCE → ✓ [very easy problem]
P8: BASELINE → ✓
P9: STRETCH → ✗
P10: BASELINE → ✓

Scored: 4/8 BASELINE/STRETCH = 50%
Result: <70% → TRY AGAIN

PRACTICE ATTEMPT 2:
[Similar flow with more support]
Scored: 5/8 = 62%
Result: <70% → AUTO PATH SWITCH
```

#### **Phase 1 Implementation (Current):**

```
learning_goal: "Compose non-unit fractions from unit fractions"

simple_scoring:
  pass_threshold: 0.70
  require_apply: true
  min_attempts: 6

tracking_for_analysis:
  procedural_problems: [1, 2, 3]  # CREATE problems
  conceptual_problems: [4, 5]      # IDENTIFY/COMPARE
  transfer_problems: [6, 7]        # APPLY/CONNECT

sample_problems:
  problem_1:
    cognitive_verb: CREATE
    tier: BASELINE
    prompt: "CREATE 3/4 using the bar tool"
    counts: true
    component_tracked: PROCEDURAL
    
  problem_8:
    cognitive_verb: CREATE
    tier: SUPPORT
    prompt: "CREATE 1/2 any way you like"
    counts: false
    component_tracked: PROCEDURAL
```

#### **Phase 2 Implementation (Target):**

```
learning_goal: "Compose non-unit fractions from unit fractions"

component_breakdown:
  PROCEDURAL: 
    weight: 0.35
    minimum: 0.60
    cognitive_verbs: [CREATE]
    intervention: "More scaffolded building practice"
    
  CONCEPTUAL:
    weight: 0.30
    minimum: 0.60
    cognitive_verbs: [IDENTIFY, COMPARE]
    intervention: "Explore different representations"
    
  TRANSFER:
    weight: 0.35
    minimum: 0.60  # Plus gate: at least 1 correct
    cognitive_verbs: [APPLY, CONNECT]
    intervention: "Context-first problems"
    
critical_gates:
  transfer_gate: "Must pass at least 1 APPLY or CONNECT problem"
```

### **Example 3: Mastery Calculation with Cognitive Verbs**

#### **Phase 1 (Simple):**

```py
# Student attempts Module 3 Practice
results_by_verb = {
    'CREATE': [1, 1, 0],      # 2/3 correct (PROCEDURAL)
    'IDENTIFY': [1, 0],        # 1/2 correct (CONCEPTUAL)
    'COMPARE': [0, 1],         # 1/2 correct (CONCEPTUAL)
    'APPLY': [0, 1],           # 1/2 correct (TRANSFER)
    'CONNECT': [1],            # 1/1 correct (TRANSFER)
    'SUPPORT': [1, 1, 1],      # Not counted
}

# Simple calculation (Phase 1)
baseline_stretch = 8
correct = 6
score = 6/8 = 0.75

transfer_passed = True  # APPLY=1 + CONNECT=1 (at least one)

mastery = "PASSED" if score >= 0.70 and transfer_passed else "NEEDS PRACTICE"
# Result: PASSED (both conditions met)
```

#### **Phase 2 (Component-Based):**

```py
# Same performance, component analysis
component_scores = {
    'PROCEDURAL': 2/3,     # CREATE verbs: 67% ✓
    'CONCEPTUAL': 2/4,     # IDENTIFY + COMPARE: 50% ✗
    'TRANSFER': 2/3,       # APPLY + CONNECT: 67% ✓
}

# Weighted calculation
weighted_score = (0.67 * 0.35) + (0.50 * 0.30) + (0.67 * 0.35) = 0.62

# Component gates check
conceptual_below_min = component_scores['CONCEPTUAL'] < 0.60  # True!
transfer_gate_passed = True  # Has 1+ TRANSFER correct

mastery_detailed = {
    'status': 'NEEDS INTERVENTION',  # Failed component minimum
    'overall': 0.62,
    'weak_component': 'CONCEPTUAL',
    'intervention': 'Visual exploration with IDENTIFY/COMPARE practice',
    'note': 'CONCEPTUAL at 50% below 60% minimum'
}
```

Note how Phase 2 catches the conceptual weakness that Phase 1 missed\!

---

## **Quality Assurance Checklist**

### **Phase 1 Checklist (Testing)**

* \[ \] 70% threshold implemented  
* \[ \] TRANSFER gate functional (1+ APPLY/CONNECT)  
* \[ \] SUPPORT problems marked as non-counting  
* \[ \] Exit Check routing (1/3 → intervention)  
* \[ \] Practice routing (2 attempts max)  
* \[ \] No early exit enforced  
* \[ \] All data tracked for analysis

### **Phase 2 Checklist (Before Activation)**

* \[ \] Component calculations validated  
* \[ \] Weights tested with real data  
* \[ \] Teacher dashboard ready  
* \[ \] Parent translations written  
* \[ \] Standards alignment mapped  
* \[ \] Migration triggers met

### **Universal Requirements (Both Phases)**

* \[ \] Learning goal clearly stated  
* \[ \] 10+ problems classified by tier  
* \[ \] Cognitive verbs identified  
* \[ \] Intervention pathways defined  
* \[ \] Data collection comprehensive  
* \[ \] Student experience smooth

---

## **Migration Path**

### **Current Status: Phase 1 Active**

* Simple scoring implemented  
* Data tracking infrastructure built  
* Testing with internal students  
* Collecting validation data

### **Phase 1 → Phase 2 Decision Points**

**Continue with Simple if:**

* 70% threshold accurately predicts success  
* Teachers satisfied with pass/fail  
* Interventions effective without components  
* Complexity adds no clear value

**Activate Phase 2 if:**

* Need more precise diagnostics  
* Teachers request component detail  
* Intervention routing needs refinement  
* Data shows component patterns matter

### **Rollout Strategy**

**Option A: Big Bang**

* Complete Phase 1 testing  
* Analyze all data  
* Switch entire system to Phase 2

**Option B: Progressive** (Recommended)

* Start with Phase 1 everywhere  
* Activate Phase 2 for specific modules  
* Compare effectiveness  
* Roll out based on results

### **Technical Implementation**

```javascript
// Configuration-driven phases
const MASTERY_CONFIG = {
  'module_1': { phase: 1, threshold: 0.70 },
  'module_2': { phase: 1, threshold: 0.70 },
  'module_3': { phase: 2, components: true }, // Testing Phase 2
  // ... etc
};
```

---

## **Implementation Timeline: Realistic vs. Vision**

### **What We're Building NOW (Phase 1\)**

**Core Mastery System:**

* Simple 70% threshold  
* APPLY gate requirement (for modules that require it)  
* Problem classification (BASELINE, STRETCH, SUPPORT, etc.)  
* Basic intervention routing (\<40% path switch, \<70% practice)  
* Full data tracking for analysis

**Hidden Tracking (For Phase 2 Prep):**

* Component breakdown (not enforced)  
* Cognitive verb distribution  
* Tool diagnostics  
* Time and attempt patterns

### **What's Planned NEXT (Phase 2\)**

**Component System Activation:**

* ⏳ Component minimums enforced  
* ⏳ Weighted scoring by module  
* ⏳ Precision intervention routing  
* ⏳ Standards alignment active

**Enhanced Teacher Features:**

* ⏳ Component breakdown visibility  
* ⏳ Grouping recommendations  
* ⏳ Diagnostic reports  
* ⏳ Progress predictions

**Parent Communication:**

* ⏳ Detailed strength/struggle areas  
* ⏳ Translated component language  
* ⏳ Targeted home support suggestions

### **Future Vision (Post-Validation)**

**Advanced Features:**

* 🔮 Cross-domain expansion (English, Science)  
* 🔮 Predictive analytics  
* 🔮 Learning profiles  
* 🔮 Adaptive sequencing  
* 🔮 Full LMS integration

### **Phase Transition Criteria**

**Phase 1 → 2 Triggers:**

1. Minimum 1000 student sessions completed  
2. 70% threshold validated as predictive  
3. TRANSFER gate necessity confirmed  
4. Component patterns identified  
5. Exit Check intervention threshold validated  
6. Practice attempts (2 vs 3\) determined  
7. Clear evidence that complexity adds value

**Decision Framework:**

* If simple works → Keep it, make components optional  
* If components needed → Activate Phase 2  
* If neither sufficient → Design Phase 3 based on data

---

## **Key Principles**

### **Universal Principles (Both Phases)**

1. **Components are universal, verbs are domain-specific**  
2. **Diagnostics inform but don't determine mastery**  
3. **Support problems build confidence but don't count**  
4. **Interventions are practical, not theoretical**  
5. **Standards are metadata, not drivers**

### **Phase-Specific Principles**

**Phase 1 (Testing):**

* Simplicity over precision  
* Track everything, enforce little  
* Learn fast, adjust often  
* 70% threshold is a hypothesis

**Phase 2 (Production):**

* Component precision for intervention routing  
* Teacher language preserved, parent language simplified  
* Quality over quantity in assessment  
* Weighted scoring reflects module complexity

---

## **Competitive Advantage**

### **What Others Do vs. What We Do**

| Competitor | Their Approach | Our Advantage |
| ----- | ----- | ----- |
| **Khan Academy** | Binary mastery (practiced/mastered) \+ points | Component breakdown shows WHERE struggle is |
| **IXL** | SmartScore 0-100, single number | Three components reveal intervention needs |
| **i-Ready** | Grade level equivalents (complex) | Actionable components teachers understand |
| **DreamBox** | Black box adaptive (hidden logic) | Transparent mastery criteria |

### **Our Unique Differentiators**

1. **Interactive Guide with Targeted Remediation** \- Not passive videos or generic feedback  
2. **Path Switching Based on Performance** \- No one else truly adapts pedagogy mid-module  
3. **Component-Specific Interventions** \- Not just "try again" but targeted support  
4. **Tool Competence Tracking** \- Recognizes digital manipulation as separate skill  
5. **Teacher-Friendly Language** \- Uses verbs teachers actually think with  
6. **Built-in Translation Layers** \- Same data, different stakeholder views

### **Why This Matters for Students**

* **More Accurate Diagnosis**: Know if issue is doing, understanding, or applying  
* **Faster Intervention**: System immediately routes to right support  
* **Preserved Confidence**: SUPPORT problems that don't punish exploration  
* **Multiple Chances**: Different paths for different learners  
* **Clear Progress**: Students see component growth, not just pass/fail

---

## **Why This Framework vs. Established Taxonomies**

### **Comparison with Established Frameworks**

We carefully evaluated DOK (Depth of Knowledge) and Bloom's Taxonomy before developing this hybrid approach. Our framework incorporates their strengths while addressing specific needs of digital, interactive learning.

| Framework | Strengths We Keep | Limitations We Address | Our Solution |
| ----- | ----- | ----- | ----- |
| **Webb's DOK** | • Clear complexity levels • Standards alignment • Assessment focus | • Too abstract for moment-by-moment tracking • Not designed for digital tools • Single dimension | • Use complexity as metadata • Track tool interaction separately • Multi-dimensional components |
| **Bloom's Revised** | • Cognitive progression • Universal recognition • Research-backed | • "Create" as highest level doesn't fit (shading 2/3 is creating but basic) • Hierarchical only • Not action-oriented | • Domain-specific verb flexibility • Horizontal complexity • Direct action mapping |
| **SOLO Taxonomy** | • Observable outcomes • Quality focus • Structural progression | • Less known to US educators • Complex for parents • Abstract terminology | • Simple component language • Parent-friendly translations • Concrete examples |

### **How We Incorporate Best Practices**

```
From DOK:
  - Complexity indicators for each problem
  - Standards alignment tracking
  - Assessment-worthy vs. practice problems

From Bloom's:
  - Cognitive categories (reimagined as components)
  - Progressive skill development
  - Higher-order thinking emphasis

From SOLO:
  - Structural quality over quantity
  - Observable learning outcomes
  - Integrated understanding focus

Our Addition:
  - Tool competence tracking
  - Real-time intervention routing
  - Domain-authentic language
  - Stakeholder translation layers
```

### **The Key Advantage: Practical Implementation**

**Traditional Taxonomy Application:** "This problem is DOK Level 2 requiring Analyze-level thinking per Bloom's"

* What does a teacher DO with this information?  
* How does this help route interventions?  
* What does a parent understand?

**Our Framework Application:** "Student struggles with CONCEPTUAL understanding (67%) in fraction comparison"

* Teacher knows: Focus on visual models  
* System routes: Additional representation practice  
* Parent sees: "Needs help understanding what fractions mean"

### **Why Not Just Use DOK or Bloom's?**

**We considered this carefully.** Here's why we chose a hybrid approach:

1. **Digital Tool Reality**: DOK/Bloom's predate interactive digital learning. Creating 3/4 by dragging bars is neither DOK 1 nor Bloom's "Create" \- it's its own action that needs specific tracking.

2. **Intervention Routing**: Knowing something is "DOK 2" doesn't tell us whether to provide visual models, more practice, or conceptual explanation. Our components directly map to intervention types.

3. **Teacher Intuition**: Teachers think "Can they compare fractions?" not "Is this DOK Level 2?" Our verbs match teacher planning language.

4. **Parent Communication**: Parents understand "practicing doing problems" vs "understanding concepts" better than taxonomy levels.

5. **Cross-Domain Flexibility**: "CREATE" means different things in Math vs English. Our framework allows this while maintaining universal components for reporting.

**We're not rejecting established frameworks** \- we're building a translation layer that uses their insights while serving practical needs. Schools can still get DOK-aligned reports; we just track more actionable data underneath.

### **Research Alignment**

Our approach aligns with:

* **Cognitive Load Theory**: Components separate different types of mental processing  
* **Self-Determination Theory**: Clear competence tracking supports motivation  
* **Universal Design for Learning**: Multiple representations and flexible pathways  
* **Formative Assessment Best Practices**: Actionable, immediate feedback

---

	

## **Appendix: Quick Reference**

### **Routing Configuration (Testing Hypotheses)**

```
exit_check:
  problems: 3
  thresholds:
    pass: 2/3 or 3/3
    intervention: 1/3 or 0/3
  interventions:
    - repeat_lesson_after_break
    - offer_path_switch
    
practice_phase:
  problems_per_attempt: 10-12
  max_attempts: 2  # Testing hypothesis (may become 3)
  mastery_threshold: 0.70
  transfer_gate: true  # Must pass 1+ APPLY or CONNECT
  
  adaptive_rules:
    consecutive_failures: 2  # Triggers SUPPORT problem
    support_failure: true    # Triggers CONFIDENCE problem
    early_exit: false        # NEVER - prevents gaming
    
  routing_outcomes:
    attempt_1_fail: "Try again with adjustments"
    attempt_2_fail: "Automatic path switch"
    
what_were_testing:
  - "Is 2 attempts sufficient with adaptation?"
  - "Does 70% predict next module success?"
  - "Should Exit Check be 1/3 or 0/3 for intervention?"
  - "Do SUPPORT problems improve success rates?"
  - "Is TRANSFER gate necessary for progression?"
```

### **Component → Intervention Mapping**

* **PROCEDURAL weak** → Scaffolded practice, modeling  
* **CONCEPTUAL weak** → Visual exploration, patterns  
* **TRANSFER weak** → Word problems, contexts  
* **Multiple weak** → Path switch

### **Tier → Purpose Mapping**

* **BASELINE** → Core mastery assessment  
* **STRETCH** → Extended assessment  
* **CHALLENGE** → Above-grade exploration  
* **SUPPORT** → Confidence building (after struggles)  
* **CONFIDENCE** → Emotional support (after SUPPORT fails)

### **Grade → Complexity Mapping**

* **Grades K-2** → Heavy scaffolding, concrete  
* **Grades 3-5** → Balanced, semi-concrete  
* **Grades 6-8** → Light scaffolding, abstract  
* **Grades 9-12** → Independent, formal

---

*Document Version 3.0 \- Phased Implementation*  
 *Phase 1: Active for testing*  
 *Phase 2: Target production system*  
 *Routing Logic: Version 2.0 (2 attempts, no early exit)* *Living document \- updated as system evolves based on student data*

