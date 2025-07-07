<script>
  import { onMount } from 'svelte';
  import { onDestroy } from 'svelte';
  import { refreshData } from '../App.svelte';

  let moisture = '--';
  let temperature = '--';
  let lightIntensity = '--';
  let lastUpdated = '--';

  // Define thresholds
  const DRY_THRESHOLD = 40;
  const WET_THRESHOLD = 85;
  const TEMP_HIGH_THRESHOLD = 30;
  const TEMP_LOW_THRESHOLD = 15;
  const LIGHT_LOW_THRESHOLD = 500;

  let moistureStatus = '';
  let temperatureStatus = '';
  let lightStatus = '';

  function updateStatuses() {
    if (moisture === '--') {
      moistureStatus = '';
    } else if (moisture < DRY_THRESHOLD) {
      moistureStatus = 'dry';
    } else if (moisture > WET_THRESHOLD) {
      moistureStatus = 'wet';
    } else {
      moistureStatus = 'moderate';
    }

    if (temperature === '--') {
      temperatureStatus = '';
    } else if (temperature > TEMP_HIGH_THRESHOLD) {
      temperatureStatus = 'high';
    } else if (temperature < TEMP_LOW_THRESHOLD) {
      temperatureStatus = 'low';
    } else {
      temperatureStatus = 'optimal';
    }

    if (lightIntensity === '--') {
      lightStatus = '';
    } else if (lightIntensity < LIGHT_LOW_THRESHOLD) {
      lightStatus = 'low';
    } else {
      lightStatus = 'good';
    }
  }

  async function fetchLatestReading() {
    try {
      const response = await fetch('/api/latest_reading');
      if (response.ok) {
        const data = await response.json();
        moisture = data.moisture_level ?? '--';
        temperature = data.temperature ?? '--';
        lightIntensity = data.light_intensity ?? '--';
        lastUpdated = data.timestamp ?? '--';
        updateStatuses();
      } else {
        console.error('Failed to fetch latest reading:', response.status);
      }
    } catch (error) {
      console.error('Error fetching latest reading:', error);
    }
  }

  let nextWateringEstimate = '--';

  async function fetchNextWatering() {
    try {
      const response = await fetch('/api/next_watering');
      if (response.ok) {
        const data = await response.json();
        nextWateringEstimate = new Date(data.next_watering_estimate).toLocaleString();
      } else {
        nextWateringEstimate = 'Unavailable';
        console.error('Failed to fetch next watering estimate:', response.status);
      }
    } catch (error) {
      nextWateringEstimate = 'Error';
      console.error('Error fetching next watering estimate:', error);
    }
  }

  let unsubscribe;

  onMount(() => {
    fetchLatestReading();
    fetchNextWatering();
    unsubscribe = refreshData.subscribe(() => {
      fetchLatestReading();
      fetchNextWatering();
    });
  });

  onDestroy(() => {
    if (unsubscribe) unsubscribe();
  });
</script>

<section id="current-status">
  <h2>Current Plant Status</h2>
  <p class:dry={moistureStatus === 'dry'} class:moderate={moistureStatus === 'moderate'} class:wet={moistureStatus === 'wet'}>
    Soil Moisture: {moisture}%
    {#if moistureStatus === 'dry'}
      - Plant needs water!
    {/if}
  </p>
  <p class:high={temperatureStatus === 'high'} class:low={temperatureStatus === 'low'} class:optimal={temperatureStatus === 'optimal'}>
    Temperature: {temperature}°C
  </p>
  <p class:low={lightStatus === 'low'} class:good={lightStatus === 'good'}>
    Light Intensity: {lightIntensity} Lux
  </p>
  <p>Last Updated: {lastUpdated}</p>
  <p>Next Watering Estimate: {nextWateringEstimate}</p>
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

  /* Moisture status styles */
  p.dry {
    color: red;
    font-weight: bold;
  }

  p.moderate {
    color: orange;
  }

  p.wet {
    color: green;
  }

  /* Temperature status styles */
  p.high {
    color: red;
    font-weight: bold;
  }

  p.low {
    color: blue;
  }

  p.optimal {
    color: green;
  }

  /* Light intensity status styles */
  p.low {
    color: orange;
  }

  p.good {
    color: green;
  }
</style>
