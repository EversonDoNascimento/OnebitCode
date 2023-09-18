import React from "react";

const Button = ({ onClick }) => {
  const handleClick = () => {
    onClick();
  };

  return <button onClick={handleClick}>Clique aqui</button>;
};

export default Button;
