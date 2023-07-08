import React, { useEffect, useState } from "react";
interface Props {
  onData: (dados: string) => void;
}
const Input = ({ onData }: Props) => {
  const [inputValue, setInputValue] = useState("");

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleClick = () => {
    onData(inputValue);
  };

  return (
    <div>
      <input type="text" value={inputValue} onChange={handleChange} />
      <button onClick={handleClick}>Enviar</button>
    </div>
  );
};

export default Input;
