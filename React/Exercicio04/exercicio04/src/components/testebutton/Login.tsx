import React, { useState } from "react";
import Input from "./Input";
import Button from "./Button";

const Login = () => {
  const [dados, setDados] = useState("");
  const handleData = (data: string) => {
    console.log("Dados do input:", data);
    setDados(data);
  };

  const handleClick = (data: string) => {
    console.log("Dados enviados para o componente pai:", data);
    setDados(data);
    alert(dados);
  };

  return (
    <div>
      <Input onData={handleData} />
    </div>
  );
};

export default Login;
