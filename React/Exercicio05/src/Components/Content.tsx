import { Generate } from "../Generate_Password/Generate";
import {
  Heading,
  Stack,
  Text,
  Button,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
  NumberIncrementStepper,
  NumberDecrementStepper,
} from "@chakra-ui/react";
import * as C from "./styledContent";
import { useEffect, useState } from "react";

export const Content = (): JSX.Element | null => {
  //Função para screenSize
  const [windowSize, setWindowSize] = useState<number>({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  useEffect(() => {
    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);
  //Fim

  const [password, setPassword] = useState(
    "Clique no botão abaixo para gerar sua senha!"
  );
  const [infoButtonCopy, setInfoButtonCopy] = useState("Copiar Senha");
  const [infoGeneratePass, setInfoGeneratePass] = useState("Gerar Senha");
  const [infoTextCopy, setInfoTextCopy] = useState(password);
  const [condTime, setCondTime] = useState<boolean>(false);
  const [sizePass, setSizePass] = useState<number>(4);

  const [counter, setCounter] = useState(0);

  useEffect(() => {
    const timer = setTimeout(() => {
      if (counter !== 5) {
        setCounter((prevCounter) => prevCounter + 1);
        setCondTime(false);
      } else {
        setCounter(5);
        setInfoButtonCopy("Copiar Senha");
        setInfoTextCopy(password);
        if (condTime) {
          setCounter(0);
        }
      }
    }, 1000);

    return () => {
      clearTimeout(timer);
    };
  }, [counter, condTime]);
  useEffect(() => {
    setInfoTextCopy(password);
  }, [password]);
  const handleCopy = () => {
    if (password !== "Clique no botão abaixo para gerar sua senha!") {
      navigator.clipboard
        .writeText(password)
        .then(() => {
          console.log("Texto copiado com sucesso!");
          setInfoButtonCopy("Senha copiada!");
          setInfoTextCopy("Senha copiada com sucesso!");
          setCondTime(true);
        })
        .catch((error) => {
          console.error("Erro ao copiar o texto:", error);
        });
    } else {
      alert("Por favor, gere uma senha antes de copiar!!");
    }
  };
  const handleGeneratePassword = (): void => {
    setPassword(Generate(sizePass));
    setInfoGeneratePass("Gerar Outra Senha");
  };

  return (
    <>
      <C.Container>
        <C.Content>
          <Heading as={"h1"} size={windowSize <= 280 ? "md" : "lg"}>
            Gerador de Senhas
          </Heading>
          <Text
            onClick={handleCopy}
            _hover={{ bg: "blue.600", cursor: "pointer" }}
            p={"10px"}
            bg={"#2e2e2e"}
            borderRadius={"10px"}
            fontSize={windowSize <= 280 ? "1.5rem" : "1rem"}
          >
            {infoTextCopy}
          </Text>
          <C.Controls>
            <NumberInput
              onChange={(e) => {
                setSizePass(e);
              }}
              defaultValue={6}
              min={4}
              max={15}
            >
              <NumberInputField />
              <NumberInputStepper>
                <NumberIncrementStepper />
                <NumberDecrementStepper />
              </NumberInputStepper>
            </NumberInput>
            <Stack direction={["column", "row"]} spacing="24px">
              <Button
                variant={"outline"}
                color={"#fff"}
                _hover={{ backgroundColor: "green.400" }}
                onClick={handleGeneratePassword}
                colorScheme="teal"
                size="md"
              >
                {infoGeneratePass}
              </Button>
              <Button
                variant={"outline"}
                color={"#fff"}
                _hover={{ backgroundColor: "blue.600" }}
                onClick={handleCopy}
                colorScheme="teal"
                size="md"
              >
                {infoButtonCopy}
              </Button>
            </Stack>
          </C.Controls>
        </C.Content>
      </C.Container>
    </>
  );
};
