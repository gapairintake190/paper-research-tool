# Writing Templates for Paper Research Tool

TEMPLATES = {
    "literature_review": "Traditional literature review with thematic synthesis",
    "systematic": "PRISMA-style systematic review",
    "argumentative": "Argumentative essay with thesis-antithesis-synthesis"
}


def get_template(template_name: str) -> str:
    """Get writing template by name"""
    
    templates = {
        "literature_review": TEMPLATE_LITERATURE_REVIEW,
        "systematic": TEMPLATE_SYSTEMATIC,
        "argumentative": TEMPLATE_ARGUMENTATIVE,
        "progress": TEMPLATE_PROGRESS
    }
    
    return templates.get(template_name, "")


TEMPLATE_LITERATURE_REVIEW = """# Literature Review Template

## 1. Introduction
- Research context
- Significance of the topic
- Scope of review
- Overview of structure

## 2. Methodology
- Search strategy
- Inclusion/exclusion criteria
- Databases searched
- Number of papers reviewed

## 3. Thematic Analysis

### Theme 1: [Title]
- Key findings from [Author, Year]
- Supporting evidence
- Contradictions in literature

### Theme 2: [Title]
[Same structure]

### Theme 3: [Title]
[Same structure]

## 4. Synthesis
- How themes relate
- Consensus in field
- Major debates
- Gaps identified

## 5. Conclusion
- Summary of key insights
- Implications for practice
- Future research directions

## References
[To be added]
"""


TEMPLATE_SYSTEMATIC = """# Systematic Review Template (PRISMA)

## 1. Title
[Descriptive title with "systematic review" or "meta-analysis"]

## 2. Abstract
- Background
- Objectives
- Methods
- Results
- Conclusions
- Registration number

## 3. Introduction
- Rationale
- Research question(s)
- Protocol registration

## 4. Methods

### 4.1 Eligibility Criteria
- Study designs
- Participants
- Interventions
- Comparators
- Outcomes

### 4.2 Information Sources
- Databases searched
- Date range
- Supplementary searches

### 4.3 Search Strategy
[Full search string for each database]

### 4.4 Selection Process
- Number of records identified
- Number screened
- Number included

### 4.5 Data Extraction
- Items extracted
- Reviewers

### 4.6 Risk of Bias Assessment
- Tool used
- Domains assessed

## 5. Results

### 5.1 Study Selection
[PRISMA flow diagram]

### 5.2 Study Characteristics
[Table of included studies]

### 5.3 Risk of Bias
[Assessment results]

### 5.4 Synthesis
- Narrative synthesis
- Meta-analysis (if applicable)

## 6. Discussion
- Summary of evidence
- Limitations
- Strength of evidence
- Conclusions

## 7. Registration & Support
- Protocol link
- Funding sources
"""


TEMPLATE_ARGUMENTATIVE = """# Argumentative Essay Template

## 1. Introduction
- Hook/Background
- Background information
- Thesis statement
- Roadmap

## 2. Background
- Context for debate
- Key definitions
- Stakeholder perspectives

## 3. Literature Review
- Existing positions
- Supporting arguments
- Opposing arguments

## 4. Arguments

### For [Thesis]
- Argument 1 + evidence
- Argument 2 + evidence
- Argument 3 + evidence

### Against [Antithesis]
- Counterargument 1 + evidence
- Counterargument 2 + evidence

## 5. Synthesis
- Evaluation of evidence
- Weighing arguments
- Nuance and limitations

## 6. Conclusion
- Restate thesis
- Summary of key arguments
- Implications
- Future considerations

## References
"""


TEMPLATE_PROGRESS = """# Research Writing Progress Tracker

## Project: [Title]

### Timeline
| Phase | Start | End | Status |
|-------|-------|-----|--------|
| Research | | | |
| Outline | | | |
| First Draft | | | |
| Revision 1 | | | |
| Revision 2 | | | |
| Final Polish | | | |
| Submission | | | |

### Word Count Goals
- Introduction: ___ / ___ words
- Literature Review: ___ / ___ words
- Methodology: ___ / ___ words
- Results: ___ / ___ words
- Discussion: ___ / ___ words
- Conclusion: ___ / ___ words
- **Total: ___ / ___ words**

### Section Status
- [ ] Introduction
- [ ] Literature Review
- [ ] Methodology
- [ ] Results
- [ ] Discussion
- [ ] Abstract
- [ ] References

### Key Citations Needed
1. 
2. 
3. 

### Weekly Goals
**Week of [date]:**
- [ ] 
- [ ] 

### Blockers
- 
-

### Notes
-
"""
