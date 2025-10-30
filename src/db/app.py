# src/web/app.py
from flask import Flask, request, render_template, jsonify
from src.nlp.entity_extractor import extract_entities
from src.planner.query_planner import plan_compare_avg_rainfall, plan_top_crops_by_state
from src.exec.executor import run_query
from src.synth.synthesizer import synthesize
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    payload = request.json
    question = payload.get("question")
    # naive routing for demo
    ent = extract_entities(question)
    states = ent.get("states", [])
    years = ent.get("years") or 5
    if len(states) >= 2 and "rain" in question.lower():
        # compare rainfall example
        sql, params = plan_compare_avg_rainfall(states[0], states[1], years)
        res = run_query(sql, params)
        provenance = "Results derived from dataset_registry entries for fact_rainfall"
        text = synthesize(question, json.dumps(res), provenance)
        return jsonify({"answer": text, "results": res})
    elif len(states) >= 1 and "top" in question.lower():
        # top crops example
        # Very simple: parse last N years from ent; default 2015-2019 demo
        sql, params = plan_top_crops_by_state(states[0], 2015, 2019, top_m=3)
        res = run_query(sql, params)
        provenance = "Results derived from dataset_registry entries for fact_crop_production"
        text = synthesize(question, json.dumps(res), provenance)
        return jsonify({"answer": text, "results": res})
    else:
        return jsonify({"answer": "I could not parse the question. Try asking to compare rainfall or ask top crops.", "results": {}}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
