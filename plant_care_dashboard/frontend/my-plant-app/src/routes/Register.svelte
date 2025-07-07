<script>
  import { createEventDispatcher } from 'svelte';

  let username = '';
  let password = '';
  let confirmPassword = '';
  let errorMessage = '';
  let successMessage = '';

  const dispatch = createEventDispatcher();

  async function handleRegister(event) {
    event.preventDefault();
    errorMessage = '';
    successMessage = '';

    if (password !== confirmPassword) {
      errorMessage = 'Passwords do not match';
      return;
    }

    try {
      const response = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });

      if (response.ok) {
        successMessage = 'Registration successful! You can now log in.';
        username = '';
        password = '';
        confirmPassword = '';
      } else {
        const data = await response.json();
        errorMessage = data.message || 'Registration failed';
      }
    } catch (error) {
      errorMessage = 'Network error: ' + error.message;
    }
  }
</script>

<form on:submit|preventDefault={handleRegister}>
  <h2>Register</h2>
  {#if errorMessage}
    <p style="color: red;">{errorMessage}</p>
  {/if}
  {#if successMessage}
    <p style="color: green;">{successMessage}</p>
  {/if}
  <div>
    <label for="username">Username</label>
    <input id="username" type="text" bind:value={username} required />
  </div>
  <div>
    <label for="password">Password</label>
    <input id="password" type="password" bind:value={password} required />
  </div>
  <div>
    <label for="confirmPassword">Confirm Password</label>
    <input id="confirmPassword" type="password" bind:value={confirmPassword} required />
  </div>
  <button type="submit">Register</button>
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
