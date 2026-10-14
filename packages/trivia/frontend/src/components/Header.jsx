import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../stylesheets/Header.css';

function Header() {
  const navigate = useNavigate();

  const navTo = (uri) => {
    navigate(uri);
  };

  return (
    <div className='App-header'>
      <h1 onClick={() => navTo('/')}>Udacitrivia</h1>
      <h2 onClick={() => navTo('/')}>List</h2>
      <h2 onClick={() => navTo('/add')}>Add</h2>
      <h2 onClick={() => navTo('/play')}>Play</h2>
    </div>
  );
}

export default Header;
