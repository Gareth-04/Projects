'use strict';


window.onload = function () {  // onload means that the all the javascript here will work when the website is fully loaded.
  document.getElementById('Readall').style.visibility='visible';  // When the webpage is loaded the READ ALL REVIEWS button is visible but the READ LESS REVIEWS button is hidden until the READ ALL REVIEWS button is clicked.
  document.getElementById('hide_reviews').style.visibility='hidden';

  let option = {
  method: "GET"
}
  

  fetch ('https://cis1110apicw.computing.edgehill.ac.uk/reviews', option)  // this fetches the data from the review API
  .then(function(response) {
    return response.json();  // function to return the data from the api in the form of JSON.
  })
  .then(function(Data) {  // function to load the first 5 reviews
    for(let i = 0; i < 5; i++) {
      let nickname = Data[i].nickname;  // the Data[i].nickname gives the name nickname to the nickname data retrieved from the API
      let review = Data[i].review;
      let stars = Data[i].rating;
      RenderData(nickname,review,stars);
    }
  })
 

  function StarRating (rating) { // function to convert the rating integer into a star total The stars are used from Alt-Codes,2024. Star Symbols Alt Codes [Online] Available from : https://www.alt-codes.net/star_alt_code.php [Accessed 2nd January 2024]
    let stars = " ";
    if (rating == 1) {
      stars = "★ ☆ ☆ ☆ ☆";  // this function converts the rating integer from the API into a star output.
    }
    else if (rating == 2) {
      stars = " ★ ★ ☆ ☆ ☆"
    }
    else if (rating == 3) {
      stars = "★ ★ ★ ☆ ☆ "
    }
    else if (rating == 4) {
      stars = "★ ★ ★ ★ ☆"
    }
    else if (rating == 5) {
      stars = "★ ★ ★ ★ ★ "
    }
    return stars
  }


  function RenderData(nickname, review, stars) {  // function to display the data retrieved from the API
    let reviewtext = document.createElement("div");
    reviewtext.className = "Onscreen Review";

  
  let star_box = document.createElement("p");  // each box creates a p element for each retrieved data set. 
  star_box.className = "star_placement";
  star_box.innerText = StarRating(stars);


  let nickname_box = document.createElement("p");
  nickname_box.className = "nickname_placement";
  nickname_box.innerText = nickname;


  let review_box = document.createElement("p");
  review_box.className = "review_placement";
  review_box.innerText = review;


  let profile_image = document.createElement("img"); // this adds the first image to the pre loaded reviews. Once the button is clicked the secondary image will be loaded.
  profile_image.src = "robot-juice-images/reviewicon1.jpg";
  profile_image.className = "icon1";
  profile_image.alt = "Red Picture with a white robot standing in the middle of the image."

  let border = document.createElement('hr');
  border.className = "border";


  let combined_review = document.createElement("div");  // this creates a div for all the elements in the review. 
  combined_review.id = "full_review";
  combined_review.appendChild(profile_image);
  combined_review.appendChild(star_box);
  combined_review.appendChild(nickname_box);  // the combined_review.appendChild elements adds all the p elements created previously to a defined box. This box is then attached to another main div to all the reviews to put into blocks.
  combined_review.appendChild(review_box);
  combined_review.appendChild(border);
  reviewtext.appendChild(combined_review);


  let review_section = document.getElementById("ProductReviews");  // this function adds the retrieved review data and their assigned boxes to the main established div in the html.
  review_section.appendChild(reviewtext);
  }


let show_all = document.getElementById("Readall");


show_all.addEventListener("click", event => {  // This adds an event to the READ ALL REVIEWS button when it is clicked, this button uses the same function as when the webpage is loaded but changes the reviews from being the 5th review up.


  fetch ('https://cis1110apicw.computing.edgehill.ac.uk/reviews', option)
  .then(function(response) {
    return response.json();  // function to return the data from the api in the form of JSON.
  })
  .then(function(Data) {  // function to load the final reviews
    for(let i = 5; i < Data.length; i++) {
      let nickname = Data[i].nickname;  // the Data[i].nickname gives the name nickname to the nickname data retrieved from the API
      let review = Data[i].review;
      let stars = Data[i].rating;
      RenderAllData(nickname,review,stars)
    }


    function RenderAllData(nickname, review, stars) {  // function to display the data retrieved from the API This version displays all reviews from the API
      let reviewtext = document.createElement("div");
      reviewtext.className = "Onscreen Review";
  
    
    let star_box = document.createElement("p");  // each box creates a p element for each retrieved data set. 
    star_box.className = "star_placement";
    star_box.innerText = StarRating(stars);
  
  
    let nickname_box = document.createElement("p");
    nickname_box.className = "nickname_placement";
    nickname_box.innerText = nickname;
  
  
    let review_box = document.createElement("p");
    review_box.className = "review_placement";
    review_box.innerText = review;
  
  
    let profile_image = document.createElement("img"); // this adds the second icon image to the next set of reviews. 
    profile_image.src = "robot-juice-images/reviewicon2.jpg";
    profile_image.className = "icon2";
    profile_image.alt = "White Image with a robot standing up in the middle of the image. The robot is silver."
  

    let border = document.createElement('hr');
    border.className = "border";
  
  
    let combined_review = document.createElement("div");  // this creates a div for all the elements in the review. 
    combined_review.id = "full_review";
    combined_review.appendChild(profile_image);
    combined_review.appendChild(star_box);
    combined_review.appendChild(nickname_box);  // the combined_review.appendChild elements adds all the p elements created previously to a defined box. This box is then attached to another main div to all the reviews to put into blocks.
    combined_review.appendChild(review_box);
    combined_review.appendChild(border);
    reviewtext.appendChild(combined_review);
  
  
    let review_section = document.getElementById("ProductReviews");  // this function adds the retrieved review data and their assigned boxes to the main established div in the html.
    review_section.appendChild(reviewtext);
    }
     let hide_reviews = document.getElementById("hide_reviews");
     hide_reviews = document.getElementById("hide_reviews").style.visibility="visible"; // when the READ ALL REVIEWS Button is clicked the button is hidden and the READ LESS REVIEWS Button becomes visible


  })
  document.getElementById('Readall').style.visibility='hidden';  // this hides the READ ALL REVIEWS button when it's clicked. The button will reappear when the Less Reviews button is clicked.
})


let hide_review = document.getElementById("hide_reviews");

function reload () {
  window.location.reload(); // Sentry, 2023. How do I refresh a page using JavaScript [Online] Available from: https://sentry.io/answers/how-do-i-refresh-a-page-using-javascript/#:~:text=Using%20history.go()&text=If%20you%20add%20no%20argument,the%20current%20page%20will%20reload. [Accessed 3rd January 2024]
}
  hide_review.addEventListener("click",reload); {  // this allows the button when clicked to remove the extra reviews added with the read all button. This function reloads the webpage to its original state.
    document.getElementById("hide_reviews").style.visibility = "hidden";
  document.getElementById('Readall').style.visibility='visible';  // When The READ LESS REVIEWS Button is clicked the READ ALL REVIEWS Button is visible again.
  }

} // This fully closes the JavaScript and ends the Window onload function. 
