<script>
  import { onMount } from 'svelte';

  let moisture = '--';
  let temperature = '--';
  let lightIntensity = '--';
  let lastUpdated = '--';

  onMount(async () => {
    try {
      const response = await fetch('/api/latest_reading');
      if (response.ok) {
        const data = await response.json();
        moisture = data.moisture_level ?? '--';
        temperature = data.temperature ?? '--';
        lightIntensity = data.light_intensity ?? '--';
        lastUpdated = data.timestamp ?? '--';
      } else {
        console.error('Failed to fetch latest reading:', response.status);
      }
    } catch (error) {
      console.error('Error fetching latest reading:', error);
    }
  });
</script>

<section id="current-status">
  <h2>Current Plant Status</h2>
  <p>Soil Moisture: {moisture}%</p>
  <p>Temperature: {temperature}°C</p>
  <p>Light Intensity: {lightIntensity} Lux</p>
  <p>Last Updated: {lastUpdated}</p>
</section>

<style>
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
</style>
