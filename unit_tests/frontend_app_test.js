/**
 * Basic frontend tests for App.svelte using Jest and @testing-library/svelte
 */

import { render } from '@testing-library/svelte';
import App from '../plant_care_dashboard/frontend/my-plant-app/src/App.svelte';

describe('App component', () => {
  test('renders greeting with name prop', () => {
    const { getByText } = render(App, { props: { name: 'world' } });
    expect(getByText('Hello world!')).toBeInTheDocument();
  });

  test('contains link to Svelte tutorial', () => {
    const { getByText } = render(App);
    const link = getByText('Svelte tutorial');
    expect(link).toBeInTheDocument();
    expect(link.getAttribute('href')).toBe('https://svelte.dev/tutorial');
  });
});
