window.onload = function() {
    console.log("checking dfsdsdfsdfdfds")
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
    /// Text to speech 
    let speech = new SpeechSynthesisUtterance();
    speech.lang = "en";
    document.getElementsByClassName("playButton")[0].addEventListener("click", () => {
        console.log("click")
        speech.rate = 10;
        speech.volume = 100;
        speech.pitch = 10;
        let voices = [];
        voices = window.speechSynthesis.getVoices();
        speech.voice = voices[0];
        speech.text = "Abhishek zade"
        window.speechSynthesis.speak(speech);
    });
/// Below part is for Speech recognization So STT is implemented in Javascript  
  window.SpeechRecognition = window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.interimResults = true;
    recognition.addEventListener("result", (e) => {
        const text = Array.from(e.results)
            .map((result) => result[0])
            .map((result) => result.transcript)
            .join('');

        texts.innerText = copytext;
        // Use to check keyword in the text for Active cmd feature 
        if (e.results[0].isFinal) {
            copytext = '' + copytext + '' + text
            if (text.includes("stop and submit")) {
                start = false;
                recognition.stop();
            }
            if (text.includes("submit and next question")) {
                increment();
                recognition.start();
            }
            if (text.includes("next question")) {
                increment();
                recognition.start();
            }
            if (text.includes("previous question")) {
                decrementer()
                recognition.start();
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
            // recognition.start();
            // start = true
            driver(index)
            recognition.start();
            start = true
        };
    }



    function driver(index) {
        console.log("driver");
        //First Function to call on website load
        //load question
        var questionPanel = document.querySelector('#questionPanel');
        //console.log(questionPanel)
        questionPanel.innerText = question[index]
            //console.log(question[index])
        texts.innerText = answer[index];
        copytext = "ANSWER: "
        if (start) {
            start = true
            recognition.start();
        }
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


    //driver(index)

    // keyboards listners
    document.addEventListener('keydown', function(event) {
        if (event.key === 'd') {
            //document.body.style = "color: white; background-color: #111111";
            console.log("D");
            increment()

        }
        if (event.key === 'a') {
            //document.body.style = "color: white; background-color: #111111";
            console.log("a");
            decrementer()
        }
        if (event.key === 's') {
            //document.body.style = "color: white; background-color: #111111";
            console.log("s");
            start = true
            driver(index)
        }
        if (event.key === 'z') {
            //document.body.style = "color: white; background-color: #111111";
            console.log("z");
            start = false;
            recognition.stop();
            // driver(index)
        }
    });
    driver(index)

}