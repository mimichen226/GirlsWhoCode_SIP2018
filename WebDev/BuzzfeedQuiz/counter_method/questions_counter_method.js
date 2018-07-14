(function createQuestions(){
  var questions = [
    {
      "question": "what is ur fave color",
      "name": "colors",
      "answers" : {
        "red": "broccoli",
        "green": "zucchini",
        "blue": "carrot"
      }
    },
    {
      "question": "what is ur fave animal",
      "name": "animal",
      "answers" : {
        "penguin": "broccoli",
        "giraffe": "zucchini",
        "dog": "carrot"
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

  var score = {
  "zucchini": 0,
  "broccoli": 0,
  "carrot": 0
  };
  var categories = ["colors","animal"];
  for (var j = 0; j < categories.length; j ++){
    var cat = document.getElementsByName(categories[j]);
    for (var i = 0; i < cat.length; i++){
      if (cat[i].checked){
        score[cat[i].value] = score[cat[i].value] + 1;
      }
    }
  }

  var win_veggie;
  var win_score = 0;

  for (var key in score){

    if (score[key] > win_score){
      win_score = score[key];
      win_veg = key;
    }
  }
  // SPIRIT VEGETABLE

  document.getElementById("results").innerHTML = "YOU ARE A " + win_veg.toUpperCase();
}
