let n = 1;

const button = document.querySelector('#addinput-button');
const form = document.querySelector('form')
const submitButton = document.querySelector('#submit-button');

button.addEventListener('click', (ev) => {
    ev.preventDefault();
    const newInput = document.createElement('div');
    newInput.classList.add('form-group');
    newInput.innerHTML = `
        <label for="book-input-${n}">Livre:</label>
        <input type="text" id="book-input-${n}" class="form-control book-input">
    `;
    n++;
    form.insertBefore(newInput, submitButton);
    setAutocomplete();
});