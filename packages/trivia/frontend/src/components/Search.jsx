import React, { useRef, useState } from 'react';

function Search({ submitSearch }) {
  const [query, setQuery] = useState('');
  const inputRef = useRef(null);

  const handleInputChange = () => {
    setQuery(inputRef.current.value);
  };

  const getInfo = (event) => {
    event.preventDefault();
    submitSearch(query);
  };

  return (
    <form onSubmit={getInfo}>
      <input
        placeholder='Search questions...'
        ref={inputRef}
        onChange={handleInputChange}
      />
      <input type='submit' value='Submit' className='button' />
    </form>
  );
}

export default Search;
