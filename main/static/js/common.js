let startTime;
let operationStartTime;
let elapsedTime = 0;
let timestamps = [];
let operationIndex = 1;

function sendToDjangoDatabase(dataToSend, selectedGarmentId) {
  console.log('Sending data to Django:', dataToSend);

  fetch(`/main/update_operation/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      totalElapsed: dataToSend.totalElapsed,
      individualTimes: dataToSend.individualTimes,
      percentageProgress: dataToSend.percentageProgress,
      selectedGarmentId: selectedGarmentId,
    }),
  })
  .then(response => response.json())
  .then(data => console.log('Data sent to Django:', data))
  .catch(error => console.error('Error sending data to Django:', error));
}

function startStopwatch() {
  console.log('Starting stopwatch...');
  startTime = new Date().getTime();
  operationStartTime = startTime;
  setInterval(updateStopwatch, 10);
}

function updateStopwatch() {
  const currentTime = new Date().getTime();
  elapsedTime = (currentTime - startTime) / 1000;
  const operationElapsedTime = (currentTime - operationStartTime) / 1000;
  console.log('Updating stopwatch. Elapsed Time:', elapsedTime, 'Operation Elapsed Time:', operationElapsedTime);
  updateDisplay(operationElapsedTime);
}

function updateDisplay(operationElapsedTime) {
  console.log('Updating display with Operation Elapsed Time:', operationElapsedTime);
  const displayElement = document.getElementById('stopwatch-display');
  displayElement.innerText = formatTime(elapsedTime, operationElapsedTime);
}

function displayTimestamps() {
  console.log('Displaying timestamps...');
  const timestampsElement = document.getElementById('recorded-timestamps');
  timestampsElement.innerHTML = "";

  timestamps.forEach((record, index) => {
    const li = document.createElement('li');
    const operationTime = index > 0 ? (record.elapsed - timestamps[index - 1].elapsed) : record.elapsed;
    const operationEfficiency = operationTime - timeAllowed;
    const percentageProgress = (record.index) * 100 / quantity;
    li.innerText = `${index + 1}. Operation ${record.index}: ${formatOperationTime(operationTime)} (Total Elapsed: ${formatTime(record.elapsed)}) seconds, efficiency: ${formatEfficiency(operationEfficiency)}, progress %: ${percentageProgress}`;
    timestampsElement.appendChild(li);
  });
}

function recordTimestamp(selectedGarmentId) {
  console.log('Recording timestamp for Operation', operationIndex, 'of Garment', selectedGarmentId);
  if (timestamps.length < quantity) {
    const timestamp = new Date().getTime();
    timestamps.push({ index: operationIndex, timestamp, elapsed: elapsedTime });
    console.log(`Operation ${operationIndex} completed in ${formatTime(elapsedTime)} seconds`);
    operationIndex++;
    operationStartTime = new Date().getTime();
    displayTimestamps();

    const totalElapsed = elapsedTime;
    const individualTimes = timestamps.map(record => record.elapsed);
    const percentageProgress = (operationIndex - 1) * 100 / quantity;

    const dataToSend = {
      totalElapsed: totalElapsed,
      individualTimes: individualTimes,
      percentageProgress: percentageProgress,
      selectedGarmentId: selectedGarmentId, // Corrected variable name
    };

    console.log('Data to send:', dataToSend);
    
    sendToDjangoDatabase(dataToSend);
  } else {
    console.log("END OF PRODUCTION FOR THIS OPERATOR");
  }
}

function formatTime(totalElapsed) {
  const totalMinutes = Math.floor(totalElapsed / 60);
  const totalRemainingSeconds = Math.floor(totalElapsed % 60);
  const totalMilliseconds = Math.floor((totalElapsed % 1) * 1000);
  return `${totalMinutes}m ${totalRemainingSeconds}s ${totalMilliseconds}ms`;
}

function formatOperationTime(operationTime) {
  const operationSeconds = Math.floor(operationTime);
  const operationMilliseconds = Math.floor((operationTime % 1) * 1000);
  return `${operationSeconds}s ${operationMilliseconds}ms`;
}

function formatEfficiency(efficiency) {
  const efficiencySeconds = Math.floor(Math.abs(efficiency));
  const efficiencyMilliseconds = Math.floor((Math.abs(efficiency) % 1) * 1000);
  const formattedMilliseconds = ('00' + efficiencyMilliseconds).slice(-3);
  const sign = efficiency >= 0 ? '+' : '-';
  return `${sign}${efficiencySeconds}s ${formattedMilliseconds}ms`;
}

document.addEventListener('DOMContentLoaded', function () {
  console.log('DOM content loaded.');
  const garmentDropdown = document.getElementById('garmentDropdown');
  const operationDropdownContainer = document.getElementById('operationDropdownContainer');

  function updateOperationsDropdown() {
    var selectedGarmentId = garmentDropdown.value;
    console.log('Selected Garment ID:', selectedGarmentId);

    const operationDropdown = document.getElementById('operationDropdown');
    if (!operationDropdown) {
      console.error('Operation Dropdown not found.');
      return;
    }

    fetch(`/main/get_operations/${selectedGarmentId}/`)
      .then(response => {
        console.log('Response Status:', response.status);

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const contentType = response.headers.get('Content-Type');
        console.log('Content-Type:', contentType);

        if (contentType && contentType.includes('application/json')) {
          return response.json();
        } else {
          return response.text();
        }
      })
      .then(data => {
        operationDropdownContainer.style.display = 'block';
        console.log('Data received:', data);

        operationDropdown.innerHTML = "";

        for (var i = 0; i < data.length; i++) {
          var option = document.createElement("option");
          option.value = data[i].id;
          option.text = data[i].operation_name;
          operationDropdown.add(option);
        }
      })
      .catch(error => {
        console.error('Error fetching operations:', error);
      });
  }

  garmentDropdown.addEventListener('change', function () {
    updateOperationsDropdown();
  });

  window.startStopwatch = startStopwatch;
  window.recordTimestamp = recordTimestamp;

  console.log('Functions attached to window object.');
});
