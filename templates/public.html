<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Blackjack Quiz - Écran Public</title>
    <style>
        body { 
            font-family: 'Arial', sans-serif; 
            background-color: #0b6623; 
            color: white; 
            text-align: center; 
            margin: 0; 
            padding: 40px; 
            overflow: hidden;
        }
        .quiz-container { 
            background: rgba(0,0,0,0.85); 
            padding: 40px; 
            border-radius: 20px; 
            max-width: 1000px; 
            margin: 50px auto; 
            box-shadow: 0 0 30px gold; 
        }
        h1 { 
            color: gold; 
            font-size: 3em; 
            margin-bottom: 10px; 
            text-shadow: 2px 2px 4px black;
        }
        .q-counter {
            font-size: 1.5em;
            color: #ddd;
            margin-bottom: 30px;
        }
        #question-text {
            font-size: 2.5em;
            margin-bottom: 40px;
            line-height: 1.4;
        }
        .options { 
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 25px; 
        }
        .option { 
            padding: 25px; 
            background: #222; 
            border: 4px solid #fff; 
            border-radius: 12px; 
            font-size: 1.8em; 
            font-weight: bold;
        }
        .status-alert { 
            font-size: 3em; 
            margin-top: 40px; 
            height: 80px; 
            color: #00ffff; 
            font-weight: bold;
            text-shadow: 2px 2px 4px black;
        }
    </style>
</head>
<body>

    <h1>♣ ♦ BLACKJACK QUIZ ♥ ♠</h1>
    <div class="q-counter">Question <span id="q-number">0/0</span></div>
    
    <div class="quiz-container">
        <div id="question-text">Chargement de la question...</div>
        <div class="options">
            <div class="option" id="opt-0">A</div>
            <div class="option" id="opt-1">B</div>
            <div class="option" id="opt-2">C</div>
            <div class="option" id="opt-3">D</div>
        </div>
        
        <div class="status-alert" id="status-text"></div>
    </div>

    <script>
        function updatePublicScreen() {
            fetch('/api/state')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('q-number').innerText = (data.current_idx + 1) + "/" + data.total_questions;
                    document.getElementById('question-text').innerText = data.question;
                    document.getElementById('opt-0').innerText = "A: " + data.options[0];
                    document.getElementById('opt-1').innerText = "B: " + data.options[1];
                    document.getElementById('opt-2').innerText = "C: " + data.options[2];
                    document.getElementById('opt-3').innerText = "D: " + data.options[3];

                    if(data.status === "answered") {
                        let pName = data.names[data.buzzed_player];
                        let letter = ["A", "B", "C", "D"][data.selected_answer];
                        document.getElementById('status-text').innerText = `${pName} a bloqué la réponse [ ${letter} ] !`;
                    } else {
                        document.getElementById('status-text').innerText = "À vos buzzers !";
                    }
                });
        }

        // Synchronisation rapide (toutes les 300ms) pour que l'affichage soit instantané
        setInterval(updatePublicScreen, 300);
        updatePublicScreen();
    </script>
</body>
</html>