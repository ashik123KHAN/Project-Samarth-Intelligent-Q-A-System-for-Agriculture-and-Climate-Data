# src/nlp/entity_extractor.py
import spacy
import re
nlp = spacy.load("en_core_web_sm")

# Simple patterns. For production use a fine-tuned NER or explicit mapping.
STATE_KEYWORDS = ["Karnataka", "Maharashtra", "Tamil Nadu", "Kerala", "Bihar", "Uttar Pradesh"]

def extract_entities(question):
    doc = nlp(question)
    # Basic extraction: states and crop by keyword search
    states = [s for s in STATE_KEYWORDS if s.lower() in question.lower()]
    # year range or last N years
    years = None
    m = re.search(r"last\s+(\d+)\s+years", question, re.I)
    if m:
        years = int(m.group(1))
    # crops
    crop = None
    # naive: pick common crop names from question
    for token in doc:
        if token.pos_ == "NOUN" and len(token.text) > 2:
            # this will pick many nouns. we can filter with a small crop list if available.
            pass
    # more robust approach: look for "crop" or explicit names
    m2 = re.search(r"crop\s+([A-Za-z0-9\-\s]+)", question, re.I)
    if m2:
        crop = m2.group(1).strip()
    return {
        "states": states,
        "years": years,
        "crop": crop
    }
