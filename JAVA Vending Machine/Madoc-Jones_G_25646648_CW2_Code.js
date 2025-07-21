const readline = require('readline');  // Code Academy(2024),Getting User Input in Node.js [Online] Available from: https://www.codecademy.com/article/getting-user-input-in-node-js [Accessed 17th November 2024]
const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let credits = 0;  // Variables that need global scope for the application to run.
let totalamount = 0;   // These variables will be used among a variety of functions therefore they need to be global to allow each function to recognise them.
let items = [];
let purchased_items = [];
let hashtable = {};
let itemname = "";
let itemprice = 0;

function main_menu() {  // Main Menu function this is the starting point of the application.
    console.log("-------------------- \n Vending Machine \n --------------------");
    console.log("Main Menu \n 1. Add Credits (Current Credits) =", credits, "\n 2. Select Products", "\n 3. Purchased Products", "\n 0. Exit \n");
    reader.question("Please select your option: ", choice => {
        if (choice == 1) {
            addcredits(); // Calls the addcredits() function.
        }
        if (choice == 2) {
            productselection(); // Calls the productselection() function.
        }
        if (choice == 3) {
            viewpurchases();  // Calls the viewpurchases() function. 
        }
        if (choice == 0) {
            console.log("User Triggered Shutdown");
            process.exit(); // BetterStack(2024) How to exit in Node.js [Online] Available from: https://betterstack.com/community/questions/how-to-exit-in-node-js/ [Accessed 19th November 2024]
        }
        else if (choice < 0 || choice > 3 || isNaN(choice)) { // these values have to be used to specify the range for this condition to trigger. In developing the application, if the values were not specified this condition would sometimes trigger. Mdn web docs (2024) isNaN() [Online] Available from: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN [Accessed 20th November 2024]
            console.log("ERROR, Invalid Input, Please try again");
            console.log("Proceeding back to Main Menu")
            setTimeout(main_menu, 2000); // Mdn Web Docs Window: setTimeout() method [Online] Available from https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout [Accessed 20th November 2024]
        }
    })
}

function addcredits() {
    reader.question("Please select how many Credits you would like: ", input => {
        creditinput = parseInt(input); // Makes sure only integers can be input.
        if (creditinput < 0 || isNaN(creditinput)) {  // // Mdn web docs (2024) isNaN() [Online] Available from: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN [Accessed 20th November 2024]
            console.log("ERROR!! Credits must be postive and/or credits must always be a number \nPlease try again");
            addcredits(); // Restarts the function.
        }
        else {
            credits += creditinput; // Assigns credit value
            console.log("You now have: ", credits, "credits.", "\nReturning to Main Menu");
            setTimeout(main_menu, 2000); // Returns to main menu after 2 seconds. This gives the user a chance to read through the terminal and understand what they have done before they do anything else. Mdn Web Docs Window: setTimeout() method [Online] Available from https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout [Accessed 20th November 2024]
        }
    })
}

function productselection() {
    console.log("PRODUCT SELECTION  [Current Credits] =", credits, "[Current Items] = ", items); // Each product is input to the console then a new line occurs to stack each product upon each other.
    console.log("Please choose from the following options: \n",
        "1. Chocolate Bar [0.80 credits]", '\n',
        "2. Soda Can [0.70 credits]", '\n',
        "3. Soda Bottle [1.25 credits]", '\n', // This is a cleaner way of listing the items instead of having them in one straight line.
        "4. Crisps  [0.50 credits]", '\n',
        "5. Cookies [1.10 credits]", '\n',
        "6. Cancel Purchases", '\n',
        "7. Checkout Now", '\n',
        "0. Return to Main Menu", '\n');

    reader.question("Please choose an option:", item_choice => {
        item_choice = parseInt(item_choice);
        if (item_choice == 1) {
            complete_purchase('Chocolate Bar', 0.80);  // Each item choice calls the complete_purchase function and defines the set parameters. This is a more streamlined way than having 6 copies of the same code each tweaked a little.
        }
        if (item_choice == 2) {
            complete_purchase('Soda Can', 0.70);
        }
        if (item_choice == 3) {
            complete_purchase("Soda Bottle", 1.25);
        }
        if (item_choice == 4) {
            complete_purchase("Crisps", 0.50);
        }
        if (item_choice == 5) {
            complete_purchase("Cookies", 1.10);
        }
        if (item_choice == 6) {
            cancelpurchase();
        }
        if (item_choice == 7) {
            checkout();
        }
        if (item_choice == 0) {
            console.log("Incomplete Purchases will be stored until purchase is complete/purchase is cancelled.")
            main_menu();
        }
        else if (item_choice < 0 || item_choice > 7 || isNaN(item_choice)) {  // This catches the error when a user inputs a value that is not specified. Using this the console tells the user the error and re runs the Product Selection Error. Mdn web docs (2024) isNaN() [Online] Available from: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN [Accessed 20th November 2024]
            console.log("ERROR! Invalid input Please try again");
            productselection();
        }
    })
}

function cancelpurchase() { // This function will run if the user goes back to the main menu midway through a purchase. Acting as a cancelation 
    reader.question("Are you sure you would like to go cancel purchases. \n This will cancel any purchases that have not been completed. \n Press 1 if you would like to Continue Cancellation, Press 2 if you would like to Continue Purchases: ", input => {
        input = parseInt(input)
        if (input == 1) { // Wipes incomplete purchases. Takes User back to productselection wiping there current purchases.
            items.length = 0; // This clears the array. By setting the length to 0. Sentry 2022 How do I empty an Array in Javascript Available from: https://sentry.io/answers/how-do-i-empty-an-array-in-javascript/ [Accessed 22nd November 2024]
            totalamount = 0;
            console.log("Wiping Shopping Cart ");
            console.log("Clearing Sub Total");
            console.log("Returning To Product Selection");
            setTimeout(productselection, 2000);
            return;
        }

        if (input == 2) { // Allows a user to return to product selection. This could be useful if they want to complete a purchase.
            console.log("Returning to Product Selection");
            productselection();
            return;
        }

        if (input < 0 || input > 2 || isNaN(input)) { // Error management Mdn web docs (2024) isNaN() [Online] Available from: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN [Accessed 20th November 2024]
            console.log("ERROR Invalid Input please type 1 for Yes and type 2 for No");
            cancelpurchase();
        }
    })
}

function complete_purchase(itemname, itemprice) { // W3 Schools (2024) JavaScript Function Parameters [Online] Available from: https://www.w3schools.com/js/js_function_parameters.asp [Accessed 22nd November 2024]
    if (credits < itemprice) {
        console.log("Error! Insufficient credits please add more \nReturning to Credit Purchase");
        setTimeout(addcredits, 2000);
    }
    if (credits >= itemprice) { // This code runs if the User's credit value is equal or more than the Value of the Item
        reader.question(`How many ${itemname}/s do you want: `, input => {  // This asks the user how many Items they want.Stack Overflow 2024 What does ${}(dollar sign and curly brackets) mean in JavaScript? Available from: https://stackoverflow.com/questions/35835362/what-does-dollar-sign-and-curly-braces-mean-in-a-string-in-javascript [Accessed 23rd November 2024]
            var totalcost;  // The totalcost variable will be used as a calculation of cost. Once the user has decided to complete a purchase this value will be transferred to the totalamount variable.
            amount = parseInt(input); // This assigns the Input value to the variable amount
            totalcost = amount * itemprice;  // Calculation of cost
            if (amount <= 0 || isNaN(amount)) { // Amount Error Management. Prevents Negative Amount Inputs
                console.log("Error! Restarting Purchase");
                complete_purchase(itemname, itemprice);
                return;
            }
            console.log("Current sub total =", totalcost); // Acts as a checkpoint 
            if (credits < totalcost) {
                console.log("Insufficient Credits! Please insert more credits and try again.");
                setTimeout(addcredits, 2000);
            }
            if (credits >= totalcost) {
                items.push(amount, itemname); // W3 Schools 2024 JavaScript Array Push() Available from: https://www.w3schools.com/jsref/jsref_push.asp [Accessed 23rd November 2024]
                totalamount += totalcost;  // This sets the totalamount and totalcost equal to eachother/
                console.log("Total Purchase Value so far", totalamount);
                checkout();
            }
        })
    }
} // This will be the basis for every purchase

function checkout() {
    reader.question("Would you like to add another product to your bag or checkout? Please input 1 for adding another product and 2 for checkout: ", input => {
        rebuy = parseInt(input);
        if (rebuy == 1) {
            console.log("You have chosen to purchase another product. Returning to Product Selection.")
            productselection();
            return;
        }
        if (rebuy == 2) {
            if (credits < totalamount) {// This code runs if the user wants to purchase many items but has insufficient credits. This stores the shopping bag, the sub total and total and sends the user back to the credits purchase. Therfore allowing the user to comoplete the purchase once they have added sufficient credits.
                console.log("Error! Insufficient Credits. \n Please Insert More Credits.\n Purchase data will be kept to allow purchase completion once necessary credits reached.");
                console.log("Returing to Credit Purchase. \n");
                addcredits();
                return;
            }
            purchased_items.push(...items); // This moves the items selected to a seperate array when the purchse is complete.
            items = []; // This clears the original array to prevent duplication of items.
            credits = credits - totalamount;  // Cost Deduction
            totalamount = 0; // Wipes purchase value after successful cost deduction
            console.log(amount, itemname, 'added to bag'); // This shows the user how much they have bought.
            console.log('You now have', credits, "credits");
            arraytohashtable(); // Conversion of storing array items to a hashtable to help merge any duplicate purchases
            handlerefund();  //Function to handle the refund process
        }
        else { //This is if the rebuy option is anything other than 1 or 2
            console.log("ERROR INVALID INPUT!");
            console.log("Restarting Checkout Process")
            checkout(); // This starts the process of checkout.
        }
    })
}

function arraytohashtable() { // This function will loop through the array of purchased items and sort through them to store them appropriately in a hash table.
    for (let i = 0; i < purchased_items.length; i += 2) {  // This loops through the array in groups of two. FreeCodeCamp(2023) How to Loop Through Arrays in JavaScript [Online] Available from: https://www.freecodecamp.org/news/loop-through-arrays-javascript/ [Accessed 10th January 2025]
        let amount = purchased_items[i]; // In the purchased_items array the amount goes first. 
        let itemname = purchased_items[i + 1]; // Then the itemname goes second. This is taken from the way purchases are pushed in the completepurchase function.
        if (hashtable[itemname]) { // This IF statement checks if there are duplicate item names meaning multiple purchases of the same item. If there is the amount of both the purchases will be merged.
            hashtable[itemname].amount += amount;
        } else {
            hashtable[itemname] = { amount: amount };
        }
    }
    purchased_items.length = 0; // This wipes the array after the process is complete to prevent duplicate purchases going through and ensuring accuracy. 
}

function handlerefund() {
    reader.question("Do you want to refund your credits? \n Type 1 for Yes and Type 2 for No.", refund => {
        if (refund == 1) {  // Runs if user wants a refund.
            console.log("Refunding Credits.");
            credits = 0; // Wipes Users credits.
            console.log("Returning to Main Menu");
            setTimeout(main_menu, 2000);
        }
        if (refund == 2) {  // Runs if user does not want a refund.
            console.log("Credits have remained at", credits);
            console.log("Returning to Main Menu");
            setTimeout(main_menu, 2000);
        }
        else if (refund < 1 || refund > 2 || isNaN(refund)) {  // Error Handling. Mdn web docs (2024) isNaN() [Online] Available from: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN [Accessed 20th November 2024]
            console.log("ERROR! Invalid Input. Please Enter Only 1 or 2"); // This loops the function if there is any incorrect input
            handlerefund();
        }
    })
}

function viewpurchases() {
    console.log("--------------- \n Current Purchased Items \n --------------- ")
    console.log(hashtable);
    console.log("Returning to Main Menu")
    setTimeout(main_menu, 2000); // Mdn Web Docs Window: setTimeout() method [Online] Available from https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout [Accessed 20th November 2024]
}

main_menu(); // Starts the whole process