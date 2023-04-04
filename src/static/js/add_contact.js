
  // Wait for the DOM to load
  document.addEventListener('DOMContentLoaded', () => {
    const formContainer = document.getElementById('form-container');
    const addInputButton = formContainer.querySelector('.add-input');
    
    // Add a click event listener to the "Add Input" button
    addInputButton.addEventListener('click', () => {
      // Create the new input element
      const newInput = document.createElement('div');
      newInput.classList.add('form-row');
      newInput.innerHTML = `
                <div class="form-group col-md-3">
                    <label>Address ${formContainer.children.length}:</label>
                    <input type="text" class="form-control" name="address[address${formContainer.children.length}][text]">
                  </div>
                  <div class="form-group col-md-3">
                    <label>Title ${formContainer.children.length}:</label>
                    <input type="text" class="form-control" name="address[address${formContainer.children.length}][title]">
                  </div>
                  <div class="form-group col-md-2">
                    <label>Postal Code ${formContainer.children.length}:</label>
                    <input type="text" class="form-control" name="address[address${formContainer.children.length}][postal_code]">
                  </div>
                  <div class="form-group col-md-3">
                    <label>Phone ${formContainer.children.length}:</label>
                    <input type="text" class="form-control" name="address[address${formContainer.children.length}][phone]">
                  </div>
                  <div class="form-group col-md-1 position-relative mt-5 mt-md-0">
                    <button class="remove-input btn btn-danger position-absolute fixed-bottom" type="button">X</button>
                  </div>
      `;
      
      // Add a click event listener to the new "Remove" button
      const removeInputButtons = newInput.querySelectorAll('.remove-input');
      removeInputButtons.forEach(button => {
        button.addEventListener('click', () => {
          newInput.remove();
        });
      });
      
      // Add the new input element to the form container
      formContainer.insertBefore(newInput, addInputButton);
    });
    
    // Add click event listeners to the existing "Remove" buttons
    const removeInputButtons = formContainer.querySelectorAll('.remove-input');
    removeInputButtons.forEach(button => {
      button.addEventListener('click', (event) => {
        event.target.parentElement.parentElement.remove();
      });
    });
  });
