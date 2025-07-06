<script>
  import { createEventDispatcher } from 'svelte';

  let moisture = '';
  let temperature = '';
  let lightIntensity = '';
  let notes = '';

  const dispatch = createEventDispatcher();

  async function handleSubmit(event) {
    event.preventDefault();

    const formData = {
      moisture_level: parseFloat(moisture),
      temperature: parseFloat(temperature),
      light_intensity: parseFloat(lightIntensity),
      notes: notes,
      timestamp: new Date().toISOString(),
      plant_id: 1
    };

    try {
      const response = await fetch('/api/add_reading', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        const data = await response.json();
        alert('Reading added successfully!');
        moisture = '';
        temperature = '';
        lightIntensity = '';
        notes = '';
        dispatch('readingAdded', data);
      } else {
        alert('Failed to add reading.');
      }
    } catch (error) {
      alert('Error submitting reading: ' + error.message);
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <div>
    <label for="moisture">Soil Moisture (%)</label>
    <input id="moisture" type="number" bind:value={moisture} min="0" max="100" step="0.1" required />
  </div>

  <div>
    <label for="temperature">Temperature (°C)</label>
    <input id="temperature" type="number" bind:value={temperature} step="0.1" required />
  </div>

  <div>
    <label for="lightIntensity">Light Intensity (Lux)</label>
    <input id="lightIntensity" type="number" bind:value={lightIntensity} min="0" step="1" required />
  </div>

  <div>
    <label for="notes">Notes</label>
    <textarea id="notes" bind:value={notes} rows="3"></textarea>
  </div>

  <button type="submit">Submit Reading</button>
</form>

<style>
  form {
    background-color: #ecf0f1;
    padding: 1em;
    border-radius: 8px;
    max-width: 400px;
    margin: 0 auto 2em auto;
  }

  div {
    margin-bottom: 1em;
  }

  label {
    display: block;
    margin-bottom: 0.25em;
    font-weight: bold;
  }

  input, textarea {
    width: 100%;
    padding: 0.5em;
    border: 1px solid #bdc3c7;
    border-radius: 4px;
    font-size: 1em;
  }

  button {
    background-color: #27ae60;
    color: white;
    border: none;
    padding: 0.75em 1.5em;
    font-size: 1em;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #219150;
  }
</style>
