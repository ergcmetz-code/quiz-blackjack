from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "/data/questions.json" if os.path.exists("/data") else "questions.json"

DEFAULT_QUESTIONS = [
    {
        "question": "Quelle est la couleur du cheval blanc d'Henri IV ?",
        "options": ["Bleu", "Blanc", "Rouge", "Vert"],
        "correct": 1
    }
]

def load_questions():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_QUESTIONS, f, indent=4, ensure_ascii=False)
        return DEFAULT_QUESTIONS
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_questions(questions):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)

questions = load_questions()

# VARIABLES TEMPORAIRES (Mémoire RAM uniquement)
players_names = {"1": "Joueur 1", "2": "Joueur 2", "3": "Joueur 3", "4": "Joueur 4"}
players_scores = {"1": 0, "2": 0, "3": 0, "4": 0}

game_state = {
    "current_question_idx": 0,
    "buzzed_player": None,
    "selected_answer": None,
    "status": "waiting",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/public')
def public():
    return render_template('public.html')

@app.route('/buzzers')
def buzzers():
    return render_template('buzzers.html')

@app.route('/api/state')
def get_state():
    if not questions:
        return jsonify({"error": "No questions"})
    
    q = questions[game_state["current_question_idx"]]
    return jsonify({
        "question": q["question"],
        "options": q["options"],
        "buzzed_player": game_state["buzzed_player"],
        "selected_answer": game_state["selected_answer"],
        "names": players_names,
        "scores": players_scores,
        "status": game_state["status"],
        "total_questions": len(questions),
        "current_idx": game_state["current_question_idx"]
    })

@app.route('/api/press', methods=['POST'])
def press_button():
    data = request.json
    player = str(data.get('player'))
    button_idx = int(data.get('button'))

    if game_state["status"] == "waiting":
        game_state["buzzed_player"] = player
        game_state["selected_answer"] = button_idx
        game_state["status"] = "answered"
        
        correct_idx = questions[game_state["current_question_idx"]]["correct"]
        if button_idx == correct_idx:
            players_scores[player] += 1
            
        return jsonify({"result": "success"})
    return jsonify({"result": "ignored"})

@app.route('/api/next', methods=['POST'])
def next_question():
    game_state["buzzed_player"] = None
    game_state["selected_answer"] = None
    game_state["status"] = "waiting"
    game_state["current_question_idx"] = (game_state["current_question_idx"] + 1) % len(questions)
    return jsonify({"status": "next"})

@app.route('/api/add_question', methods=['POST'])
def add_question():
    global questions
    data = request.json
    new_q = {
        "question": data.get('question'),
        "options": [data.get('opt0'), data.get('opt1'), data.get('opt2'), data.get('opt3')],
        "correct": int(data.get('correct'))
    }
    questions.append(new_q)
    save_questions(questions)
    return jsonify({"status": "added"})

@app.route('/api/set_name', methods=['POST'])
def set_name():
    data = request.json
    player = str(data.get('player'))
    name = data.get('name')
    if name.strip():
        players_names[player] = name
    return jsonify({"status": "name_updated"})

@app.route('/api/reset_game', methods=['POST'])
def reset_game():
    global players_names, players_scores
    players_names = {"1": "Joueur 1", "2": "Joueur 2", "3": "Joueur 3", "4": "Joueur 4"}
    players_scores = {"1": 0, "2": 0, "3": 0, "4": 0}
    game_state["current_question_idx"] = 0
    game_state["buzzed_player"] = None
    game_state["selected_answer"] = None
    game_state["status"] = "waiting"
    return jsonify({"status": "reset"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)