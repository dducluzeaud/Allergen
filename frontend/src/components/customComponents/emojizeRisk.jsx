import React from 'react';

const emojizeRisk = (risk) => {
  const emoji = {
    0: () => (
      <span role="img" aria-label="red-heart">
        ❤️
      </span>
    ),
    1: () => (
      <span role="img" aria-label="green-heart">
        💚
      </span>
    ),
    2: () => (
      <span role="img" aria-label="check">
        ✅
      </span>
    ),
    3: () => (
      <span role="img" aria-label="heartBroken">
        💔
      </span>
    ),
    4: () => (
      <span role="img" aria-label="forbidden">
        ⛔️
      </span>
    ),
    default: () => null,
  };

  return (emoji[risk] || emoji.default)();
};

export default emojizeRisk;
