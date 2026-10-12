const form = document.querySelector('.todo_form');
const todocontainer = document.querySelector('.todo-container');

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const form = document.querySelector('.todo_form');

        const todo_item_div = document.createElement("div");
        const todo_text_div = document.createElement("div"); 

        const heading = document.createElement("h3");
        const para = document.createElement("p");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";

        checkbox.classList.add("todo_btn");
        todo_item_div.classList.add("todo_item");

        todo_text_div.classList.add("todo_text");
     
        // Get form data
        const title = form.elements["title"].value;
        const description = form.elements["description"].value;
     
        heading.textContent = title;
        para.textContent = description;

        // assign form data into our html elements
        heading.textContent = title;
        para.textContent = description;
     
        // Add our elements to the DOM
        todo_text_div.appendChild(heading);
        todo_text_div.appendChild(para);
     
        todo_item_div.appendChild(todo_text_div);
        todo_item_div.appendChild(checkbox);
     
        todocontainer.appendChild(todo_item_div);
     
        // bonus content for adding strikeout on button press
        checkbox.addEventListener('change', () => {
            if (checkbox.checked) {
                todo_text_div.style.textDecoration = "line-through";
                todo_text_div.style.color = "black";
            } else {
                todo_text_div.style.textDecoration = "none";
                todo_text_div.style.color = "";
            }
        });
     
        form.reset();
    });

    deletebtn.addEventListener("click",() => {
        todocontainer.removeChild(todo_item_div);
    });
    form.reset();