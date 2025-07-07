<script>
  import { createEventDispatcher } from 'svelte';
  import { onMount } from 'svelte';

  let username = '';
  let password = '';
  let errorMessage = '';

  const dispatch = createEventDispatcher();

  async function handleLogin(event) {
    event.preventDefault();
    errorMessage = '';

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ username, password })
      });

      if (response.ok) {
        dispatch('loginSuccess');
      } else {
        const data = await response.json();
        errorMessage = data.message || 'Login failed';
      }
    } catch (error) {
      errorMessage = 'Network error: ' + error.message;
    }
  }
</script>

<form on:submit|preventDefault={handleLogin}>
  <h2>Login</h2>
  {#if errorMessage}
    <p style="color: red;">{errorMessage}</p>
  {/if}
  <div>
    <label for="username">Username</label>
    <input id="username" type="text" bind:value={username} required />
  </div>
  <div>
    <label for="password">Password</label>
    <input id="password" type="password" bind:value={password} required />
  </div>
  <button type="submit">Login</button>
</form>

<style>
  form {
    max-width: 400px;
    margin: 2em auto;
    padding: 1em;
    background-color: #ecf0f1;
    border-radius: 8px;
  }
  div {
    margin-bottom: 1em;
  }
  label {
    display: block;
    margin-bottom: 0.25em;
    font-weight: bold;
  }
  input {
    width: 100%;
    padding: 0.5em;
    border: 1px solid #bdc3c7;
    border-radius: 4px;
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
