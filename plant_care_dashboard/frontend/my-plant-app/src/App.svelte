<script>
  // No props needed for now
</script>

<main>
  <header>
    <h1>Resource-Efficient Plant Care Dashboard</h1>
  </header>

  <section id="current-status">
    <h2>Current Plant Status</h2>
    <!-- Placeholder for current status metrics -->
    <p>Soil Moisture: --%</p>
    <p>Temperature: --°C</p>
    <p>Light Intensity: -- Lux</p>
  </section>

  <section id="manual-input">
    <button>Manual Input</button>
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

  #current-status {
    background-color: #ecf0f1;
    padding: 1em;
    border-radius: 8px;
    margin-bottom: 2em;
  }

  #current-status h2 {
    margin-top: 0;
    color: #34495e;
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

  footer {
    text-align: center;
    color: #7f8c8d;
    font-size: 0.9em;
  }
</style>
