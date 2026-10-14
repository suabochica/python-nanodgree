import React, { useState } from 'react';
import '../stylesheets/Question.css';

function Question({ question, answer, category, difficulty, questionAction }) {
  const [visibleAnswer, setVisibleAnswer] = useState(false);

  const flipVisibility = () => {
    setVisibleAnswer((prev) => !prev);
  };

  return (
    <div className='Question-holder'>
      <div className='Question'>{question}</div>
      <div className='Question-status'>
        <img
          className='category'
          alt={`${category.toLowerCase()}`}
          src={`${category.toLowerCase()}.svg`}
        />
        <div className='difficulty'>Difficulty: {difficulty}</div>
        <img
          src='delete.png'
          alt='delete'
          className='delete'
          onClick={() => questionAction('DELETE')}
        />
      </div>
      <div className='show-answer button' onClick={flipVisibility}>
        {visibleAnswer ? 'Hide' : 'Show'} Answer
      </div>
      <div className='answer-holder'>
        <span
          style={{
            visibility: visibleAnswer ? 'visible' : 'hidden',
          }}
        >
          Answer: {answer}
        </span>
      </div>
    </div>
  );
}

export default Question;
