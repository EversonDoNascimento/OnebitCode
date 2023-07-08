import styled from "styled-components";

const getRandomTop = (): string => {
  const minNumber = 1;
  const maxNumber = 1000;
  const randomNumber =
    Math.floor(Math.random() * (maxNumber - minNumber + 1)) + minNumber;
  return `${randomNumber}px`;
};

console.log(getRandomTop());

export const Container = styled.div`
  display: flex;
  height: 100vh;
  width: 100vw;
  justify-content: center;
  align-items: center;
`;

export const Content = styled.div`
  color: white;
  background-color: black;
  width: 150px;
  height: 200px;
  position: absolute;

  @media (max-width: 480px) {
    width: 250px;
    height: 400px;
  }

  @media (min-width: 481px) and (max-width: 650px) {
    width: 300px;
    height: 450px;

    &.link:hover {
      background-color: pink;
    }
  }
`;

export const Button = styled.button`
  padding: 0.2rem;
  position: relative;
  &:hover {
    top: ${getRandomTop()};
  }
`;
