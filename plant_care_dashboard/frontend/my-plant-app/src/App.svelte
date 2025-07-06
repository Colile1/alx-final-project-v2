<script>
  import CurrentStatus from './lib/CurrentStatus.svelte';
</script>

<main>
  <header>
    <h1>Resource-Efficient Plant Care Dashboard</h1>
  </header>

  <CurrentStatus />

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
