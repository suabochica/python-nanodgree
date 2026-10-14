import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import App from './App';

it('renders without crashing', () => {
  render(
    <MemoryRouter
      future={{
        v7_startTransition: true,
        v7_relativeSplatPath: true,
      }}
    >
      <App />
    </MemoryRouter>
  );
  expect(screen.getByText('Udacitrivia')).toBeInTheDocument();
});
