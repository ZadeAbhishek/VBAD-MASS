window.onload = function() {

    var studentName = "Abhishek"
    var texts = document.getElementsByClassName('answer')[0];
    var submit = document.getElementsByClassName('submit')[0];
    console.log("checking ddssssss")
        /// Now Question and Awnswer Array
        // Global variable
    var question = [' Question-1. What is a version control system (VCS)?', ' Question-2. What is the git pull command?', ' Question-3.  What is a conflict?']
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

    function speak(string) {
        var msg = new SpeechSynthesisUtterance(string);
        msg.rate = 1;
        msg.pitch = 1.2;
        window.speechSynthesis.speak(msg);
    }
    var playbutton = document.getElementsByClassName("playButton")[0];
    playbutton.addEventListener("click", (e) => {
        speak(question[index]);
    })
    var answerbutton = document.getElementsByClassName("playButton")[1];
    answerbutton.addEventListener("click", (e) => {
        speak(answer[index]);
    })




    // var speechUtteranceChunker = function(utt, settings, callback) {
    //     settings = settings || {};
    //     var newUtt;
    //     var txt = (settings && settings.offset !== undefined ? utt.text.substring(settings.offset) : utt.text);
    //     if (utt.voice && utt.voice.voiceURI === 'native') { // Not part of the spec
    //         newUtt = utt;
    //         newUtt.text = txt;
    //         newUtt.addEventListener('end', function() {
    //             if (speechUtteranceChunker.cancel) {
    //                 speechUtteranceChunker.cancel = false;
    //             }
    //             if (callback !== undefined) {
    //                 callback();
    //             }
    //         });
    //     } else {
    //         var chunkLength = (settings && settings.chunkLength) || 160;
    //         var pattRegex = new RegExp('^[\\s\\S]{' + Math.floor(chunkLength / 2) + ',' + chunkLength + '}[.!?,]{1}|^[\\s\\S]{1,' + chunkLength + '}$|^[\\s\\S]{1,' + chunkLength + '} ');
    //         var chunkArr = txt.match(pattRegex);

    //         if (chunkArr[0] === undefined || chunkArr[0].length <= 2) {
    //             //call once all text has been spoken...
    //             if (callback !== undefined) {
    //                 callback();
    //             }
    //             return;
    //         }
    //         var chunk = chunkArr[0];
    //         newUtt = new SpeechSynthesisUtterance(chunk);
    //         var x;
    //         for (x in utt) {
    //             if (utt.hasOwnProperty(x) && x !== 'text') {
    //                 newUtt[x] = utt[x];
    //             }
    //         }
    //         newUtt.addEventListener('end', function() {
    //             if (speechUtteranceChunker.cancel) {
    //                 speechUtteranceChunker.cancel = false;
    //                 return;
    //             }
    //             settings.offset = settings.offset || 0;
    //             settings.offset += chunk.length - 1;
    //             speechUtteranceChunker(utt, settings, callback);
    //         });
    //     }

    //     if (settings.modifier) {
    //         settings.modifier(newUtt);
    //     }
    //     console.log(newUtt); //IMPORTANT!! Do not remove: Logging the object out fixes some onend firing issues.
    //     //placing the speak invocation inside a callback fixes ordering and onend issues.
    //     setTimeout(function() {
    //         speechSynthesis.speak(newUtt);
    //     }, 0);
    // };

    // //create an utterance as you normally would...
    // var myLongText = "dfdsfdsfdsf";

    // var utterance = new SpeechSynthesisUtterance(myLongText);

    // //modify it as you normally would
    // var voiceArr = speechSynthesis.getVoices();
    // utterance.voice = voiceArr[2];

    // //pass it into the chunking function to have it played out.
    // //you can set the max number of characters by changing the chunkLength property below.
    // //a callback function can also be added that will fire once the entire text has been spoken.
    // speechUtteranceChunker(utterance, {
    //     chunkLength: 120
    // }, function() {
    //     //some code to execute when done
    //     console.log('done');
    // });


    /// Below part is for Speech recognization So STT is implemented in Javascript  
    window.SpeechRecognition = window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.interimResults = true;
    recognition.addEventListener("result", (e) => {
        copytext = answer[index]
        const text = Array.from(e.results)
            .map((result) => result[0])
            .map((result) => result.transcript)
            .join('');

        texts.innerText = copytext;
        // Use to check keyword in the text for Active cmd feature 
        if (e.results[0].isFinal) {
            copytext = '' + copytext + '' + text
            if (text.includes("stop recording")) {
                stopRec();
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
            if (text.includes("repeat question")) {
                // console.log(question[index])
                speak(question[index])
            }
            if (text.includes("speak answer")) {
                //console.log(question[index])
                speak(answer[index])
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
    var start = false;
    let button = document.getElementById('recordButton');
    let recordIcon = document.getElementsByClassName('recording')[0];


    if (typeof button !== 'undefined' && button !== null) {
        button.onclick = () => {
            // recognition.start();
            // start = true

            if (start != true && index == 0) {
                speak("Recording start");
                startRec();
            } else if (start != true && index > 0) {

            } else {
                stopRec();
            }
        };
    }


    function startRec() {
        driver(index)
            //     recognition.start();
            //     start = true
        recordIcon.style.visibility = 'visible';
    }

    function stopRec() {
        recordIcon.style.visibility = 'hidden';
        start = false
        recognition.stop();
    }
    var studentid = 12458
    submit.addEventListener('click', (e) => {
        e.preventDefault()
        url = ""
        const data = {
            studentid: studentid,
            studentname: studentName,
            answerone: answer[0],
            answertwo: answer[1],
            answerthree: answer[2],
        }
        console.log(data)

        $.ajax({
            method: "post",
            url: url,
            dataType: "json",
            data: data,
            success: function(responce) {
                console.log(responce)
            },
            error: function(error) {
                console.log(error)
            },

        })
    })

    function driver(index) {
        console.log("driver");
        //First Function to call on website load
        //load question
        var questionPanel = document.querySelector('#questionPanel');
        //console.log(questionPanel)
        questionPanel.innerText = question[index]
        console.log(question.length - 1)
        speak(question[index]);
        if (index == question.length - 1) {
            console.log("her")
            submit.style.visibility = 'visible';
        } else {
            submit.style.visibility = 'hidden';
        }
        //console.log(question[index])

        texts.innerText = answer[index];
        copytext = "ANSWER: "
        if (start != true) {
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
    //  driver(index)
    // var starttest = document.getElementById('StartTest').addEventListener('click', (e) => {
    //     window.location.href = "./test";
    // })
}