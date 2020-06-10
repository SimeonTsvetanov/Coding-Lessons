function create(words) {                                    // We will receive a list of strings 
   words.map(word => {                                      // Map the strings one by one
      let div = document.createElement('div');              // Crete the DIV
      let p = document.createElement('p');                  // Create the P
      p.innerText = word;                                   // Add the word to the p
      p.style.display = "none";                             // Hide the p
      div.appendChild(p);                                   // Append the p to the div
      div.addEventListener('click', (e) => {                // Now add the Event listener
         e.target.children[0].style.display = 'block';      // To make the p visual if someone click on the div   
      });                                                   // And finally:
      document.getElementById('content').appendChild(div);  // Add the div to the parent div
   })
}
 