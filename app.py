from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template with inline CSS and JavaScript
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Math Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .container {
            margin-top: 50px;
        }
        .question {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .input {
            font-size: 18px;
            padding: 10px;
            width: 200px;
        }
        .button {
            font-size: 18px;
            padding: 10px 20px;
            margin: 10px;
            cursor: pointer;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #0056b3;
        }
        .result {
            font-size: 20px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Simple Math Game</h1>
        <div class="question" id="question">Loading...</div>
        <input type="number" id="answer" class="input" placeholder="Your answer here">
        <br>
        <button class="button" onclick="checkAnswer()">Submit</button>
        <button class="button" onclick="generateQuestion()">Skip</button>
        <div class="result" id="result"></div>
    </div>

    <script>
        let correctAnswer;

        function generateQuestion() {
            const num1 = Math.floor(Math.random() * 10) + 1;
            const num2 = Math.floor(Math.random() * 10) + 1;
            correctAnswer = num1 + num2;
            document.getElementById('question').innerText = `What is ${num1} + ${num2}?`;
            document.getElementById('result').innerText = "";
            document.getElementById('answer').value = "";
        }

        function checkAnswer() {
            const userAnswer = parseInt(document.getElementById('answer').value);
            if (userAnswer === correctAnswer) {
                document.getElementById('result').innerText = "Correct! Well done.";
                document.getElementById('result').style.color = "green";
                generateQuestion();
            } else {
                document.getElementById('result').innerText = "Incorrect. Try again.";
                document.getElementById('result').style.color = "red";
            }
        }

        // Generate the first question on page load
        window.onload = generateQuestion;
    </script>
</body>
</html>
"""

@app.route('/')
def game():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
