<script>
  import { onMount, onDestroy } from 'svelte';
  import { afterUpdate } from 'svelte';
  import Chart from 'chart.js/auto';
  import { writable } from 'svelte/store';

  export let timeRange = '7days';

  let chartCanvas;
  let myChart;
  let chartData = writable({ labels: [], datasets: [] });

  async function fetchData(range) {
    try {
      let url = '/api/readings';
      if (range && range !== 'all') {
        url += `?range=${range}`;
      }
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();

      // Assuming data is an array of readings with timestamp and moisture_level
      const labels = data.map(item => new Date(item.timestamp).toLocaleString());
      const moistureData = data.map(item => item.moisture_level);

      chartData.set({
        labels: labels,
        datasets: [{
          label: 'Soil Moisture (%)',
          data: moistureData,
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      });
    } catch (error) {
      console.error('Failed to fetch data:', error);
      chartData.set({
        labels: [],
        datasets: []
      });
    }
  }

  let unsubscribe;

  onMount(() => {
    fetchData(timeRange);

    unsubscribe = chartData.subscribe(value => {
      if (myChart) {
        myChart.destroy();
      }
      const ctx = chartCanvas.getContext('2d');
      myChart = new Chart(ctx, {
        type: 'line',
        data: value,
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true,
              max: 100
            }
          }
        }
      });
    });
  });

  afterUpdate(() => {
    fetchData(timeRange);
  });

  onDestroy(() => {
    if (myChart) {
      myChart.destroy();
    }
    if (unsubscribe) {
      unsubscribe();
    }
  });
</script>

<canvas bind:this={chartCanvas}></canvas>

<style>
  canvas {
    max-width: 100%;
    height: 300px;
  }
</style>
