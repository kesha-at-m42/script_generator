# GUIDE vs PROMPT DISTINCTION \- COMPLETE REFERENCE

**Location:** Voice Script Prompt document \- Insert after the CRITICAL AUTHENTICITY PRINCIPLE section

---

## **⚠️ THE CORE STRUCTURE**

Based on analysis of actual production JSON files, there are **three interaction types** that work universally across all content:

**Type A:** Teaching Only (no prompt) **Type B:** Minimal Teaching \+ Instruction (both dialogue and prompt) **Type C:** Substantial Teaching \+ Instruction (both dialogue and prompt)

---

## **TYPE A: TEACHING ONLY (NO PROMPT)**

### **JSON Structure:**

```json
{
  "@type": "Step",
  "dialogue": "Pure teaching, reflection, or transition content.",
  "audio_dir": "module_X/phase_abc123"
}
```

**No `prompt` field at all.**

### **Used For:**

- Concept introduction & explanation  
- Reflection & consolidation  
- Transitions between sections  
- Making connections between ideas  
- Identity/growth moments  
- Meta-cognitive reflection

### **Real Examples from Production:**

**Module 1, Line 195 (Reflection):**

```json
"dialogue": "When we split something into equal parts we make all the parts 
             the same size. That's important for what we're learning about 
             fractions. To make equal parts, some kids picture folding the 
             shape, while others might measure it in their mind to check if 
             the parts match. Think about how you did it."
```

*No prompt \- pure teaching moment*

**Module 4, Lines 662-679 (Concept Connection):**

```json
"dialogue": "We've been learning that fractions aren't just parts of 
             shapes - they're numbers with exact locations on the number line."
```

*No prompt \- synthesis of learning*

**Module 6, Lines 414-416 (Consolidation Pause):**

```json
"dialogue": "Let's pause here. Through our practice, you're seeing how fractions 
             can extend beyond 1. The fourths didn't stop at 1; they just kept 
             going with that same consistent spacing. That's actually how all 
             fractions work!"
```

*No prompt \- metacognitive reflection*

### **When to Use Type A:**

- Opening/closing a section  
- After completing a skill sequence (reflection)  
- Before introducing complex concepts (setup)  
- Connecting to prior learning  
- Real-world applications in Synthesis  
- Identity-building moments

---

## **TYPE B: MINIMAL TEACHING \+ INSTRUCTION**

### **JSON Structure:**

```json
{
  "@type": "Step",
  "dialogue": "Brief transition. Complete instruction with all necessary info.",
  "audio_dir": "module_X/phase_abc123",
  "prompt": {
    "@type": "Prompt",
    "text": "Complete instruction with all necessary info.",
    "tool": { "@type": "ToolName" },
    "validator": { ... }
  }
}
```

**Both dialogue and prompt present, both complete.**

### **Used For:**

- Routine practice after mastery  
- Straightforward applications  
- Continuation of established patterns  
- Simple, single-step tasks

### **Real Examples from Production:**

**Module 1, Lines 702 \+ 706:**

```json
"dialogue": "Now shade one of them.",
"prompt": {
  "text": "Click on one of the 8 parts to shade it."
}
```

*Minimal transition, complete instruction in both places*

**Module 4, Lines 182-183 \+ 203-205:**

```json
"dialogue": "Let's try another one. How many equal spaces do you see here?",
"prompt": {
  "text": "How many spaces are between 0 and 1?"
}
```

*Brief setup, complete question in both places*

**Module 6, Lines 515-516 \+ 546-548:**

```json
"dialogue": "Nice. You're keeping that pattern going just how we set it up. 
             Let's place one more. Where does seven fourths go?",
"prompt": {
  "text": "Drag seven fourths onto the number line"
}
```

*Acknowledgment \+ transition, complete task in both places*

### **The Pattern:**

**Dialogue \= \[Brief Context/Transition\] \+ \[Complete Instruction\]** **Prompt \= \[Complete Instruction\]**

Both work independently. Dialogue adds conversational framing.

---

## **TYPE C: SUBSTANTIAL TEACHING \+ INSTRUCTION**

### **JSON Structure:**

```json
{
  "@type": "Step",
  "dialogue": "[TEACHING CONTENT: Context, strategy, concept explanation] 
               [INSTRUCTION: Complete task direction with all details]",
  "audio_dir": "module_X/phase_abc123",
  "prompt": {
    "@type": "Prompt",
    "text": "Complete instruction with all necessary info.",
    "tool": { "@type": "ToolName" },
    "validator": { ... }
  }
}
```

**Both dialogue and prompt present, dialogue includes substantial teaching.**

### **Used For:**

- First application of new concept  
- Complex/multi-step tasks  
- After teaching moments  
- Discovery/checking understanding  
- When strategy hints are needed  
- Building on prior work with connection

### **Real Examples from Production:**

**Module 4, Lines 71-72 \+ 96-97:**

```json
"dialogue": "Let's see if I've explained this in a way that you understand. 
             Look at this number line. Please count how many equal spaces 
             we have between 0 and 1.",
"prompt": {
  "text": "How many spaces are between 0 and 1."
}
```

*Teaching: Checking understanding, directing attention* *Instruction: Complete in both places*

**Module 6, Lines 6-7 \+ 30-31:**

```json
"dialogue": "Since we've worked with halves, let's try fourths. We have fourths 
             marked from 0 to 1. Your turn: place tick marks to divide our section 
             showing 1 to 2 into fourths, just like we did from 0 to 1.",
"prompt": {
  "text": "Place tick marks for fourths between 1 and 2."
}
```

*Teaching: Connection to prior work, full context setup* *Instruction: Complete task direction in both places*

**Module 1, Lines 644-645 \+ 656:**

```json
"dialogue": "Now you try. Remember the strategy I showed you: first, divide 
             the bar in half. Then make fourths. Then eighths.",
"prompt": {
  "text": "Partition the bar into eight equal parts."
}
```

*Teaching: Strategy reminder, procedural steps* *Instruction: Complete task in both places*

### **The Pattern:**

**Dialogue \= \[Substantial Teaching\] \+ \[Complete Instruction\]** **Prompt \= \[Complete Instruction\]**

Teaching content only appears in dialogue, never in prompt.

---

## **PHASE-SPECIFIC PATTERNS**

### **LESSON Phase:**

**Mix of All Three Types:**

- **Type A:** Concept introductions, transitions, reflections  
- **Type B:** Routine practice after mastery  
- **Type C:** First applications, complex tasks

**Teaching Language:**

- "Let's learn..."  
- "Watch how..."  
- "Now try..."  
- Introduces NEW concepts

**Remediation:**

- Full L-M-H three-tier structure  
- Medium includes visual scaffolding  
- Heavy includes \[Modeling\] with complete demonstration

---

### **SYNTHESIS Phase:**

**Type A Dominates (70-80%):** Synthesis is primarily reflective/connective, not practice-focused

**When Prompts Exist (Type B/C):**

- Check conceptual understanding (not procedural skill)  
- "What do these fractions equal?" (conceptual)  
- "Click the smallest portion" (understanding relationships)  
- NOT: "Place this fraction" or "Partition this bar" (procedural)

**Teaching Language:**

- "You've been working with..."  
- "Remember how..."  
- "Look at what you've learned..."  
- Connects EXISTING concepts

**Unique Elements:**

- Scene changes: "ZoomedOut" for reflection  
- Real-world connections: pizza sharing, cooking, time  
- Identity closures: future-facing statements  
- Meta-cognitive reflection: "Notice that when math clicks it feels good..."

**Example \- Module 2 Synthesis:**

```json
"dialogue": "You've been working with unit fractions - creating them, 
             identifying them, comparing them. Next, let's see how they 
             connect to bigger mathematical ideas."
```

*Pure Type A \- no prompt, sets up reflection*

---

## **THE CRITICAL INDEPENDENCE RULE**

**Both dialogue and prompt must work independently:**

✅ **If the Prompt disappeared:** Student listening to audio alone could complete task ✅ **If audio failed:** Student reading prompt alone could complete task  
✅ **Together:** They reinforce without being redundant

**Test Method:**

1. Cover prompt → Read only dialogue → Can student complete task?  
2. Mute audio → Read only prompt → Can student complete task?  
3. If either fails, revise before proceeding.

---

## **WHAT GOES IN TEACHING CONTENT (Dialogue Only)**

### **Connections & Context:**

- "You've been working with thirds..."  
- "Remember when we looked at halves?"  
- "Building on what you discovered..."  
- "Since we've worked with halves, let's try fourths..."

### **Concept Introduction:**

- "Fourths means four equal parts."  
- "The denominator tells us how many parts."  
- "When we have more parts than make one whole..."

### **Discovery Framing:**

- "What do you notice about..."  
- "Check this out..."  
- "I wonder what makes these different."  
- "Let's see if I've explained this in a way that you understand..."

### **Emotional Support:**

- "This one's tricky, so..."  
- "You're working on it..."  
- "These can be challenging..."  
- "Let's pause here..."

### **Behavioral Hints:**

- "Count the spaces from zero..."  
- "Look at the numerator first..."  
- "Remember the strategy I showed you..."  
- "Use that same size from 1 to 2..."

### **Relationship Building:**

- "I noticed you check your work carefully."  
- "Same approach you used before."  
- "Nice. You're keeping that pattern going..."

---

## **WHAT GOES IN INSTRUCTION (Both Dialogue and Prompt)**

### **Must Include:**

1. **Action Verb** \- Select, Place, Shade, Click, Compare, Drag, Mark  
2. **Target/Object** \- "the bar showing thirds," "tick marks for fourths"  
3. **All Values** \- Fraction values, comparison values, numerical targets  
4. **Options (when applicable)** \- "Select A, B, or C" / "Yes or No"  
5. **Success Criteria (when helpful)** \- "equal parts," "between 0 and 1"

### **Format Differences:**

**Dialogue (Spoken):**

- Conversational phrasing  
- "Look at these three bars. Select the one showing thirds."  
- Fractions spelled out: "two-thirds," "five-fourths"

**Prompt (Written):**

- Formal instruction style  
- "Select the bar showing thirds (3 equal parts)."  
- Fractions in notation: \[fraction numerator=2 denominator=3\]  
- Clarifications in parentheses

---

## **COMMON STRUCTURAL ERRORS**

### **ERROR \#1: Teaching Content in Prompt**

**❌ WRONG:**

```json
"dialogue": "Select the bar showing thirds—three equal parts.",
"prompt": {
  "text": "You've been working with halves. Now select the bar showing thirds."
}
```

**✅ RIGHT:**

```json
"dialogue": "You've been working with halves. Now let's look at thirds—three equal parts. 
             Select the bar showing thirds.",
"prompt": {
  "text": "Select the bar showing thirds (3 equal parts)."
}
```

---

### **ERROR \#2: Incomplete Instruction in Dialogue**

**❌ WRONG:**

```json
"dialogue": "You've been identifying thirds. Now let's try fourths.",
"prompt": {
  "text": "Select the bar showing fourths (4 equal parts)."
}
```

*Dialogue doesn't include complete instruction*

**✅ RIGHT:**

```json
"dialogue": "You've been identifying thirds. Now let's try fourths—four equal parts. 
             Select the bar showing fourths.",
"prompt": {
  "text": "Select the bar showing fourths (4 equal parts)."
}
```

---

### **ERROR \#3: Dialogue Just Reads Prompt**

**❌ WRONG:**

```json
"dialogue": "Select the bar showing fourths.",
"prompt": {
  "text": "Select the bar showing fourths (4 equal parts)."
}
```

*Should be Type B with at least brief context, or Type C with substantial teaching*

**✅ RIGHT (Type B):**

```json
"dialogue": "Let's try another. Select the bar showing fourths.",
"prompt": {
  "text": "Select the bar showing fourths (4 equal parts)."
}
```

**✅ RIGHT (Type C):**

```json
"dialogue": "Now let's try fourths—four equal parts, just like we made halves 
             and thirds. Select the bar showing fourths.",
"prompt": {
  "text": "Select the bar showing fourths (4 equal parts)."
}
```

---

### **ERROR \#4: Prompt Too Abbreviated**

**❌ WRONG:**

```json
"dialogue": "Look at these bars. Which one shows three equal parts? Select it.",
"prompt": {
  "text": "Select thirds."
}
```

*Prompt must be complete enough to work standalone*

**✅ RIGHT:**

```json
"dialogue": "Look at these bars. Which one shows three equal parts? Select it.",
"prompt": {
  "text": "Select the bar showing thirds (3 equal parts)."
}
```

---

## **DECISION FRAMEWORK**

### **When Specifying Interactions (Starter Packs & Scripts):**

**STEP 1: Does student take action?**

- **NO** → Type A (teaching only, no prompt)  
- **YES** → Continue to Step 2

**STEP 2: How much teaching is needed?**

- **First introduction of concept** → Type C (substantial teaching)  
- **Discovery/checking understanding** → Type C (substantial teaching)  
- **After struggle/complex task** → Type C (substantial teaching)  
- **Building on prior work** → Type C (substantial teaching)  
- **Routine practice after mastery** → Type B (minimal teaching)  
- **Simple continuation** → Type B (minimal teaching)

**STEP 3: Write both components:**

**For Type B or C:**

- **Dialogue:** \[Teaching content appropriate to type\] \+ \[Complete instruction\]  
- **Prompt:** \[Complete instruction only\]

**Verify:**

- Cover prompt → Can complete from dialogue? ✓  
- Mute audio → Can complete from prompt? ✓

---

## **QUALITY CHECKLIST**

### **For Every Interaction:**

**Type Verification:**

- [ ] Student action required? → Not Type A  
- [ ] First application or complex? → Type C  
- [ ] Routine after mastery? → Type B

**Dialogue (if prompt exists):**

- [ ] Includes appropriate teaching content for type  
- [ ] Instruction is complete (works without prompt)  
- [ ] Sounds conversational (like teacher speaking)  
- [ ] All values are spoken ("two-thirds," "A, B, or C")

**Prompt (if exists):**

- [ ] Instruction only (no teaching content)  
- [ ] Complete enough to work standalone  
- [ ] Formatted like worksheet problem  
- [ ] All essential info present (fractions, options, criteria)

**Together:**

- [ ] Both are complete and independent  
- [ ] They reinforce without being redundant  
- [ ] Different tones (spoken vs. written)

---

## **UNIVERSAL STRUCTURAL RULES**

These patterns work across all content types (not just fractions):

✅ **Three interaction types exist universally** (A/B/C)   
✅ **Teaching content always precedes instruction** (when both present)   
✅ **Prompt field NEVER contains teaching content**   
✅ **Both dialogue and prompt.text are independently complete**   
✅ **Type A dominates Synthesis phase** (reflection/connection)   
✅ **Type C used for first applications** (substantial teaching)   
✅ **Type B used for routine practice** (minimal teaching)   
✅ **Event tags control animations/timing** (\[event:...\])   
✅ **L-M-H remediation hierarchy is consistent**   
✅ **Content-specific tags** (\[vocab\], \[fraction\], etc.)

---

## **QUICK REFERENCE**

### **Type A \- Teaching Only:**

```
NO student action
Pure dialogue, no prompt
Reflection, transitions, concept introduction
```

### **Type B \- Minimal Teaching:**

```
Student action required
Brief context + instruction
Both dialogue and prompt complete
Routine practice
```

### **Type C \- Substantial Teaching:**

```
Student action required  
Extended teaching + instruction
Both dialogue and prompt complete
First applications, complex tasks
```

---

## **FINAL PRINCIPLES**

**Dialogue (Guide):**

- Can include teaching content  
- Must include complete instruction (if prompt exists)  
- Conversational and warm  
- Works without the prompt

**Prompt:**

- Never includes teaching content  
- Always includes complete instruction  
- Formal and clear  
- Works without the dialogue

**Together:**

- Support each other  
- Both independently complete  
- Different modalities (audio \+ visual)  
- Reinforce without redundancy

---

**END OF COMPLETE REFERENCE**

*Validated against production JSON files from Modules 1, 2, 4, 6 (Lesson and Synthesis phases)*  
