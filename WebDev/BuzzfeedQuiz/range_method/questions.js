(function createQuestions(){
  var questions = [
    {
      "question": "what is ur fave color",
      "name": "colors",
      "answers" : {
        "red": 5,
        "green": 2,
        "blue": 3
      }
    },
    {
      "question": "what is ur fave animal",
      "name": "animal",
      "answers" : {
        "penguin": 0,
        "giraffe": 7,
        "dog": 2
      }
    }
  ];

  var html = "";
  for (var i = 0; i < questions.length; i++){
    html += questions[i]["question"] + "<br>";
    for (var key in questions[i]["answers"]){
      html += '<input type="radio" name="' + questions[i]["name"] + '" value="';
      html += questions[i]["answers"][key] + '">' + key + "<br>";
    }
  }
  document.getElementById("survey").innerHTML= html;
})();

function submitAnswer(){
  var total = 0;
  var categories = ["colors","animal"];

  // Outer loop goes through categories to get our question name
  for (var j = 0; j < categories.length; j ++){
    var cat = document.getElementsByName(categories[j]);
    for (var i = 0; i < cat.length; i++){
      if (cat[i].checked){
        total += parseInt(cat[i].value);
      }
    }
  }

  // SPIRIT VEGETABLE
  var veggie;
  if (total < 5){
    veggie = "Broccoli";
  } else if (total < 10) {
    veggie = "Carrot";
  } else {
    veggie = "Zucchini";
  }
  document.getElementById("results").innerHTML = "YOU ARE A " + veggie.toUpperCase();
}
