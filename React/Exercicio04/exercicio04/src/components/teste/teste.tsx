import { Props } from "./type";
import { useState } from "react";
import "bulma/css/bulma.css";
import * as C from "./styleTeste";
import MyButton from "./ButtonTeste/ButtonTeste";
import React, { ChangeEvent } from "react";
import {
  Alert,
  AlertIcon,
  AlertTitle,
  AlertDescription,
  PinInput,
  PinInputField,
  Button,
} from "@chakra-ui/react";

export const Teste = ({ restProps, children }: Props) => {
  const [inputValue, setInputValue] = useState<number[]>([]);

  const handleChange = (event: ChangeEvent<HTMLInputElement>): void => {
    setInputValue((prevValue) => [...prevValue, Number(event.target.value)]);
  };
  const handleSubmit = (): void => {
    console.log("Valor do input:", inputValue);
  };
  return (
    <>
      <C.Container {...restProps}>
        {/*
        <C.Content className={"link"}>
          {children}
          <C.Button>Login</C.Button>
          <MyButton></MyButton>
        </C.Content>
        <Alert status="error">
          <AlertIcon />
          <AlertTitle>Your browser is outdated!</AlertTitle>
          <AlertDescription>
            Your Chakra experience may be degraded.
          </AlertDescription>
        </Alert>
*/}
        <PinInput otp>
          <PinInputField type="number" onChange={handleChange} />
          <PinInputField type="number" onChange={handleChange} />
          <PinInputField type="number" onChange={handleChange} />
          <PinInputField type="number" onChange={handleChange} />
          <PinInputField type="number" onChange={handleChange} />
          <PinInputField type="number" onChange={handleChange} />
        </PinInput>
        <Button onClick={handleSubmit}>Enviar</Button>
      </C.Container>
    </>
  );
};
