/*function addOperationInput() {
    const formsetContainer = document.getElementById('operations-container');
    const totalForms = formsetContainer.querySelectorAll('.operation').length;

    const lastForm = formsetContainer.querySelector('.operation:last-of-type');
    const lastOperationName = lastForm.querySelector('input[name*=operation_name]').value;
    const lastTimeAllowed = lastForm.querySelector('input[name*=time_allowed]').value;

    // Check if the last form has empty values
    if (lastOperationName.trim() === '' && lastTimeAllowed.trim() === '') {
        console.log('Last form has empty values. Not adding a new form.');
        return; // Exit the function without adding a new form
    }

    const newForm = lastForm.cloneNode(true);

    newForm.querySelectorAll('input, select').forEach((element) => {
        element.value = '';  
        element.name = element.name.replace(`-${totalForms - 1}-`, `-${totalForms}-`);
        element.id = `id_${element.name}`;
    });

    formsetContainer.appendChild(newForm);

    // Logging the form data before submission
    const formArray = Array.from(formsetContainer.querySelectorAll('.operation'));
    const formData = [];
    formArray.forEach(form => {
        const operationName = form.querySelector(`input[name*=operation_name]`).value;
        const timeAllowed = form.querySelector(`input[name*=time_allowed]`).value;
        formData.push({ operationName, timeAllowed });
    });
    console.log('Form Data before submission:', formData);
}
*/