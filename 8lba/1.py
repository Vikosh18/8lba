import React from 'react';
import ReactDOM from 'react-dom';

// Створення компоненту
function Hello() {
  return <div>Hello, World!</div>;
}

// Рендеринг компоненту в DOM
ReactDOM.render(
  <Hello />,
  document.getElementById('root')
);

