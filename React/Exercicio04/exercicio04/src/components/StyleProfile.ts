import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  gap: 50px;
  align-items: center;
  justify-content: center;
  height: 100vh;
`;

export const Content = styled.div`
  display: flex;

  align-items: center;
  flex-direction: column;
  background-color: #041122;
  height: 75vh;
  width: 20vw;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: -4px 4px 15px rgba(0, 0, 0, 0.7);
`;
export const Avatar = styled.div`
  display: flex;
  flex-direction: column;
  gap: 35px;
  align-items: center;
  justify-content: center;
`;

export const NameProfile = styled.span`
  color: white;
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
`;

export const Imagem = styled.img`
  width: 7rem;
  border-radius: 15rem;
  background-size: cover;
  box-shadow: -4px 4px 5px rgba(0, 0, 0, 0.8);
`;

export const Line = styled.div`
  margin: 15px;
  width: 20rem;

  border-top: 0.5px solid #fff;
`;

export const Information = styled.span`
  color: white;
`;
