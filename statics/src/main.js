window.onload = function() {
    /// Now Question and Awnswer Array
    // Global variable
    var question = [' Q1. What is GIT ?', ' Q2. What is GITHUB ?', ' Q3. Something is in Air ?']
    var answer = ['', '', '']
    var index = 0

    function decrementer() {
        if (index == 0) {
            index = 0
        } else {
            index -= 1
        }

        driver(index)
    }

    function increment() {
        if (index == question.length - 1) {
            index = question.length - 1
        } else {
            index += 1
        }

        driver(index)
    }

    /// Below part is for Speech recognization So STT is implemented in Javascript   
    console.log("checking df")
    const texts = document.querySelector(".answer");
    var copytext = "ANSWER: "
    var start = false;

    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.interimResults = true;
    recognition.addEventListener("result", (e) => {
        const text = Array.from(e.results)
            .map((result) => result[0])
            .map((result) => result.transcript)
            .join('');


        // Use to check keyword in the text for Active cmd feature 
        if (e.results[0].isFinal) {
            copytext = copytext + '' + text
            if (text.includes("stop and submit")) {
                start = false;
                recognition.stop();
            }
            if (text.includes("submit and next question")) {
                start = false;
                recognition.stop();
                increment();
            }
            if (text.includes("next question")) {
                start = false;
                recognition.stop();
                increment();
            }
            if (text.includes("previous question")) {
                start = false;
                recognition.stop();
                decrementer()
            }
        }


        texts.innerText = copytext;
        answer[index] = copytext
    });

    recognition.addEventListener("end", () => {
        if (start) {
            recognition.start();
        }

    });
    var start = true;
    let button = document.getElementById('recordButton');

    if (typeof button !== 'undefined' && button !== null) {
        button.onclick = () => {
            recognition.start();
            start = true
        };
    }



    function driver(index) {
        //First Function to call on website load
        //load question
        var questionPanel = document.querySelector('#questionPanel');
        //console.log(questionPanel)
        questionPanel.innerText = question[index]
            //console.log(question[index])
        texts.innerText = answer[index];
        copytext = "ANSWER: "
            // recognition.start();
            // start = true
    }

    // previous and Next button listner

    var prev = document.getElementById('prevButton')
    prev.onclick = () => {
        decrementer()
    }


    var next = document.getElementById('nextButton')
    next.onclick = () => {
        increment()
    }


    driver(index)



}