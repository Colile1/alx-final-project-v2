<script>
  import { onMount } from 'svelte';
  import CurrentStatus from './lib/CurrentStatus.svelte';
  import InputForm from './lib/InputForm.svelte';
  import ChartComponent from './lib/ChartComponent.svelte';

  let timeRange = '7days';

  function handleTimeRangeChange(event) {
    timeRange = event.target.value;
  }
</script>

<main>
  <header>
    <h1>Resource-Efficient Plant Care Dashboard</h1>
  </header>

  <CurrentStatus />

  <section id="manual-input">
    <InputForm />
  </section>

  <section id="historical-data">
    <label for="timeRangeSelect">Select Time Range: </label>
    <select id="timeRangeSelect" bind:value={timeRange} on:change={handleTimeRangeChange}>
      <option value="24hours">Last 24 Hours</option>
      <option value="7days">Last 7 Days</option>
      <option value="30days">Last 30 Days</option>
      <option value="all">All Data</option>
    </select>
    <ChartComponent {timeRange} />
  </section>

  <footer>
    <p>Last Updated: --</p>
  </footer>
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    padding: 1em;
    font-family: Arial, sans-serif;
  }

  header {
    text-align: center;
    margin-bottom: 2em;
  }

  header h1 {
    font-size: 2em;
    color: #2c3e50;
  }

  #manual-input {
    text-align: center;
    margin-bottom: 2em;
  }

  #manual-input button {
    background-color: #27ae60;
    color: white;
    border: none;
    padding: 0.75em 1.5em;
    font-size: 1em;
    border-radius: 4px;
    cursor: pointer;
  }

  #manual-input button:hover {
    background-color: #219150;
  }

  #historical-data {
    margin-top: 1em;
    text-align: center;
  }

  #timeRangeSelect {
    margin-bottom: 1em;
    padding: 0.5em;
    font-size: 1em;
    border-radius: 4px;
    border: 1px solid #ccc;
  }

  footer {
    text-align: center;
    color: #7f8c8d;
    font-size: 0.9em;
  }
</style>
