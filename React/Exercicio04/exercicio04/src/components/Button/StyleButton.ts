import styled from "styled-components";

export const Button = styled.button`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20rem;
  height: 2.5rem;
  margin: 0.5rem 0px;
  color: white;
  cursor: pointer;
  font-size: 1.2rem;
  border-radius: 10px;
  box-shadow: -4px 4px 5px rgba(0, 0, 0, 0.8);
`;

export const Center = styled.div`
  width: 9rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  gap: 0.7rem;
`;
export const Link = styled.a`
  text-decoration: none;
  color: white;
`;

export const Icon = styled.img`
  width: 1.5rem;
`;

export const Line = styled.div`
  border-left: 1px solid #fff;
  height: 1rem;
`;
