import React, { useEffect, useState } from 'react';
import '../stylesheets/FormView.css';

function FormView() {
  const [formData, setFormData] = useState({
    question: '',
    answer: '',
    difficulty: 1,
    category: 1,
  });
  const [categories, setCategories] = useState({});

  useEffect(() => {
    fetch('/api/categories')
      .then((res) => res.json())
      .then((result) => {
        setCategories(result.categories);
      })
      .catch(() => {
        alert('Unable to load categories. Please try your request again');
      });
  }, []);

  const handleChange = (event) => {
    setFormData((prev) => ({
      ...prev,
      [event.target.name]: event.target.value,
    }));
  };

  const submitQuestion = (event) => {
    event.preventDefault();
    fetch('/api/questions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    })
      .then(() => {
        document.getElementById('add-question-form').reset();
        setFormData({ question: '', answer: '', difficulty: 1, category: 1 });
      })
      .catch(() => {
        alert('Unable to add question. Please try your request again');
      });
  };

  return (
    <div id='add-form'>
      <h2>Add a New Trivia Question</h2>
      <form
        className='form-view'
        id='add-question-form'
        onSubmit={submitQuestion}
      >
        <label>
          Question
          <input type='text' name='question' onChange={handleChange} />
        </label>
        <label>
          Answer
          <input type='text' name='answer' onChange={handleChange} />
        </label>
        <label>
          Difficulty
          <select name='difficulty' onChange={handleChange}>
            <option value='1'>1</option>
            <option value='2'>2</option>
            <option value='3'>3</option>
            <option value='4'>4</option>
            <option value='5'>5</option>
          </select>
        </label>
        <label>
          Category
          <select name='category' onChange={handleChange}>
            {Object.keys(categories).map((id) => (
              <option key={id} value={id}>
                {categories[id]}
              </option>
            ))}
          </select>
        </label>
        <input type='submit' className='button' value='Submit' />
      </form>
    </div>
  );
}

export default FormView;
