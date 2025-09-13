/*
let marks = prompt("enter marks ");
let grade;
if (marks >=90&& marks <= 100) {
    grade="A";
} else if (marks >=70 && marks <= 89) {
    grade="B";
} else if (marks >=60 && marks <=69) {
    grade="C";
} else if (marks >=50 && marks <=59) {
    grade="D";
} else if (marks >=0 && marks <=49) {
    grade="F";
} else {
    console.log("Invalid marks entered");
}
console.log("Your grade is " + grade);

*/



/*
let num = 25;
let i =0;
while (i>=0){
    i++;
    let guess = prompt("guess a number between 1 and 100");
    if (guess == num){
        console.log("you guessed it right");
        break;
    }
    else if(guess != num){
        console.log("you guessed it wrong, try again");
    }
}
*/


/*
let str= prompt("enter your full name ");
let str1= `@${str}${str.length}`;
console.log(str1);
*/

/*

let cities = ["karachi", "lahore", "islamabad", "peshawar", "quetta"];
for (city of cities){
    console.log(city);
}
*/

/*
let price = [250,645,300,900,50];
let i=0;
for ( let x of price ){
    x=x/10;
    price[i]= price[i] - x; 
    i++;

}
console.log(price);
*/

/*
 let marks = [50, 60, 70, 80, 90];
 marks.slice(2, 4);
 console.log(marks.slice(2, 4));
 */
/*

const countVow= (str) =>{
    let y = prompt("enter a string ");
    z=0;
    for (let i=0; i<y.length; i++){
        x= y[i]
        if (x == "a" || x == "e" || x == "i" || x == "o" || x == "u"){
            z++;
        
        }
    }
    console.log("number of vowels in the string are " + z );
}

*/
/*
let arr=[1,2,3,4,5,6,7,8,9,10];
arr.forEach ((val,idx,arr) =>{
    console.log(val,idx,arr);
});


*/
/*
let nums = [1,2,3,4,5,6,7,8,9,10];
 nums.forEach((val) => {
    console.log(val*val);
}) 

*/


// Replace with your real API key and endpoint

const API_KEY = '8966b12998d647a789a64717251804';

// Get DOM elements
const cityElement = document.getElementById("city");         // <span id="city">...</span>
const searchInput = document.getElementById("q");            // input field
const submitBtn = document.getElementById("submit");         // search button

// Function to fetch and display weather data
const getWeather = (cityName) => {
  if (!cityName) return;

  const API_URL = `http://api.weatherapi.com/v1/current.json?key=${API_KEY}&q=${cityName}&aqi=no`;

  fetch(API_URL)
    .then(response => {
      if (!response.ok) {
        throw new Error("City not found");
      }
      return response.json();
    })
    .then(data => {
      const Humidity = data.current.humidity;
      const Temp_C = data.current.temp_c;
      const Wind_Mph = data.current.wind_mph;

      // Update weather values
      document.getElementById('humidity-value').textContent = `${Humidity}%`;
      document.getElementById('temp-value').textContent = `${Temp_C}°C`;
      document.getElementById('wind-value').textContent = `${Wind_Mph} mph`;

      // Update the city name in navbar
      cityElement.textContent = cityName;
    })
    .catch(error => {
      console.error("API call error:", error);
    });
};

// Handle search form submission
submitBtn.addEventListener("click", (e) => {
  e.preventDefault(); // prevent page reload
  const cityName = searchInput.value.trim();
  getWeather(cityName);
});

// Initial load with default city
getWeather("Delhi");
