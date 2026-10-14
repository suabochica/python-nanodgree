import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './stylesheets/App.css';
import FormView from './components/FormView';
import QuestionView from './components/QuestionView';
import Header from './components/Header';
import QuizView from './components/QuizView';

function App() {
  return (
    <div className='App'>
      <Header />
      <Routes>
        <Route path='/' element={<QuestionView />} />
        <Route path='/add' element={<FormView />} />
        <Route path='/play' element={<QuizView />} />
        <Route path='*' element={<QuestionView />} />
      </Routes>
    </div>
  );
}

export default App;
