import React, { useEffect, useState } from 'react';
import '../stylesheets/App.css';
import Question from './Question';
import Search from './Search';

const QUESTIONS_PER_PAGE = 10;

function QuestionView() {
  const [questions, setQuestions] = useState([]);
  const [page, setPage] = useState(1);
  const [totalQuestions, setTotalQuestions] = useState(0);
  const [categories, setCategories] = useState({});
  const [currentCategory, setCurrentCategory] = useState(null);

  const getQuestions = (currentPage = page) => {
    fetch(`/api/questions?page=${currentPage}`)
      .then((res) => res.json())
      .then((result) => {
        setQuestions(result.questions);
        setTotalQuestions(result.total_questions);
        setCategories(result.categories);
        setCurrentCategory(result.current_category);
      })
      .catch(() => {
        alert('Unable to load questions. Please try your request again');
      });
  };

  useEffect(() => {
    getQuestions();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const selectPage = (num) => {
    setPage(num);
    getQuestions(num);
  };

  const createPagination = () => {
    const pageNumbers = [];
    const maxPage = Math.ceil(totalQuestions / QUESTIONS_PER_PAGE);
    for (let i = 1; i <= maxPage; i++) {
      pageNumbers.push(
        <span
          key={i}
          className={`page-num ${i === page ? 'active' : ''}`}
          onClick={() => selectPage(i)}
        >
          {i}
        </span>
      );
    }
    return pageNumbers;
  };

  const getByCategory = (id) => {
    fetch(`/api/categories/${id}/questions`)
      .then((res) => res.json())
      .then((result) => {
        setQuestions(result.questions);
        setTotalQuestions(result.total_questions);
        setCurrentCategory(result.current_category);
      })
      .catch(() => {
        alert('Unable to load questions. Please try your request again');
      });
  };

  const submitSearch = (searchTerm) => {
    fetch('/api/questions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ searchTerm }),
    })
      .then((res) => res.json())
      .then((result) => {
        setQuestions(result.questions);
        setTotalQuestions(result.total_questions);
        setCurrentCategory(result.current_category);
      })
      .catch(() => {
        alert('Unable to load questions. Please try your request again');
      });
  };

  const questionAction = (id) => (action) => {
    if (action === 'DELETE') {
      if (window.confirm('are you sure you want to delete the question?')) {
        fetch(`/api/questions/${id}`, { method: 'DELETE' })
          .then(() => {
            getQuestions();
          })
          .catch(() => {
            alert('Unable to load questions. Please try your request again');
          });
      }
    }
  };

  return (
    <div className='question-view'>
      <div className='categories-list'>
        <h2 onClick={() => getQuestions()}>Categories</h2>
        <ul>
          {Object.keys(categories).map((id) => (
            <li key={id} onClick={() => getByCategory(id)}>
              {categories[id]}
              <img
                className='category'
                alt={`${categories[id].toLowerCase()}`}
                src={`${categories[id].toLowerCase()}.svg`}
              />
            </li>
          ))}
        </ul>
        <Search submitSearch={submitSearch} />
      </div>
      <div className='questions-list'>
        <h2>Questions</h2>
        {questions.map((q) => (
          <Question
            key={q.id}
            question={q.question}
            answer={q.answer}
            category={categories[q.category]}
            difficulty={q.difficulty}
            questionAction={questionAction(q.id)}
          />
        ))}
        <div className='pagination-menu'>{createPagination()}</div>
      </div>
    </div>
  );
}

export default QuestionView;
