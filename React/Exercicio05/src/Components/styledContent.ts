import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 100vh;
`;

export const Content = styled.div`
  color: white;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  flex-direction: column;
  background-color: #4a4a4a;
  width: 40rem;
  height: 25rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  @media (max-width: 500px) {
    background-color: #2e2e2e;
    width: 100vw;
    height: 100wh;
  }

  @media (max-width: 720px) {
    background-color: #2e2e2e;
    width: 100vw;
    height: 100wh;
  }
`;

export const Controls = styled.div`
  display: flex;
  flex-direction: column;
  gap: 15px;
`;
