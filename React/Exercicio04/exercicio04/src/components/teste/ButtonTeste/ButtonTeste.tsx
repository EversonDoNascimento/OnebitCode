import React, { useState } from "react";
import styled from "styled-components";

const getRandomTop = (): string => {
  const minNumber = 1;
  const maxNumber = 100;
  const randomNumber =
    Math.floor(Math.random() * (maxNumber - minNumber + 1)) + minNumber;
  return `${randomNumber}px`;
};

const Button = styled.button`
  padding: 0.2rem;
  position: relative;

  right: ${(props) => props.randomTop};

  &:hover {
    top: 0; /* Ou qualquer outro valor desejado para o hover */
    background-color: pink;
  }
`;

const MyButton = () => {
  const [randomTop, setRandomTop] = useState<string>(getRandomTop());

  const handleMouseEnter = () => {
    setRandomTop("0");
  };

  const handleMouseLeave = () => {
    setRandomTop(getRandomTop());
  };

  return (
    <Button
      randomTop={randomTop}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      My Button
    </Button>
  );
};

export default MyButton;
